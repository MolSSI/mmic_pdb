from mmelemental.models import ProcOutput, Molecule
from .input import PdbFixerInput
from pydantic import Field

__all__ = ["PdbFixerOutput"]


class PdbFixerOutput(ProcOutput):
    proc_input: PdbFixerInput = Field(
        ..., description="Input schema used to run pdbfixer."
    )
    molecule: Molecule = Field(
        ...,
        description="Molecular mechanics molecule object. See the :class:``Molecule`` class. ",
    )
