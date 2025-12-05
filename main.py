#!/usr/bin/env python3
"""
Main entry point for Github Heroes.
"""

import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).parent.joinpath("src").as_posix())
from github_heroes.core.app import run_app

if __name__ == "__main__":
    # Call the Click command - it will parse sys.argv for options like --log
    # If no --log is provided, it will use the default "info" from the Click option
    sys.exit(run_app.main(standalone_mode=False))
