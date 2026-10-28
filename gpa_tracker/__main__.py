"""Command-line entry point for GPA Tracker."""

import argparse

from . import cli
from .storage import default_data_path


def main() -> int:
    """Parse command-line arguments and launch GPA Tracker."""
    parser = argparse.ArgumentParser(prog="gpa_tracker")
    parser.add_argument(
        "--file",
        metavar="PATH",
        help="use PATH instead of the default student data file",
    )
    args = parser.parse_args()

    path = args.file if args.file is not None else default_data_path()
    return cli.run(path)


if __name__ == "__main__":
    raise SystemExit(main())