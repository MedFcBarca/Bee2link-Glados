from marshmallow import fields, validate

from glados import ma, constants
from glados.models import Entity


class EntitiesRequestSerializer(ma.Schema):
    type = fields.String(
        required=False,
        validate=validate.OneOf([x.name for x in constants.EntityType])
    )

    room = fields.UUID(required=False)

    status = fields.String(
        required=False,
        validate=validate.OneOf([x.name for x in constants.EntityStatus])
    )


class EntitySerializer(ma.Schema):
    created_at = fields.DateTime("%Y-%m-%dT%H:%M:%S")

    class Meta:
        model = Entity
        ordered = True
        fields = [
            "id",
            "name",
            "type",
            "status",
            "value",
            "created_at"
        ]


class EntityResponseSerializer(EntitySerializer):
    pass

class EntityUpdateRequestSerializer(ma.Schema):
    name = fields.String(required=False)
    status = fields.String(
        required=False,
        validate=validate.OneOf([x.name for x in constants.EntityStatus])
    )
    value = fields.String(required=False, allow_none=True)
    room_id = fields.UUID(required=False, allow_none=True)
