from ..database import db

association_table_1 = db.Table('resource_drop_probability_x_search_zone_type', db.Model.metadata,
                               db.Column('resource_drop_probability_id', db.Integer,
                                         db.ForeignKey('resource_drop_probability.id')),
                               db.Column('search_zone_type_id', db.Integer, db.ForeignKey('search_zone_type.id')),
                               )

association_table_2 = db.Table('search_zone_action_type_x_search_zone_type', db.Model.metadata,
                               db.Column('search_zone_action_type_id', db.Integer,
                                         db.ForeignKey('search_zone_action_type.id')),
                               db.Column('search_zone_type_id', db.Integer, db.ForeignKey('search_zone_type.id')),
                               )


class SearchZoneTypeEntity(db.Model):
    __tablename__ = 'search_zone_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    resource_drop_table = db.relationship('ResourceDropProbabilityEntity', secondary=association_table_1)
    search_zone_action_types = db.relationship('SearchZoneActionTypeEntity', secondary=association_table_2)
