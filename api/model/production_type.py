from flask_restplus import Model, fields

from .resource_pack import ResourcePackModelFull as ResourcePackModel
from .skill_pack import SkillPackModelFull as SkillPackModel

ProductionTypeModel = Model('ProductionType', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'minutes': fields.Integer(required=True),
    'required_skills': fields.List(fields.Nested(SkillPackModel), required=False),
    'required_tools': fields.List(fields.Nested(ResourcePackModel), required=False),
    'from_resources': fields.List(fields.Nested(ResourcePackModel), required=False),
    'to_resources_successful': fields.List(fields.Nested(ResourcePackModel), required=False),
    'to_resources_interrupted': fields.List(fields.Nested(ResourcePackModel), required=False),
})
