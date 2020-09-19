from flask_restplus import Model, fields

ZoneModel = Model('Zone', {
    'id': fields.Integer(required=True),
})
