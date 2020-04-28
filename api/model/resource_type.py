from flask_restplus import Model, fields

ResourceTypeModelSimple = Model('ResourceType', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
})
