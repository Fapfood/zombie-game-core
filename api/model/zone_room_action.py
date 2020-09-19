from flask_restplus import Model, fields

ZoneRoomActionModel = Model('ZoneRoomAction', {
    'id': fields.Integer(required=True),
})
