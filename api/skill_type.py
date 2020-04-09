from flask_restplus import Namespace, Resource

from db import SkillTypeDao
from .model import SkillTypeModelSimple as SkillTypeModel

api = Namespace('skill_type')
api.add_model('SkillType', SkillTypeModel)


@api.route('')
class SkillTypeList(Resource):
    @api.doc('list all')
    @api.marshal_list_with(SkillTypeModel)
    def get(self):
        return SkillTypeDao.read_all()
