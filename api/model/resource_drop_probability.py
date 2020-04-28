from flask_restplus import Model, fields

ResourceDropProbabilityModel = Model('ResourceDropProbability', {
    'id': fields.Integer(required=True),
})
