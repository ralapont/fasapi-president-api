from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from typing import List, Optional
from fastapi import Path

from app.v1.schema import president_schema
from app.v1.service import president_service

from app.v1.utils.db import get_db

router = APIRouter(prefix="/api/v1")

@router.post(
    "/president/",
    tags=["presidentes"],
    status_code=status.HTTP_201_CREATED,
    response_model=president_schema.President,
    dependencies=[Depends(get_db)],
    summary="Create a new president"
)
def create_president(president: president_schema.PresidentPicture = Body(...)):
    """
    ## Create a new president in the app

    ### Args
    The app can recive next fields into a JSON
    - email: A valid email
    - username: Unique username
    - password: Strong password for authentication

    ### Returns
    - president: president info
    """
    print("presidente " + president.last_name + " " + president.first_name + " " + president.photo)
    return president_service.create_president(president)

@router.get(
    "/president/",
    tags=["presidentes"],
    status_code=status.HTTP_200_OK,
    response_model=List[president_schema.President],
    dependencies=[Depends(get_db)],
    summary="Obtiene lista de presidents"
)
def get_presidents():
    return president_service.get_presidents()

@router.get(
    "/president/{president_id}",
    tags=["presidentes"],
    status_code=status.HTTP_200_OK,
    response_model=president_schema.President,
    dependencies=[Depends(get_db)],
    summary="Get a president"
)
def get_president(president_id: int = Path(
        ...,
        gt=0
    )
):
    return president_service.get_president(president_id)    

@router.put(
    "/president/{president_id}",
    tags=["presidentes"],
    status_code=status.HTTP_200_OK,
    response_model=president_schema.President,
    dependencies=[Depends(get_db)],
    summary="Actualiza un president"
)
def update_president(president_id: int = Path(
        ...,
        gt=0
    ), president: president_schema.PresidentPicture = Body(...)
):
    return president_service.update_president(president_id, president)

@router.delete(
    "/president/{president_id}",
    tags=["presidentes"],
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(get_db)],
    summary="Elimina un president"
)
def get_president(president_id: int = Path(
        ...,
        gt=0
    )
):
    president_service.delete_president(president_id)    
