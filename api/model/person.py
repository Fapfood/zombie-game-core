from flask_restplus import Model, fields

from .skill import SkillModel

PersonModel = Model('Person', {
    'id': fields.Integer(required=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'gender': fields.String(required=True),
    'age': fields.Integer(required=True),
    'base_icon': fields.String(required=True),
    'temp_icon': fields.String(required=False),
    'attitude': fields.Integer(required=True),
    'skills': fields.List(fields.Nested(SkillModel), required=False),
})
