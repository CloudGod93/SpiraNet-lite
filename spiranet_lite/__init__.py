"""
Thin wrapper around the SpiraNetLite binary extension for MidWest Machine projects.

Usage:
    from spiranet_lite import SpiraNetLite
"""

import sys

# Ensure SpiraLibsPars is importable as a top-level module, because the
# compiled SpiraLibs extension does `import SpiraLibsPars` (no package prefix).
from . import SpiraLibsPars as _SpiraLibsPars  # type: ignore
sys.modules.setdefault("SpiraLibsPars", _SpiraLibsPars)

# Now it is safe to import the extension; its internal `import SpiraLibsPars`
# will resolve against sys.modules["SpiraLibsPars"].
from .SpiraLibs import SpiraNetLite  # type: ignore

__all__ = ["SpiraNetLite"]
