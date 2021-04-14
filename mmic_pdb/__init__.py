"""
mmic_pdb
MMIC for extracting and fixing PDB files converted to MMSchema molecules
"""

# Add imports here
from .models import *
from .components import *

# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
