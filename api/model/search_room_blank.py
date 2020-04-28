from flask_restplus import Model, fields

SearchRoomBlankModel = Model('SearchRoomBlank', {
    'id': fields.Integer(required=True),
})
