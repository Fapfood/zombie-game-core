from ..database import db

association_table = db.Table('production_x_building_type', db.Model.metadata,
                             db.Column('production_id', db.Integer, db.ForeignKey('production.id')),
                             db.Column('building_type_id', db.Integer, db.ForeignKey('building_type.id')),
                             )


class BuildingTypeEntity(db.Model):
    __tablename__ = 'building_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    max_workers = db.Column(db.Integer, nullable=False)
    available_productions = db.relationship('ProductionEntity', secondary=association_table)
