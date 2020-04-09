from flask_restplus import Model, fields

from .skill_type import SkillTypeModelSimple as SkillTypeModel

SkillLevelModelSimple = Model('SkillLevel', {
    'id': fields.Integer(required=True, description='Skill level id'),
    'level': fields.Integer(required=True, description='Skill level'),
})

SkillLevelModelFull = Model('SkillLevel', {
    'id': fields.Integer(required=True, description='Skill level id'),
    'level': fields.Integer(required=True, description='Skill level'),
    'type': fields.Nested(SkillTypeModel, required=True, description='Skill type'),
})

SkillLevelModelCompact = Model('SkillLevel', {
    'id': fields.Integer(required=True, description='Skill level id'),
    'level': fields.Integer(required=True, description='Skill level'),
    'type.name': fields.String(required=True, description='Skill type name'),
})
