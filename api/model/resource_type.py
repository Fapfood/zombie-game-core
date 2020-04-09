from flask_restplus import Model, fields

ResourceTypeModelSimple = Model('ResourceType', {
    'id': fields.Integer(required=True, description='Resource type id'),
    'name': fields.String(required=True, description='Resource type name'),
})
