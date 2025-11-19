from flask import request
from flask_restful import Resource

from glados.api.entity.serializers import (
    EntitiesRequestSerializer,
    EntityResponseSerializer,
    EntityUpdateRequestSerializer
)

from glados.repositories.entities import get_entities, update_entity
from glados.models import Entity


class EntitiesAPI(Resource):
    def get(self):
        request_serializer = EntitiesRequestSerializer()
        data = request_serializer.load(request.args)

        entities = get_entities(data)

        serializer = EntityResponseSerializer(many=True)
        return serializer.dump(entities), 200


class EntityAPI(Resource):
    def put(self, entity_id):
        serializer = EntityUpdateRequestSerializer()
        data = serializer.load(request.json)

        entity = Entity.query.get(entity_id)
        if not entity:
            return {"error": "entity_not_found"}, 404

        updated = update_entity(entity, data)

        return EntityResponseSerializer().dump(updated), 200
