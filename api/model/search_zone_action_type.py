from flask_restplus import Model, fields

SearchZoneActionTypeModel = Model('SearchZoneActionType', {
    'id': fields.Integer(required=True),
})
