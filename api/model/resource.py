from flask_restplus import Model, fields

from .skill_type import SkillTypeModelSimple as SkillTypeModel

ResourceModelFull = Model('Resource', {
    'id': fields.Integer(required=True, description='Resource id'),
    'quantity': fields.Integer(required=True, description='Resource quantity'),
    'quality': fields.Integer(required=True, description='Resource quality'),
    'decay': fields.Integer(required=True, description='Resource decay'),
    'type': fields.Nested(SkillTypeModel, required=True, description='Resource type'),
})
