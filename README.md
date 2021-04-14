mmic_pdb
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/mmic_pdb/workflows/CI/badge.svg)](https://github.com/MolSSI/mmic_pdb/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/MolSSI/mmic_pdb/branch/main/graph/badge.svg)](https://codecov.io/gh/MolSSI/mmic_pdb/branch/main)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MolSSI/mmic_pdb.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/mmic_mda/context:python)

MMIC for extracting and fixing PDB files converted to MMSchema molecules. Based on Peter Eastman's [PDBFixer](https://github.com/openmm/pdbfixer).


## Example

from mmic_pdb.component import PdbFixerComponent

inp = {
    "pdbid": pdbid,
    "add_atoms": "all", # add all missing atoms
    "keep_hetero": "none", # remove all hetero atoms
    "std_residues": True, # convert non-std residues to the PDB std
}

# Execute component
outp = PdbFixerComponent.compute(inp)

# Extract log info and MMSchema molecule
log, mol = outp.log, outp.molecule

### Copyright

Copyright (c) 2021, MolSSI


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.5.
