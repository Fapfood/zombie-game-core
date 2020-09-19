from flask_restplus import Model, fields

ZoneDoorModel = Model('ZoneDoor', {
    'id': fields.Integer(required=True),
})
