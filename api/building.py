from flask_restplus import Namespace, Resource, marshal

from service import BuildingRoomSvc
from service import BuildingSvc
from view.decorator import modal_result
from .model import BuildingModel
from .model import BuildingRoomModel

api = Namespace('building')
api.add_model('Building', BuildingModel)
api.add_model('BuildingRoom', BuildingRoomModel)

parser = api.parser()
parser.add_argument('room_id')
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
    @api.doc('get by given id')
    @api.marshal_with(BuildingModel)
    def get(self, id):
        return BuildingSvc.read_by_id(id)

    @api.doc('update by given id')
    @modal_result
    def post(self, id):
        args = parser.parse_args()
        room_id = args.get('room_id')
        BuildingSvc.focus_on(id, room_id)
        return 'ok'


@api.route('/<int:id>/room')
@api.param('id', 'The building identifier')
@api.response(404, 'Building not found')
class BuildingRoomList(Resource):
    @api.doc('list all')
    @api.marshal_list_with(BuildingRoomModel)
    def get(self, id):
        return BuildingSvc.read_by_id(id).rooms


@api.route('/<int:id>/room/<int:room_id>')
@api.param('id', 'The building identifier')
@api.param('room_id', 'The building room identifier')
@api.response(404, 'Building room not found')
class BuildingRoom(Resource):
    @api.doc('get by given id')
    @api.marshal_with(BuildingRoomModel)
    def get(self, id, room_id):
        return BuildingRoomSvc.read_by_id(room_id)

    @api.doc('update by given id')
    @modal_result
    def post(self, id, room_id):
        args = parser.parse_args()
        building_type_id = args.get('building_type_id')
        production_type_id = args.get('production_type_id')
        workers = args.get('worker') if args.get('worker') is not None else []

        result = BuildingRoomSvc.update_by_id(room_id, building_type_id, production_type_id, workers)
        return marshal(result, BuildingRoomModel, skip_none=True)
