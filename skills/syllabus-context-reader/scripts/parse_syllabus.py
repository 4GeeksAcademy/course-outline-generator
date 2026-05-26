#!/usr/bin/env python3
"""
parse_syllabus.py — Extracts structured context from the AI Engineer (or AI Native Full Stack) syllabus CSV.

Usage:
  python3 parse_syllabus.py --csv <path> --week <n> --day <n>
  python3 parse_syllabus.py --csv <path> --week <n> --day <n> --include-prior
  python3 parse_syllabus.py --csv <path> --list
  python3 parse_syllabus.py --csv <path> --search "keyword"

Output: compact JSON by default (use --pretty for indented). Search returns index
        rows only; run --week/--day for full lesson context. With --include-prior,
        prior_skills uses smart mode (all prior milestones + last N regular lessons).
"""

import argparse
import json
import math
import re
import sys

import pandas as pd

DEFAULT_PRIOR_WINDOW = 15


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def _dump(data, *, pretty: bool = False) -> None:
    """Print JSON; compact by default to reduce token usage."""
    if pretty:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(data, ensure_ascii=False, separators=(",", ":")))


def _lesson_ref(lesson: dict) -> dict:
    return {
        "week": lesson["week"],
        "day": lesson["day"],
        "skill": lesson["skill_name"],
        "is_milestone": lesson["is_milestone"],
    }


def build_prior_skills(
    lessons: list[dict],
    idx: int,
    *,
    mode: str = "smart",
    window: int = DEFAULT_PRIOR_WINDOW,
) -> tuple[list[dict], dict]:
    """
    Build prior_skills list and metadata.

    Modes:
      full       — every lesson before idx
      milestones — milestones only
      smart      — all prior milestones + last `window` regular (non-milestone) lessons
    """
    prior = lessons[:idx]
    total = len(prior)

    if mode == "full":
        refs = [_lesson_ref(l) for l in prior]
        return refs, {"mode": "full", "total_prior": total, "returned": len(refs)}

    if mode == "milestones":
        refs = [_lesson_ref(l) for l in prior if l["is_milestone"]]
        return refs, {
            "mode": "milestones",
            "total_prior": total,
            "returned": len(refs),
        }

    # smart: milestones in order + recent regular lessons
    regular_positions = [
        i for i, lesson in enumerate(prior) if not lesson["is_milestone"]
    ]
    recent_positions = set(
        regular_positions[-window:]) if window > 0 else set()
    refs = [
        _lesson_ref(lesson)
        for i, lesson in enumerate(prior)
        if lesson["is_milestone"] or i in recent_positions
    ]
    return refs, {
        "mode": "smart",
        "window": window,
        "total_prior": total,
        "returned": len(refs),
    }


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
        if re.search(r"[Hh]ito\s+\d+\s*[—–-]", line):
            return f"[{milestone_id}] {line}"
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
        content_val = _clean(row.iloc[2])
        if content_val and content_val.startswith("---"):
            if current_lesson:
                lessons.append(current_lesson)
                current_lesson = None
            continue

        if content_val and content_val.startswith("###"):
            continue

        if _is_milestone_row(row):
            if current_lesson:
                lessons.append(current_lesson)
            milestone_id = _clean(row.iloc[0])
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
            block = _build_content_block(row)
            if any(v for v in block.values()):
                current_lesson["blocks"].append(block)
            continue

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


def _search_haystack(lesson: dict) -> str:
    return (
        lesson["skill_name"]
        + lesson["skill_raw"]
        + " ".join(b.get("content") or "" for b in lesson["blocks"])
    ).lower()


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Query the AI Engineer or AI Native Full Stack syllabus.")
    parser.add_argument("--csv", required=True,
                        help="Path to the syllabus CSV file")
    parser.add_argument("--week", help="Week number (e.g. 1, 2, 0)")
    parser.add_argument("--day", help="Day number (e.g. 1, -1, 4 y 5)")
    parser.add_argument(
        "--include-prior",
        action="store_true",
        help=(
            "Include prior_skills (default mode: all prior milestones + last "
            f"{DEFAULT_PRIOR_WINDOW} regular lessons; use --prior-full for all)"
        ),
    )
    parser.add_argument(
        "--prior-full",
        action="store_true",
        help="With --include-prior: return every lesson before the target day",
    )
    parser.add_argument(
        "--prior-milestones-only",
        action="store_true",
        help="With --include-prior: return only prior milestones",
    )
    parser.add_argument(
        "--prior-window",
        type=int,
        metavar="N",
        default=DEFAULT_PRIOR_WINDOW,
        help=(
            f"With --include-prior (smart mode): include last N regular lessons "
            f"(default {DEFAULT_PRIOR_WINDOW})"
        ),
    )
    parser.add_argument("--list", action="store_true",
                        help="List all lessons (week, day, skill)")
    parser.add_argument(
        "--search",
        help="Search keyword; returns index rows only (then run --week/--day)",
    )
    parser.add_argument(
        "--search-full",
        action="store_true",
        help="With --search: return full lesson payloads (legacy, token-heavy)",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON with indentation (default: compact)",
    )
    parser.add_argument(
        "--include-raw",
        action="store_true",
        help="Include skill_raw on the current lesson",
    )
    args = parser.parse_args()

    if args.prior_window < 0:
        parser.error("--prior-window must be >= 0")

    lessons = load_syllabus(args.csv)
    pretty = args.pretty

    if args.list:
        index = [_lesson_ref(l) for l in lessons]
        _dump(index, pretty=pretty)
        return

    if args.search:
        kw = args.search.lower()
        matches = []
        for lesson in lessons:
            if kw in _search_haystack(lesson):
                if args.search_full:
                    matches.append(format_lesson(lesson))
                else:
                    matches.append(_lesson_ref(lesson))
        _dump(
            {
                "query": args.search,
                "count": len(matches),
                "matches": matches,
                "next": (
                    "Run --week and --day on a match for full lesson context."
                    if matches and not args.search_full
                    else None
                ),
            },
            pretty=pretty,
        )
        return

    if not args.week or not args.day:
        parser.error("Provide --week and --day (or --list / --search).")

    idx = _lesson_index(lessons, args.week, args.day)
    if idx is None:
        _dump(
            {"error": f"No lesson found for week={args.week} day={args.day}"},
            pretty=pretty,
        )
        sys.exit(1)

    result = {
        "current": format_lesson(lessons[idx], include_raw=args.include_raw),
    }

    if args.include_prior and idx > 0:
        if args.prior_full:
            mode = "full"
        elif args.prior_milestones_only:
            mode = "milestones"
        else:
            mode = "smart"
        prior, meta = build_prior_skills(
            lessons,
            idx,
            mode=mode,
            window=args.prior_window,
        )
        result["prior_skills"] = prior
        result["prior_skills_meta"] = meta

    _dump(result, pretty=pretty)


if __name__ == "__main__":
    main()
