from ..database import db


class BuildingEntity(db.Model):
    __tablename__ = 'building'
    id = db.Column(db.Integer, primary_key=True)
    building_type_id = db.Column(db.Integer, db.ForeignKey('building_type.id'))
    type = db.relationship('BuildingTypeEntity', backref='buildings')
    multipolygon_id = db.Column(db.Integer, db.ForeignKey('shape_multipolygon.id'))
    shape = db.relationship('ShapeMultiPolygonEntity')
    production_type_id = db.Column(db.Integer, db.ForeignKey('production_type.id'))
    production_type = db.relationship('ProductionTypeEntity')
