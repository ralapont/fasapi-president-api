from fastapi import HTTPException, status

from app.v1.model.president_model import President as PresidentModel
from app.v1.model.picture_model import Picture as PictureModel
from app.v1.schema import president_schema

def create_president(president: president_schema.PresidentPicture):
    
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

    db_picture = PictureModel(
        pict_id = db_president.id,
        pict_icon = president.icon,
        pict_data = president.photo
    )

    pictureNew = db_picture.create(pict_id=db_president.id, pict_icon=president.icon, pict_data=president.photo)

    return president_schema.President(
        id = db_president.id,
        last_name = db_president.last_name,
        first_name = db_president.first_name,
        suffix=db_president.suffix,
        city= db_president.city,
        state= db_president.state,
        birth= db_president.birth,
        death= db_president.death,
        icon = pictureNew.pict_icon,
        photo = pictureNew.pict_data

    )

def get_presidents():
    db_presidents = PresidentModel.filter()
    list_presidents = []

    for db_president in db_presidents:
            
        db_picture = PictureModel.get_by_id(db_president.id)

        list_presidents.append(
            president_schema.President(
                id = db_president.id,
                last_name = db_president.last_name,
                first_name = db_president.first_name,
                suffix=db_president.suffix,
                city= db_president.city,
                state= db_president.state,
                birth= db_president.birth,
                death= db_president.death,
                icon=db_picture.pict_icon,
                photo=db_picture.pict_data
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

    db_picture = PictureModel.get_by_id(db_president.id)

    return president_schema.President(
        id = db_president.id,
        last_name = db_president.last_name,
        first_name = db_president.first_name,
        suffix=db_president.suffix,
        city= db_president.city,
        state= db_president.state,
        birth= db_president.birth,
        death= db_president.death,
        icon=db_picture.pict_icon,
        photo=db_picture.pict_data
    )

def update_president(president_id: int, president: president_schema.PresidentPicture):
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

    db_picture = PictureModel(
        pict_id = db_president.id,
        pict_icon = president.icon,
        pict_data = president.photo
    )

    db_picture.save()

    return president_schema.President(
        id = db_president.id,
        last_name = db_president.last_name,
        first_name = db_president.first_name,
        suffix=db_president.suffix,
        city= db_president.city,
        state= db_president.state,
        birth= db_president.birth,
        death= db_president.death,
        icon = db_picture.pict_icon,
        photo = db_picture.pict_data
    )

def delete_president(president_id: int):

    db_president = PresidentModel.get_by_id(president_id)
    if not db_president:
        msg = "President no registrado"
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg
        )

    db_picture = PictureModel.get_by_id(president_id)
    db_picture.delete_instance()

    db_president.delete_instance()
