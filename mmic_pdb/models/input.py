from mmelemental.models import ProcInput, Molecule
from pydantic import Field, validator, root_validator

__all__ = ["PdbFixerInput"]


class PdbFixerInput(ProcInput):
    """Basic input model for pdbfixer."""

    molecule: Molecule = Field(None, description="MMSchema molecule input object.")
    pdbid: str = Field(None, description="PDB id to retrieve from RCSB.")
    url: str = Field(None, description="URL to retrieve PDB from.")
    keep_hetero: str = Field(
        "all",
        description="Which heterogens to remove: all, water, or none.",
    )
    std_residues: bool = Field(
        True,
        description="Replace nonstandard residues with standard equivalents.",
    )
    miss_residues: bool = Field(
        False, dest="residues", description="Add missing residues"
    )
    add_atoms: str = Field(
        "all",
        description="Which missing atoms to add: all, heavy, hydrogen, or none.",
    )

    # Validators
    @validator("url")
    def _valid_url(cls, v):
        return v

    @validator("add_atoms")
    def _valid_add_atoms(cls, v):
        if v not in ("all", "heavy", "hydrogen", "none"):
            raise ValueError(
                "add_atoms can be one of the following: all, heavy, hydrogen, or none."
            )
        return v

    @validator("keep_hetero")
    def _valid_keep_heterogens(cls, v):
        if v not in ("all", "water", "none"):
            raise ValueError(
                "add_atoms can be one of the following: all, water, or none."
            )
        return v

    @root_validator
    def _valid_input(cls, values):
        if (
            not values.get("pdbid")
            and not values.get("url")
            and not values.get("molecule")
        ):
            raise ValueError(
                "Only one of the following must be assigned: pdbid, url, or molecule."
            )
        if (
            (values.get("pdbid") and values.get("url"))
            or (values.get("pdbid") and values.get("molecule"))
            or (values.get("url") and values.get("url"))
        ):
            raise ValueError(
                "Only one of the following must be assigned: pdbid, url, or molecule."
            )
        return values
