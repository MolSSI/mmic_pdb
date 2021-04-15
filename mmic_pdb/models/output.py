from mmelemental.models import ProcOutput, Molecule
from .input import PdbFixerInput
from pydantic import Field
from typing import Dict, Tuple, List, Optional, Any

__all__ = ["PdbFixerOutput"]


class PdbFixerOutput(ProcOutput):
    proc_input: PdbFixerInput = Field(
        ..., description="Input schema used to run pdbfixer."
    )
    molecule: Molecule = Field(
        ...,
        description="Molecular mechanics molecule object. See the :class:``Molecule`` class. ",
    )
    miss_resids: Optional[Dict[Tuple[int, int], List[str]]] = Field(
        None,
        description="Missing residues in the SEQRES records for which no atom data is present. "
        "Each key is a tuple consisting of the index of a chain, and the residue index within "
        "that chain at which new residues should be inserted. The corresponding value is a list "
        "of the names of residues to insert there.",
    )
    nonstd_resids: Optional[List[Tuple[Any, str]]] = Field(
        None,
        description="",
    )
