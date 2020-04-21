from flask_restplus import Model, fields

from .skill_type import SkillTypeModelSimple as SkillTypeModel

ResourcePackModelSimple = Model('ResourcePack', {
    'id': fields.Integer(required=True, description='Resource pack id'),
    'name': fields.String(required=True, description='Resource pack name'),
    'quantity': fields.Integer(required=True, description='Resource quantity'),
})

ResourcePackModelFull = Model('ResourcePack', {
    'id': fields.Integer(required=True, description='Resource pack id'),
    'name': fields.String(required=True, description='Resource pack name'),
    'quantity': fields.Integer(required=True, description='Resource quantity'),
    'type': fields.Nested(SkillTypeModel, required=True, description='Resource type'),
})

ResourcePackModelCompact = Model('ResourcePack', {
    'id': fields.Integer(required=True, description='Resource pack id'),
    'name': fields.String(required=True, description='Resource pack name'),
    'quantity': fields.Integer(required=True, description='Resource quantity'),
    'type.name': fields.String(required=True, description='Resource type name'),
})
