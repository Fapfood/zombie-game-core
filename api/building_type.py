from flask_restplus import Namespace, Resource

from db import BuildingTypeDao
from .model import BuildingTypeModelSimple as BuildingTypeModel

api = Namespace('building_type')
api.add_model('BuildingType', BuildingTypeModel)


@api.route('')
class BuildingTypeList(Resource):
    @api.doc('list all')
    @api.marshal_list_with(BuildingTypeModel)
    def get(self):
        return BuildingTypeDao.read_all()
