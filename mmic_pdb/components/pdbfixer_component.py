from ..models import PdbFixerInput, PdbFixerOutput
from mmelemental.models import Molecule
from mmelemental.util.files import random_file
from mmic.components.blueprints import SpecificComponent
import pdbfixer
import simtk.openmm.app as app
import os
from typing import Dict, List, Tuple, Any, Optional

__all__ = ["PdbFixerComponent"]


class PdbFixerComponent(SpecificComponent):
    @classmethod
    def input(cls):
        return PdbFixerInput

    @classmethod
    def output(cls):
        return PdbFixerOutput

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
        config: "TaskConfig" = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        if isinstance(inputs, self.input()):
            inputs = inputs.dict()

        log = []
        warnings = []

        if inputs.get("pdbid"):
            log.append(f"Retrieving PDB {inputs['pdbid']} from RCSB ...\n")
            fixer = pdbfixer.PDBFixer(pdbid=inputs["pdbid"])
        elif inputs.get("url"):
            log.append("Retrieving PDB from URL {options['url']} ...\n")
            fixer = pdbfixer.PDBFixer(url=inputs["url"])
        elif inputs.get("molecule"):
            filename = random_file(suffix=".pdb")
            inputs.molecule.to_file(filename)
            fixer = pdbfixer.PDBFixer(filename=filename)

        try:
            if inputs.get("miss_residues"):
                fixer.missingResidues = {}
            else:
                log.append("Finding missing residues...\n")
                fixer.findMissingResidues()

            # Standardize residues
            if inputs.get("std_residues"):
                log.append("Finding nonstandard residues...\n")
                fixer.findNonstandardResidues()
                log.append("Replacing nonstandard residues...\n")
                fixer.replaceNonstandardResidues()

            # Clean HETATOMS
            if inputs.get("keep_hetero") == "none":
                log.append("Removing all heterogens ...\n")
                fixer.removeHeterogens(keepWater=False)
            elif inputs.get("keep_hetero") == "water":
                log.append("Removing all heterogens except for water ...\n")
                fixer.removeHeterogens(keepWater=True)

            # Missing atoms
            log.append("Finding missing atoms...\n")
            fixer.findMissingAtoms()
            if (
                inputs.get("add_atoms") != "all"
                and inputs.get("add_atoms") != "hydrogen"
            ):
                fixer.missingAtoms = {}
                fixer.missingTerminals = {}
            log.append("Adding missing atoms...\n")
            fixer.addMissingAtoms()
            if (
                inputs.get("add_atoms") == "all"
                or inputs.get("add_atoms") == "hydrogen"
            ):
                log.append("Adding missing hydrogens...\n")
                fixer.addMissingHydrogens(pH=7)
        except (KeyError, RuntimeError) as e:
            log.append(
                f"PDBFixer returned the following exception: {type(e).__name__}: {e}\n"
            )
            warnings.append(
                "PDBFixer works only with a known sequence of natural amino acids. Proceeding with PDB file as is ..."
            )

        filename = random_file(suffix=".pdb")
        with open(filename, "w") as fp:
            log.append("Writing output...\n")
            if fixer.source is not None:
                fp.write("REMARK   1 PDBFIXER FROM: %s\n" % fixer.source)
            app.PDBFile.writeFile(fixer.topology, fixer.positions, fp, True)

        mol = Molecule.from_file(filename)
        os.remove(filename)

        return True, PdbFixerOutput(
            proc_input=inputs,
            log="".join(log),
            warnings="".join(warnings),
            miss_resids=fixer.missingResidues,
            nonstd_resids=fixer.nonstandardResidues,
            molecule=mol,
        )
