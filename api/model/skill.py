from flask_restplus import Model, fields

from .skill_type import SkillTypeModelSimple as SkillTypeModel

SkillModelFull = Model('Skill', {
    'id': fields.Integer(required=True, description='Skill id'),
    'level': fields.Integer(required=True, description='Skill level'),
    'type': fields.Nested(SkillTypeModel, required=True, description='Skill type'),
})
