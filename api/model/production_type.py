from flask_restplus import Model, fields

from .resource_pack import ResourcePackModelFull as ResourcePackModel
from .skill_pack import SkillPackModelFull as SkillPackModel

ProductionTypeModel = Model('ProductionType', {
    'id': fields.Integer(required=True, description='Production type id'),
    'name': fields.String(required=True, description='Production type name'),
    'minutes': fields.Integer(required=True, description='Production time in minutes'),
    'required_skills': fields.List(required=False, cls_or_instance=fields.Nested(SkillPackModel),
                                   description='Skill packs'),
    'required_tools': fields.List(required=False, cls_or_instance=fields.Nested(ResourcePackModel),
                                  description='Tools packs'),
    'from_resources': fields.List(required=False, cls_or_instance=fields.Nested(ResourcePackModel),
                                  description='Left resource packs'),
    'to_resources_successful': fields.List(required=False, cls_or_instance=fields.Nested(ResourcePackModel),
                                           description='Right resource packs after success'),
    'to_resources_interrupted': fields.List(required=False, cls_or_instance=fields.Nested(ResourcePackModel),
                                            description='Right resource packs after failure')
})
