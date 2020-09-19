from flask_restplus import Model, fields

from .person import PersonModel

BuildingRoomModel = Model('BuildingRoom', {
    'id': fields.Integer(required=True),
    'type': fields.String(required=False),
    'production_type': fields.String(required=False),
    'workers': fields.List(fields.Nested(PersonModel), required=False),
})
