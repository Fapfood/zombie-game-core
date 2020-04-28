from flask_restplus import Model, fields

from .skill_type import SkillTypeModelSimple as SkillTypeModel

ResourcePackModelSimple = Model('ResourcePack', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'quantity': fields.Integer(required=True),
})

ResourcePackModelFull = Model('ResourcePack', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'quantity': fields.Integer(required=True),
    'type': fields.Nested(SkillTypeModel, required=True),
})

ResourcePackModelCompact = Model('ResourcePack', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'quantity': fields.Integer(required=True),
    'type.name': fields.String(required=True),
})
