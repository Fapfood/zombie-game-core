from flask_restplus import Model, fields

SearchZoneActionModel = Model('SearchZoneAction', {
    'id': fields.Integer(required=True, description='Search zone action id'),
})
