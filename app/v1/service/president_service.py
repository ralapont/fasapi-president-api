from fastapi import HTTPException, status

from app.v1.model.president_model import President as PresidentModel
from app.v1.schema import president_schema, mensaje_schema

def create_president(president: president_schema.PresidentBase):
    get_president = PresidentModel.filter((PresidentModel.last_name == president.last_name) & (PresidentModel.first_name == president.first_name))
    if get_president:
        msg = "President ya registrado"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    
    db_president = PresidentModel(
        last_name = president.last_name,
        first_name = president.first_name,
        suffix = president.suffix,
        city = president.city,
        state = president.state,
        birth = president.birth,
        death = president.death
    )

    db_president.save()

    return president_schema.President(
        id = db_president.id,
        last_name = db_president.last_name,
        first_name = db_president.first_name,
        suffix=db_president.suffix,
        city= db_president.city,
        state= db_president.state,
        birth= db_president.birth,
        death= db_president.death

    )

def get_presidents():
    db_presidents = PresidentModel.filter()
    list_presidents = []
    for db_president in db_presidents:
        list_presidents.append(
            president_schema.President(
                id = db_president.id,
                last_name = db_president.last_name,
                first_name = db_president.first_name,
                suffix=db_president.suffix,
                city= db_president.city,
                state= db_president.state,
                birth= db_president.birth,
                death= db_president.death
        )
    )
    return list_presidents

def get_president(president_id: int):
    db_president = PresidentModel.get_by_id(president_id)
    if not db_president:
        msg = "President no registrado"
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg
        )
    
    return president_schema.President(
        id = db_president.id,
        last_name = db_president.last_name,
        first_name = db_president.first_name,
        suffix=db_president.suffix,
        city= db_president.city,
        state= db_president.state,
        birth= db_president.birth,
        death= db_president.death
    )

def update_president(president_id: int, president: president_schema.PresidentBase):
    db_president = PresidentModel.get_by_id(president_id)
    if not db_president:
        msg = "President no registrado"
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg
        )

    db_president.last_name = president.last_name
    db_president.first_name = president.first_name
    db_president.suffix = president.suffix
    db_president.city = president.city
    db_president.state = president.state
    db_president.birth = president.birth
    db_president.death = president.death

    db_president.save()

    return president_schema.President(
        id = db_president.id,
        last_name = db_president.last_name,
        first_name = db_president.first_name,
        suffix=db_president.suffix,
        city= db_president.city,
        state= db_president.state,
        birth= db_president.birth,
        death= db_president.death
    )

def delete_president(president_id: int):
    db_president = PresidentModel.get_by_id(president_id)
    if not db_president:
        msg = "President no registrado"
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg
        )
    
    db_president.delete_instance()
