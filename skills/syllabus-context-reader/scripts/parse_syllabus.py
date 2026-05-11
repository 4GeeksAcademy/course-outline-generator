#!/usr/bin/env python3
"""
parse_syllabus.py — Extracts structured context from the AI Engineer (or AI Native Full Stack) syllabus CSV.

Usage:
  python3 parse_syllabus.py --csv <path> --week <n> --day <n>
  python3 parse_syllabus.py --csv <path> --week <n> --day <n> --include-prior
  python3 parse_syllabus.py --csv <path> --list
  python3 parse_syllabus.py --csv <path> --search "keyword"

Output: JSON with the lesson context (skill, content, how_to_think, best_practices,
        patterns, anti_patterns, limitaciones) plus optional cumulative prior skills.
"""

import argparse
import json
import math
import re
import sys
import pandas as pd


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def _clean(val) -> str | None:
    """Return stripped string or None for NaN / empty."""
    if val is None or (isinstance(val, float) and math.isnan(val)):
        return None
    s = str(val).strip()
    return s if s else None


def _is_day_row(row) -> bool:
    """A day/session row has a numeric (or special) week AND a Skill: description."""
    week_raw = _clean(row.iloc[0])
    day_raw = _clean(row.iloc[1])
    content = _clean(row.iloc[2])
    if not week_raw or not day_raw or not content:
        return False
    return "skill:" in content.lower()


def _is_milestone_row(row) -> bool:
    """Milestones have 'HITO' in column 0."""
    week_raw = _clean(row.iloc[0])
    return bool(week_raw and week_raw.upper().startswith("HITO"))


def _parse_week_day(row):
    """Returns (week_str, day_str) from a day row."""
    return _clean(row.iloc[0]), _clean(row.iloc[1])


def _extract_milestone_title(milestone_id: str, content: str) -> str:
    """
    For milestone rows, try to find the human-readable title embedded in the
    content (e.g. '🎨 Hito 4 — ...', 'Hito 3 —...', '⚛️ Hito 3 —...').
    Falls back to first non-empty line of content.
    """
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        # Match patterns like "Hito N —", "🎨 Hito N —", "⚛️ Hito 3 —"
        if re.search(r"[Hh]ito\s+\d+\s*[—–-]", line):
            return f"[{milestone_id}] {line}"
    # Fallback: first non-empty line
    first = next((l.strip() for l in content.splitlines() if l.strip()), "")
    return f"[{milestone_id}] {first[:80]}" if first else milestone_id


def _extract_skill_name(content: str) -> str:
    """Pull the human-readable skill name from 'Skill: ...' lines."""
    lines = [l.strip() for l in content.splitlines() if "skill:" in l.lower()]
    skills = []
    for line in lines:
        match = re.search(r"[Ss]kill\s*:\s*(.+)", line)
        if match:
            skills.append(match.group(1).strip())
    return " | ".join(skills) if skills else content.strip()


def _build_content_block(row) -> dict:
    """Convert a content/project row into a structured dict."""
    return {
        "status":         _clean(row.iloc[1]),
        "content":        _clean(row.iloc[2]),
        "how_to_think":   _clean(row.iloc[3]),
        "best_practices": _clean(row.iloc[4]),
        "patterns":       _clean(row.iloc[5]),
        "anti_patterns":  _clean(row.iloc[6]),
        "limitaciones":   _clean(row.iloc[7]),
    }


# ---------------------------------------------------------------------------
# Main loader
# ---------------------------------------------------------------------------

