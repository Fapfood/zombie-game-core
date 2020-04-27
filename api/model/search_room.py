from flask_restplus import Model, fields

# from .skill import SkillModelFull as SkillModel
from .resource import ResourceModelFull as ResourceModel

SearchRoomModel = Model('SearchRoom', {
    'id': fields.Integer(required=True, description='Search zone id'),
    # 'type': fields.Nested(SearchRoomTypeModel, required=True, description='Skill type'),
    'resources': fields.List(required=False, cls_or_instance=fields.Nested(ResourceModel), description='Resources'),
})
