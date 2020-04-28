from flask_restplus import Model, fields

SearchZoneTypeModel = Model('SearchZoneType', {
    'id': fields.Integer(required=True),
})
