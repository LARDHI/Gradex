"""Tests for the ``--file`` entry point and the ``python -m`` module."""

import subprocess
import sys
from pathlib import Path

import pytest

from gpa_tracker import __main__ as main_module
from gpa_tracker.grading import preset_table
from gpa_tracker.models import Student
from gpa_tracker.storage import save_student


def test_main_uses_the_file_argument(tmp_path, monkeypatch):
    custom_path = tmp_path / "custom.json"
    calls = []
    monkeypatch.setattr(
        main_module.cli, "run", lambda path: calls.append(path) or 7
    )
    monkeypatch.setattr(
        sys, "argv", ["gpa_tracker", "--file", str(custom_path)]
    )

    assert main_module.main() == 7
    assert calls == [str(custom_path)]


def test_main_defaults_to_the_default_data_path(monkeypatch):
    calls = []
    default_path = Path("default-student.json")
    monkeypatch.setattr(
        main_module.cli, "run", lambda path: calls.append(path) or 0
    )
    monkeypatch.setattr(main_module, "default_data_path", lambda: default_path)
    monkeypatch.setattr(sys, "argv", ["gpa_tracker"])

    assert main_module.main() == 0
    assert calls == [default_path]


def test_module_entry_point_uses_the_file_argument(tmp_path):
    path = tmp_path / "module.json"
    save_student(Student("Test Student", preset_table("4.0-plus-only")), path)
    original = path.read_bytes()

    result = subprocess.run(
        [sys.executable, "-m", "gpa_tracker", "--file", str(path)],
        input="0\n",
        capture_output=True,
        text=True,
        timeout=60,
    )

    assert result.returncode == 0, result.stderr
    assert "Main menu:" in result.stdout
    assert path.read_bytes() == original
