from flask_restplus import Model, fields

ShapePointModel = Model('ShapePoint', {
    'id': fields.Integer(required=True),
    'order': fields.Integer(required=True),
    'long': fields.Float(required=True),
    'lat': fields.Float(required=True),
})

ShapeRingModel = Model('ShapeRing', {
    'id': fields.Integer(required=True),
    'order': fields.Integer(required=True),
    'points': fields.List(fields.Nested(ShapePointModel), required=True),
})

ShapePolygonModel = Model('ShapePolygon', {
    'id': fields.Integer(required=True),
    'order': fields.Integer(required=True),
    'rings': fields.List(fields.Nested(ShapeRingModel), required=True),
})

ShapeMultiPolygonModel = Model('ShapeMultiPolygon', {
    'id': fields.Integer(required=True),
    'polygons': fields.List(fields.Nested(ShapePolygonModel), required=True),
})
