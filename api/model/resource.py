from flask_restplus import Model, fields

from .skill_type import SkillTypeModelSimple as SkillTypeModel

ResourceModelFull = Model('Resource', {
    'id': fields.Integer(required=True, description='Resource id'),
    'available': fields.Boolean(required=True, description='Is available'),
    'owned': fields.Boolean(required=True, description='Is owned'),
    'quality': fields.Integer(required=True, description='Resource quality'),
    'decay': fields.Integer(required=True, description='Resource decay'),
    'type': fields.Nested(SkillTypeModel, required=True, description='Resource type'),
})
