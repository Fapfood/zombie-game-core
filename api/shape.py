from flask_restplus import Namespace, Resource

from db import ShapeMultiPolygonDao
from .model import ShapePointModel as ShapePointModel, ShapeRingModel as ShapeRingModel, \
    ShapePolygonModel as ShapePolygonModel, ShapeMultiPolygonModel as ShapeMultiPolygonModel

api = Namespace('shape')
api.add_model('ShapePoint', ShapePointModel)
api.add_model('ShapeRing', ShapeRingModel)
api.add_model('ShapePolygon', ShapePolygonModel)
api.add_model('ShapeMultiPolygon', ShapeMultiPolygonModel)


@api.route('')
class ShapeList(Resource):
    @api.doc('list all')
    @api.marshal_list_with(ShapeMultiPolygonModel)
    def get(self):
        return ShapeMultiPolygonDao.read_all()
