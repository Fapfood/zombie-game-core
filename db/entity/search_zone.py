from ..database import db

association_table = db.Table('resource_x_search_zone', db.Model.metadata,
                             db.Column('resource_id', db.Integer, db.ForeignKey('resource.id')),
                             db.Column('search_zone_id', db.Integer, db.ForeignKey('search_zone.id')),
                             )


class SearchZoneEntity(db.Model):
    __tablename__ = 'search_zone'
    id = db.Column(db.Integer, primary_key=True)
    search_zone_type_id = db.Column(db.Integer, db.ForeignKey('search_zone_type.id'))
    type = db.relationship('SearchZoneTypeEntity', backref='zones')
    long = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    multipolygon_id = db.Column(db.Integer, db.ForeignKey('shape_multipolygon.id'), nullable=False)
    shape = db.relationship('ShapeMultiPolygonEntity')
    resources = db.relationship('ResourceEntity', secondary=association_table)
