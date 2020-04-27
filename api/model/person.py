from flask_restplus import Model, fields

from .skill import SkillModelFull as SkillModel

PersonModel = Model('Person', {
    'id': fields.Integer(required=True, description='Person id'),
    'first_name': fields.String(required=True, description='Person first name'),
    'last_name': fields.String(required=True, description='Person last name'),
    'gender': fields.String(required=True, description='Person gender'),
    'age': fields.Integer(required=True, description='Person age'),
    'base_icon': fields.String(required=True, description='Person icon'),
    'temp_icon': fields.String(required=False, description='Person icon'),
    'attitude': fields.Integer(required=True, description='Person attitude'),
    'skills': fields.List(required=False, cls_or_instance=fields.Nested(SkillModel), description='Personal skills'),
})
