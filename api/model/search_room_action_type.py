from flask_restplus import Model, fields

SearchRoomActionTypeModel = Model('SearchRoomActionType', {
    'id': fields.Integer(required=True, description='Search room action type id'),
})
