from ..database import db


class ShapePointEntity(db.Model):
    __tablename__ = 'shape_point'
    id = db.Column(db.Integer, primary_key=True)
    long = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    ring_id = db.Column(db.Integer, db.ForeignKey('shape_ring.id'))


class ShapeRingEntity(db.Model):
    __tablename__ = 'shape_ring'
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, nullable=False)
    polygon_id = db.Column(db.Integer, db.ForeignKey('shape_polygon.id'))
    points = db.relationship('ShapePointEntity', order_by='ShapePointEntity.order')


class ShapePolygonEntity(db.Model):
    __tablename__ = 'shape_polygon'
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, nullable=False)
    multipolygon_id = db.Column(db.Integer, db.ForeignKey('shape_multipolygon.id'))
    rings = db.relationship('ShapeRingEntity', order_by='ShapeRingEntity.order')


class ShapeMultiPolygonEntity(db.Model):
    __tablename__ = 'shape_multipolygon'
    id = db.Column(db.Integer, primary_key=True)
    polygons = db.relationship('ShapePolygonEntity', order_by='ShapePolygonEntity.order')
