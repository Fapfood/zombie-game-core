from flask_restplus import Model, fields

SearchZoneModel = Model('SearchZone', {
    'id': fields.Integer(required=True, description='Search zone id'),
})
