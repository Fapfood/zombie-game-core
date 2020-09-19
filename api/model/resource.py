from flask_restplus import Model, fields

ResourceModel = Model('Resource', {
    'id': fields.Integer(required=True),
    'type': fields.String(required=True),
    'icon': fields.String(required=True),
    'available': fields.Boolean(required=True),
    'owned': fields.Boolean(required=True),
    'quality': fields.Integer(required=True),
    'decay': fields.Integer(required=True),
})
