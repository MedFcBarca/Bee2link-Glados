from glados import ma
from glados.models import Room, Entity
from marshmallow import fields


class EntitySimpleSerializer(ma.Schema):
    class Meta:
        model = Entity
        fields = ["id", "name", "type", "status", "value"]


class RoomSerializer(ma.Schema):
    entities = fields.Nested(EntitySimpleSerializer, many=True)

    class Meta:
        model = Room
        fields = ["id", "name", "created_at", "entities"]
        ordered = True
