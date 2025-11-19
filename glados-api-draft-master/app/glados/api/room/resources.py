from flask_restful import Resource
from glados.api.room.serializers import RoomSerializer
from glados.repositories.rooms import get_rooms, get_room_by_id


class RoomsAPI(Resource):
    def get(self):
        rooms = get_rooms()
        return RoomSerializer(many=True).dump(rooms), 200


class RoomAPI(Resource):
    def get(self, room_id):
        room = get_room_by_id(room_id)

        if not room:
            return {"error": "room_not_found"}, 404

        return RoomSerializer().dump(room), 200
