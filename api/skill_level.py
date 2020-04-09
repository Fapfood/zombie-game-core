from flask_restplus import Namespace, Resource

from db import SkillLevelDao
from .model import SkillLevelModelFull as SkillLevelModel

api = Namespace('skill_level')
api.add_model('SkillLevel', SkillLevelModel)


@api.route('')
class SkillLevelList(Resource):
    @api.doc('list all')
    @api.marshal_list_with(SkillLevelModel)
    def get(self):
        return SkillLevelDao.read_all()
