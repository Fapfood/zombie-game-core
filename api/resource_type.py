from flask_restplus import Namespace, Resource

from db import ResourceTypeDao
from .model import ResourceTypeModelSimple as ResourceTypeModel

api = Namespace('resource_type')
api.add_model('ResourceType', ResourceTypeModel)


@api.route('')
class ResourceTypeList(Resource):
    @api.doc('list all')
    @api.marshal_list_with(ResourceTypeModel)
    def get(self):
        return ResourceTypeDao.read_all()
