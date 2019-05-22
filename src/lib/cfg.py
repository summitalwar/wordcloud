# =============================================================================
# --- Confirguration file
# =============================================================================

import sys
import os
import re

__version__ = "0.1.0"
__doc__ = "Word cloud"
module = "src"

# Set module path
path = os.path.abspath(os.path.dirname(sys.argv[0]))
path = re.sub(r"(.+)(\\" + module + ".*)", r"\1", path)
path = path + "\\"
