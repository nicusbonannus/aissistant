from pydantic import BaseModel


class InjuryCreationData(BaseModel):
    body_part_name: str
    illness_name: str
    has_been_cured: bool = False


class InjuryResponse(InjuryCreationData):
    id: int

    class Config:
        from_attributes = True
