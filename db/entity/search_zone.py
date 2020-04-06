from ..database import db


class SearchZoneEntity(db.Model):
    __tablename__ = 'search_zone'
    id = db.Column(db.Integer, primary_key=True)
    multipolygon_id = db.Column(db.Integer, db.ForeignKey('shape_multipolygon.id'))
    shape = db.relationship('ShapeMultiPolygonEntity')
