from flask_restplus import Model, fields

from .skill_type import SkillTypeModelSimple as SkillTypeModel

ResourceModelFull = Model('Resource', {
    'id': fields.Integer(required=True),
    'available': fields.Boolean(required=True),
    'owned': fields.Boolean(required=True),
    'quality': fields.Integer(required=True),
    'decay': fields.Integer(required=True),
    'type': fields.Nested(SkillTypeModel, required=True),
})
