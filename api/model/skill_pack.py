from flask_restplus import Model, fields

from .skill_level import SkillLevelModelFull as SkillLevelModel

SkillPackModelSimple = Model('SkillPack', {
    'id': fields.Integer(required=True, description='Skill pack id'),
    'name': fields.String(required=True, description='Skill pack name'),
})

SkillPackModelFull = Model('SkillPack', {
    'id': fields.Integer(required=True, description='Skill pack id'),
    'name': fields.String(required=True, description='Skill pack name'),
    'skills': fields.Nested(SkillLevelModel, required=True, description='Skills'),
})
