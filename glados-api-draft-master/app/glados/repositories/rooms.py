from glados.models import Room
from glados import db


def get_rooms():
    return Room.query.all()


def get_room_by_id(room_id):
    return Room.query.get(room_id)
