# These imports look a bit messy. The "isort" package can fix this.
# isort will split your imports into:
# 1 - Python native packages
# 2 - Third-party packages
# 3 - Local packages

# Within these splits, imports will be split in full imports and partial imports (using the "from" keyword)
# Finally, within these splits, imports will be sorted alphabetically

# This code can be fixed by either:
# - "isort files demos/demo_isort.py"
# - "pre-commit run --files demos/demos_isort.py"
# - "pre-commit install", followed by "git add demos/demos_isort.py" and "git commit"

import re
import pandas as pd
from os import path, open, access
from demo_black import f, a, d
import sys
import json