from glados.models import Entity
from glados import db


def get_entities(filters):
    query = Entity.query

    type = filters.get("type")
    if type:
        query = query.filter(Entity.type == type)

    room = filters.get("room")
    if room:
        query = query.filter(Entity.room_id == room)

    status = filters.get("status")
    if status:
        query = query.filter(Entity.status == status)

    return query

def update_entity(entity, data):
    for key, value in data.items():
        setattr(entity, key, value)
    db.session.commit()
    return entity
