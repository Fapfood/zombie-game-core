from flask_restplus import Namespace, Resource, marshal

from service import BuildingSvc
from view.decorator import modal_result
from .model import BuildingModel as BuildingModel

api = Namespace('building')
api.add_model('Building', BuildingModel)

parser = api.parser()
parser.add_argument('building_type_id')
parser.add_argument('production_type_id')
parser.add_argument('worker', action='append')


@api.route('')
class BuildingList(Resource):
    @api.doc('list all')
    @api.marshal_list_with(BuildingModel)
    def get(self):
        return BuildingSvc.read_all()


@api.route('/<int:id>')
@api.param('id', 'The building identifier')
@api.response(404, 'Building not found')
class Building(Resource):
    @api.doc('get or update by given id')
    @modal_result
    # @api.marshal_with(BuildingModel)
    def post(self, id):
        args = parser.parse_args()
        building_type_id = args.get('building_type_id')
        production_type_id = args.get('production_type_id')
        workers = args.get('worker') if args.get('worker') is not None else []

        result = BuildingSvc.update_by_id(id, building_type_id, production_type_id, workers)
        return marshal(result, BuildingModel, skip_none=True)
