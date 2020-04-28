from flask_restplus import Model, fields

BuildingTypeModelSimple = Model('BuildingType', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'max_workers': fields.Integer(required=True),
    'worker_icon_male': fields.String(required=True),
    'worker_icon_female': fields.String(required=True),
})
