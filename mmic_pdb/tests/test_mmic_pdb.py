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


@pytest.mark.parametrize(
    "pdbid,add_atoms,keep_hetero",
    [("1dzl", "all", "water"), ("4ezi", "none", "none"), ("1lfg", "heavy", "all")],
)
def test_mmic_pdbid(pdbid, add_atoms, keep_hetero):
    inp = mmic_pdb.models.PdbFixerInput(
        pdbid=pdbid,
        add_atoms=add_atoms,
        keep_hetero=keep_hetero,
        std_residues=True,
    )
    return mmic_pdb.components.PdbFixerComponent.compute(inp)