def load_syllabus(csv_path: str) -> list[dict]:
    """
    Parse the CSV into a list of lesson dicts, each with:
      week, day, skill_raw, skill_name, blocks (list of content dicts),
      is_milestone, milestone_id
    """
    df = pd.read_csv(csv_path, header=None, dtype=str)
    lessons = []
    current_lesson = None

    for _, row in df.iterrows():
        week_val = _clean(row.iloc[0])

        # Section separator rows (---) — skip
        content_val = _clean(row.iloc[2])
        if content_val and content_val.startswith("---"):
            if current_lesson:
                lessons.append(current_lesson)
                current_lesson = None
            continue

        # Section header rows (### ... ###) — skip
        if content_val and content_val.startswith("###"):
            continue

        # Milestone row
        if _is_milestone_row(row):
            if current_lesson:
                lessons.append(current_lesson)
            milestone_id = _clean(row.iloc[0])
            # Try to find a human-readable title: "Hito N —..." or emoji-prefixed lines
            skill_name = _extract_milestone_title(
                milestone_id, content_val or "")
            current_lesson = {
                "week":         milestone_id,
                "day":          _clean(row.iloc[1]),
                "skill_raw":    content_val or "",
                "skill_name":   skill_name,
                "is_milestone": True,
                "milestone_id": milestone_id,
                "blocks":       [],
            }
            # Milestone row itself may have a content block
            block = _build_content_block(row)
            if any(v for v in block.values()):
                current_lesson["blocks"].append(block)
            continue

        # Day / session row
        if _is_day_row(row):
            if current_lesson:
                lessons.append(current_lesson)
            week_str, day_str = _parse_week_day(row)
            current_lesson = {
                "week":         week_str,
                "day":          day_str,
                "skill_raw":    content_val or "",
                "skill_name":   _extract_skill_name(content_val or ""),
                "is_milestone": False,
                "milestone_id": None,
                "blocks":       [],
            }
            continue

        # Content / project row — attach to current lesson
        if current_lesson is not None and content_val:
            block = _build_content_block(row)
            current_lesson["blocks"].append(block)

    if current_lesson:
        lessons.append(current_lesson)

    return lessons


# ---------------------------------------------------------------------------
# Query helpers
# ---------------------------------------------------------------------------

def _lesson_index(lessons: list[dict], week: str, day: str) -> int | None:
    """Return the list index of the requested lesson, or None."""
    for i, lesson in enumerate(lessons):
        if lesson["week"] == week and lesson["day"] == day:
            return i
    return None


def _merge_blocks(blocks: list[dict]) -> dict:
    """Merge multiple content blocks into one, concatenating non-null fields."""
    merged = {
        "content":        [],
        "how_to_think":   [],
        "best_practices": [],
        "patterns":       [],
        "anti_patterns":  [],
        "limitaciones":   [],
        "statuses":       [],
    }
    for b in blocks:
        for key in ("content", "how_to_think", "best_practices", "patterns",
                    "anti_patterns", "limitaciones"):
            val = b.get(key)
            if val:
                merged[key].append(val)
        if b.get("status"):
            merged["statuses"].append(b["status"])

    return {k: "\n\n---\n\n".join(v) if v else None for k, v in merged.items()}


def format_lesson(lesson: dict, include_raw: bool = False) -> dict:
    """Return a clean, serialisable representation of a lesson."""
    merged = _merge_blocks(lesson["blocks"])
    out = {
        "week":         lesson["week"],
        "day":          lesson["day"],
        "is_milestone": lesson["is_milestone"],
        "skill":        lesson["skill_name"],
        **merged,
    }
    if include_raw:
        out["skill_raw"] = lesson["skill_raw"]
    return out


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Query the AI Engineer or AI Native Full Stack syllabus.")
    parser.add_argument("--csv", required=True,
                        help="Path to the syllabus CSV file")
    parser.add_argument("--week", help="Week number (e.g. 1, 2, 0)")
    parser.add_argument("--day",  help="Day number (e.g. 1, -1, 4 y 5)")
    parser.add_argument("--include-prior", action="store_true",
                        help="Also return a summary of all prior skills")
    parser.add_argument("--list", action="store_true",
                        help="List all lessons (week, day, skill_name)")
    parser.add_argument(
        "--search", help="Search for a keyword across all lessons")
    args = parser.parse_args()

    lessons = load_syllabus(args.csv)

    # --list
    if args.list:
        index = [{"week": l["week"], "day": l["day"], "skill": l["skill_name"],
                  "is_milestone": l["is_milestone"]} for l in lessons]
        print(json.dumps(index, ensure_ascii=False, indent=2))
        return

    # --search
    if args.search:
        kw = args.search.lower()
        results = []
        for lesson in lessons:
            haystack = (lesson["skill_name"] + lesson["skill_raw"] +
                        " ".join(b.get("content") or "" for b in lesson["blocks"])).lower()
            if kw in haystack:
                results.append(format_lesson(lesson))
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    # --week + --day
    if not args.week or not args.day:
        parser.error("Provide --week and --day (or --list / --search).")

    idx = _lesson_index(lessons, args.week, args.day)
    if idx is None:
        print(json.dumps({"error": f"No lesson found for week={args.week} day={args.day}"},
                         ensure_ascii=False))
        sys.exit(1)

    result = {"current": format_lesson(lessons[idx], include_raw=True)}

    if args.include_prior and idx > 0:
        result["prior_skills"] = [
            {"week": l["week"], "day": l["day"], "skill": l["skill_name"]}
            for l in lessons[:idx]
        ]

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
