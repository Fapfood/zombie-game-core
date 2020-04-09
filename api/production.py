from flask_restplus import Namespace, Resource

from db import ProductionDao
from .model import ProductionModel as ProductionModel

api = Namespace('production')
api.add_model('Production', ProductionModel)


@api.route('')
class ProductionList(Resource):
    @api.doc('list all')
    @api.marshal_list_with(ProductionModel)
    def get(self):
        return ProductionDao.read_all()
