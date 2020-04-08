from ..database import db

association_table_1 = db.Table('skill_level_x_production', db.Model.metadata,
                               db.Column('skill_level_id', db.Integer, db.ForeignKey('skill_level.id')),
                               db.Column('production_id', db.Integer, db.ForeignKey('production.id')),
                               )

association_table_2 = db.Table('tools_resource_pack_x_production', db.Model.metadata,
                               db.Column('resource_pack_id', db.Integer, db.ForeignKey('resource_pack.id')),
                               db.Column('production_id', db.Integer, db.ForeignKey('production.id')),
                               )

association_table_3 = db.Table('from_resource_pack_x_production', db.Model.metadata,
                               db.Column('resource_pack_id', db.Integer, db.ForeignKey('resource_pack.id')),
                               db.Column('production_id', db.Integer, db.ForeignKey('production.id')),
                               )

association_table_4 = db.Table('successful_resource_pack_x_production', db.Model.metadata,
                               db.Column('resource_pack_id', db.Integer, db.ForeignKey('resource_pack.id')),
                               db.Column('production_id', db.Integer, db.ForeignKey('production.id')),
                               )

association_table_5 = db.Table('interrupted_resource_pack_x_production', db.Model.metadata,
                               db.Column('resource_pack_id', db.Integer, db.ForeignKey('resource_pack.id')),
                               db.Column('production_id', db.Integer, db.ForeignKey('production.id')),
                               )


class ProductionEntity(db.Model):
    __tablename__ = 'production'
    id = db.Column(db.Integer, primary_key=True)
    minutes = db.Column(db.Integer, nullable=False)
    required_skills = db.relationship('SkillLevelEntity', secondary=association_table_1)
    required_tools = db.relationship('ResourcePackEntity', secondary=association_table_2)
    from_resources = db.relationship('ResourcePackEntity', secondary=association_table_3)
    to_resources_successful = db.relationship('ResourcePackEntity', secondary=association_table_4)
    to_resources_interrupted = db.relationship('ResourcePackEntity', secondary=association_table_5)
