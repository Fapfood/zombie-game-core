from ..database import db


class SearchZoneEntity(db.Model):
    __tablename__ = 'search_zone'
    id = db.Column(db.Integer, primary_key=True)
    search_zone_type_id = db.Column(db.Integer, db.ForeignKey('search_zone_type.id'))
    type = db.relationship('SearchZoneTypeEntity', backref='zones')
    long = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    multipolygon_id = db.Column(db.Integer, db.ForeignKey('shape_multipolygon.id'), nullable=False)
    shape = db.relationship('ShapeMultiPolygonEntity')
