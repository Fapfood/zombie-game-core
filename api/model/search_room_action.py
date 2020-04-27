from flask_restplus import Model, fields

SearchRoomActionModel = Model('SearchRoomAction', {
    'id': fields.Integer(required=True, description='Search room action id'),
})
