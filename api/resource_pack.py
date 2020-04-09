from flask_restplus import Namespace, Resource

from db import ResourcePackDao
from .model import ResourcePackModelFull as ResourcePackModel

api = Namespace('resource_pack')
api.add_model('ResourcePack', ResourcePackModel)


@api.route('')
class ResourcePackList(Resource):
    @api.doc('list all')
    @api.marshal_list_with(ResourcePackModel)
    def get(self):
        return ResourcePackDao.read_all()
