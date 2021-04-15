mmic_pdb
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/mmic_pdb/workflows/CI/badge.svg)](https://github.com/MolSSI/mmic_pdb/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/MolSSI/mmic_pdb/branch/main/graph/badge.svg)](https://codecov.io/gh/MolSSI/mmic_pdb/branch/main)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MolSSI/mmic_pdb.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/mmic_pdb/context:python)
[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/MolSSI/mmic_pdb/3530cb20cd9fc6dc9ed3281ca36110453b070968?filepath=mmic_pdb.ipynb)

This is part of the [MolSSI](http://molssi.org) Molecular Mechanics Interoperable Components ([MMIC](https://github.com/MolSSI/mmic)) project. This package uses Peter Eastman's [PDBFixer](https://github.com/openmm/pdbfixer) to extract, fix, and/or convert PDB files to MMSchema molecules. 

![image](mmic_pdb/data/imgs/component.png)

### Code snippet

```python
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
```

### Copyright

Copyright (c) 2021, MolSSI


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.5.
