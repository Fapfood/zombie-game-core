from ..database import db


class BuildingEntity(db.Model):
    __tablename__ = 'building'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    production_type = db.Column(db.String, nullable=False)
    multipolygon_id = db.Column(db.Integer, db.ForeignKey('shape_multipolygon.id'), nullable=False)
    shape = db.relationship('ShapeMultiPolygonEntity')
