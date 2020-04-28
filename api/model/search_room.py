from flask_restplus import Model, fields

# from .skill import SkillModelFull as SkillModel
from .resource import ResourceModelFull as ResourceModel

SearchRoomModel = Model('SearchRoom', {
    'id': fields.Integer(required=True),
    # 'type': fields.Nested(SearchRoomTypeModel, required=True, description='Skill type'),
    'resources': fields.List(fields.Nested(ResourceModel), required=False),
})
