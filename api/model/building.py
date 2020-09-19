from flask_restplus import Model, fields

from .building_room import BuildingRoomModel

BuildingModel = Model('Building', {
    'id': fields.Integer(required=True),
    'rooms': fields.List(fields.Nested(BuildingRoomModel), required=True),
})
