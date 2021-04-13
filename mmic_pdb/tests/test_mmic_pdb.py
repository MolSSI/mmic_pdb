"""
Unit and regression test for the mmic_pdb package.
"""

# Import package, test suite, and other packages as needed
import mmic_pdb
import pytest
import sys

def test_mmic_pdb_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_pdb" in sys.modules
