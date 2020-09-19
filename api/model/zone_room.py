from flask_restplus import Model, fields

# from .skill import SkillModelFull
from .resource import ResourceModel

ZoneRoomModel = Model('ZoneRoom', {
    'id': fields.Integer(required=True),
    'type': fields.String(required=True),
    'resources': fields.List(fields.Nested(ResourceModel), required=False),
})
