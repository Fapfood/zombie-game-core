from flask_restplus import Model, fields

SearchRoomTypeModel = Model('SearchRoomType', {
    'id': fields.Integer(required=True),
})
