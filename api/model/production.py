from flask_restplus import Model, fields

from .resource_pack import ResourcePackModelFull as ResourcePackModel
from .skill_level import SkillLevelModelFull as SkillLevelModel

ProductionModel = Model('Production', {
    'id': fields.Integer(required=True, description='Production id'),
    'minutes': fields.Integer(required=True, description='Production time in minutes'),
    'required_skills': fields.List(required=False, cls_or_instance=fields.Nested(SkillLevelModel),
                                   description='Skill levels'),
    'from_resources': fields.List(required=False, cls_or_instance=fields.Nested(ResourcePackModel),
                                  description='Left resource packs'),
    'to_resources_successful': fields.List(required=False, cls_or_instance=fields.Nested(ResourcePackModel),
                                           description='Right resource packs after success'),
    'to_resources_interrupted': fields.List(required=False, cls_or_instance=fields.Nested(ResourcePackModel),
                                            description='Right resource packs after failure')
})
