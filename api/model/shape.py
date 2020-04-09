from flask_restplus import Model, fields

ShapePointModel = Model('ShapePoint', {
    'id': fields.Integer(required=True, description='Point id'),
    'order': fields.Integer(required=True, description='Point order'),
    'long': fields.Float(required=True, description='Longitude coordinate'),
    'lat': fields.Float(required=True, description='Latitude coordinate'),
})

ShapeRingModel = Model('ShapeRing', {
    'id': fields.Integer(required=True, description='Ring id'),
    'order': fields.Integer(required=True, description='Rings order'),
    'points': fields.List(required=True, cls_or_instance=fields.Nested(ShapePointModel),
                          description='Points'),
})

ShapePolygonModel = Model('ShapePolygon', {
    'id': fields.Integer(required=True, description='Polygon id'),
    'order': fields.Integer(required=True, description='Polygons order'),
    'rings': fields.List(required=True, cls_or_instance=fields.Nested(ShapeRingModel),
                         description='Rings'),
})

ShapeMultiPolygonModel = Model('ShapeMultiPolygon', {
    'id': fields.Integer(required=True, description='Multipolygon id'),
    'polygons': fields.List(required=True, cls_or_instance=fields.Nested(ShapePolygonModel),
                            description='Polygons'),
})
