from flask_restplus import Model, fields

from .skill_type import SkillTypeModelSimple as SkillTypeModel

SkillLevelModelSimple = Model('SkillLevel', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'level': fields.Integer(required=True),
})

SkillLevelModelFull = Model('SkillLevel', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'level': fields.Integer(required=True),
    'type': fields.Nested(SkillTypeModel, required=True),
})

SkillLevelModelCompact = Model('SkillLevel', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'level': fields.Integer(required=True),
    'type.name': fields.String(required=True),
})
