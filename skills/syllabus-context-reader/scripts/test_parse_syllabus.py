#!/usr/bin/env python3
"""Tests for parse_syllabus.py — run: python3 -m unittest test_parse_syllabus.py"""

import json
import subprocess
import unittest
from pathlib import Path

from parse_syllabus import (
    build_prior_skills,
    load_syllabus,
    _lesson_index,
)

SCRIPT_DIR = Path(__file__).resolve().parent
CSV = SCRIPT_DIR / \
    "../../../ai-engineering/New Syllabus AI Engineer - Planificación del programa.csv"
PY = SCRIPT_DIR / "parse_syllabus.py"


def run_cli(*args: str) -> dict | list:
    out = subprocess.check_output(
        ["python3", str(PY), "--csv", str(CSV.resolve()), *args],
        text=True,
    )
    return json.loads(out)


@unittest.skipUnless(CSV.resolve().is_file(), "syllabus CSV not found")
class TestParseSyllabusCLI(unittest.TestCase):
    def test_list_returns_lessons(self):
        index = run_cli("--list")
        self.assertIsInstance(index, list)
        self.assertGreater(len(index), 50)
        self.assertIn("week", index[0])
        self.assertIn("skill", index[0])

    def test_extract_week_day(self):
        result = run_cli("--week", "1", "--day", "2")
        current = result["current"]
        self.assertEqual(current["week"], "1")
        self.assertEqual(current["day"], "2")
        self.assertTrue(current.get("content"))
        self.assertNotIn("skill_raw", current)

    def test_include_prior_smart_meta(self):
        result = run_cli("--week", "8", "--day", "22", "--include-prior")
        meta = result["prior_skills_meta"]
        self.assertEqual(meta["mode"], "smart")
        self.assertEqual(meta["total_prior"], 29)
        self.assertLess(meta["returned"], meta["total_prior"])
        self.assertEqual(meta["returned"], len(result["prior_skills"]))

    def test_prior_full_returns_all(self):
        result = run_cli(
            "--week", "8", "--day", "22", "--include-prior", "--prior-full"
        )
        meta = result["prior_skills_meta"]
        self.assertEqual(meta["mode"], "full")
        self.assertEqual(meta["returned"], meta["total_prior"])

    def test_search_lightweight(self):
        result = run_cli("--search", "tailwind")
        self.assertGreater(result["count"], 0)
        self.assertEqual(result["count"], len(result["matches"]))
        self.assertNotIn("content", result["matches"][0])

    def test_missing_lesson_exits_nonzero(self):
        proc = subprocess.run(
            ["python3", str(PY), "--csv", str(CSV.resolve()),
             "--week", "99", "--day", "1"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 1)
        payload = json.loads(proc.stdout)
        self.assertIn("error", payload)

    def test_hito_lookup(self):
        result = run_cli("--week", "HITO 01", "--day", "En Syllabus")
        self.assertTrue(result["current"]["is_milestone"])
        self.assertIn("HITO 01", result["current"]["skill"])


@unittest.skipUnless(CSV.resolve().is_file(), "syllabus CSV not found")
class TestBuildPriorSkills(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lessons = load_syllabus(str(CSV.resolve()))

    def test_smart_prior_is_chronological(self):
        idx = _lesson_index(self.lessons, "8", "22")
        prior, _ = build_prior_skills(
            self.lessons, idx, mode="smart", window=15)
        positions = []
        for p in prior:
            for i, lesson in enumerate(self.lessons[:idx]):
                if lesson["week"] == p["week"] and lesson["day"] == p["day"]:
                    positions.append(i)
                    break
        self.assertEqual(positions, sorted(positions))

    def test_milestones_only(self):
        idx = _lesson_index(self.lessons, "8", "22")
        prior, meta = build_prior_skills(self.lessons, idx, mode="milestones")
        self.assertTrue(all(p["is_milestone"] for p in prior))
        self.assertEqual(meta["mode"], "milestones")


if __name__ == "__main__":
    unittest.main()
