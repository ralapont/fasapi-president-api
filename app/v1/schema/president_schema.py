from pydantic import BaseModel
from pydantic import Field
from datetime import date
from typing import Optional

class PresidentBase(BaseModel):
    last_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="kktua"
    )
    first_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="kkatua"
    )
    suffix: Optional[str] = Field(
        ...,
        example="Mr."
    )
    city: str = Field(
        ...,
        example="Los Angeles"
    )
    state: str = Field(
        ...,
        min_length=2,
        max_length=2,
        example="CA"
    )
    birth: date = Field(
        ...,
        example="2032-04-23"
    )
    death: Optional[date] = Field(
        ...,
        example="2032-04-23"
    )

class PresidentPicture(PresidentBase):
    icon: Optional[str] = Field(
        ...,
        example="georgewashington"
    )
    photo: Optional[str] = Field(
        ...,
        example="gw1"
    )

class President(PresidentPicture):
    id: int = Field(
        ...,
        example=1
    )
        


