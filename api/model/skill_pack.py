from flask_restplus import Model, fields

from .skill_level import SkillLevelModelFull as SkillLevelModel

SkillPackModelSimple = Model('SkillPack', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
})

SkillPackModelFull = Model('SkillPack', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'skills': fields.Nested(SkillLevelModel, required=True),
})
