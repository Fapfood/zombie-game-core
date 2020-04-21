from flask_restplus import Model, fields

BuildingTypeModelSimple = Model('BuildingType', {
    'id': fields.Integer(required=True, description='Building type id'),
    'name': fields.String(required=True, description='Building type name'),
    'max_workers': fields.Integer(required=True, description='Building type max workers'),
    'worker_icon_male': fields.String(required=True, description='Building worker icon male'),
    'worker_icon_female': fields.String(required=True, description='Building worker icon female'),
})
