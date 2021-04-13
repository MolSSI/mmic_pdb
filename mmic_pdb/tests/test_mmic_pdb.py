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


def test_mmic_pdbid():
    inp = mmic_pdb.models.PdbFixerInput(
        pdbid="4EZI",
        add_atoms="all",
        keep_hetero="water",
        std_residues=True,
    )
    return mmic_pdb.components.PdbFixerComponent.compute(inp)
