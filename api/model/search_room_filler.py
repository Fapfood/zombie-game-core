from flask_restplus import Model, fields

SearchRoomFillerModel = Model('SearchRoomFiller', {
    'id': fields.Integer(required=True),
})
