from flask_restplus import Model, fields

ProductionModel = Model('Production', {
    'id': fields.Integer(required=True),
})
