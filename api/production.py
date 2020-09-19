from flask_restplus import Namespace, Resource

from service import ProductionSvc
from view.decorator import modal_body_with
from .model import ProductionModel

api = Namespace('production')
api.add_model('Production', ProductionModel)

parser = api.parser()
parser.add_argument('type')
parser.add_argument('worker', action='append')
parser.add_argument('tool', action='append')
parser.add_argument('resource', action='append')


@api.route('')
class ProductionList(Resource):
    @api.doc('list all')
    @api.marshal_list_with(ProductionModel)
    def get(self):
        return ProductionSvc.read_all()

    @api.doc('create')
    @modal_body_with(ProductionModel)
    def post(self):
        args = parser.parse_args()
        type = args.get('type')
        workers = args.get('worker') if args.get('worker') is not None else []
        tools = args.get('tool') if args.get('tool') is not None else []
        resources = args.get('resource') if args.get('resource') is not None else []

        result = ProductionSvc.start_production(type, workers=workers, tools=tools, resources=resources)
        return result
