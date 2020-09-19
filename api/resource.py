from flask_restplus import Namespace, Resource

from db import ResourceDao
from .model import ResourceModel

api = Namespace('resource')
api.add_model('Resource', ResourceModel)


@api.route('')
class ResourceList(Resource):
    @api.doc('list all')
    @api.marshal_list_with(ResourceModel)
    def get(self):
        return ResourceDao.read_all()


@api.route('/<int:id>')
@api.param('id', 'The resource identifier')
@api.response(404, 'Resource not found')
class Resource(Resource):
    @api.doc('get by given id')
    @api.marshal_with(ResourceModel)
    def get(self, id):
        obj = ResourceDao.read(id)
        if obj is not None:
            return obj
        else:
            api.abort(404, 'Resource {} does not exist'.format(id))
