from flask_restplus import Model, fields

from .skill_type import SkillTypeModelSimple as SkillTypeModel

SkillModelFull = Model('Skill', {
    'id': fields.Integer(required=True),
    'level': fields.Integer(required=True),
    'type': fields.Nested(SkillTypeModel, required=True),
})
