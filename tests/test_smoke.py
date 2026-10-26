
"""Smoke tests for the GPA Tracker package."""

import gpa_tracker


def test_package_imports_with_expected_version() -> None:
    """Verify that the package imports and exposes its version."""
    assert gpa_tracker.__version__ == "0.1.0"
