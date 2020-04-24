from ..database import db

association_table_1 = db.Table('skill_pack_x_search_zone_action_type', db.Model.metadata,
                               db.Column('skill_pack_id', db.Integer, db.ForeignKey('skill_pack.id')),
                               db.Column('search_zone_action_type_id', db.Integer,
                                         db.ForeignKey('search_zone_action_type.id')),
                               )

association_table_2 = db.Table('tools_resource_pack_x_search_zone_action_type', db.Model.metadata,
                               db.Column('resource_pack_id', db.Integer, db.ForeignKey('resource_pack.id')),
                               db.Column('search_zone_action_type_id', db.Integer,
                                         db.ForeignKey('search_zone_action_type.id')),
                               )


class SearchZoneActionTypeEntity(db.Model):
    __tablename__ = 'search_zone_action_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    required_number_of_people = db.Column(db.Integer, nullable=False)
    required_skills = db.relationship('SkillPackEntity', secondary=association_table_1)
    required_tools = db.relationship('ResourcePackEntity', secondary=association_table_2)
