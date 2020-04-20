from ..database import db

association_table_1 = db.Table('skill_pack_x_production_type', db.Model.metadata,
                               db.Column('skill_pack_id', db.Integer, db.ForeignKey('skill_pack.id')),
                               db.Column('production_type_id', db.Integer, db.ForeignKey('production_type.id')),
                               )

association_table_2 = db.Table('tools_resource_pack_x_production_type', db.Model.metadata,
                               db.Column('resource_pack_id', db.Integer, db.ForeignKey('resource_pack.id')),
                               db.Column('production_type_id', db.Integer, db.ForeignKey('production_type.id')),
                               )

association_table_3 = db.Table('from_resource_pack_x_production_type', db.Model.metadata,
                               db.Column('resource_pack_id', db.Integer, db.ForeignKey('resource_pack.id')),
                               db.Column('production_type_id', db.Integer, db.ForeignKey('production_type.id')),
                               )

association_table_4 = db.Table('successful_resource_pack_x_production_type', db.Model.metadata,
                               db.Column('resource_pack_id', db.Integer, db.ForeignKey('resource_pack.id')),
                               db.Column('production_type_id', db.Integer, db.ForeignKey('production_type.id')),
                               )

association_table_5 = db.Table('interrupted_resource_pack_x_production_type', db.Model.metadata,
                               db.Column('resource_pack_id', db.Integer, db.ForeignKey('resource_pack.id')),
                               db.Column('production_type_id', db.Integer, db.ForeignKey('production_type.id')),
                               )


class ProductionTypeEntity(db.Model):
    __tablename__ = 'production_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    minutes = db.Column(db.Integer, nullable=False)
    required_skills = db.relationship('SkillPackEntity', secondary=association_table_1, lazy='dynamic')
    required_tools = db.relationship('ResourcePackEntity', secondary=association_table_2, lazy='dynamic')
    from_resources = db.relationship('ResourcePackEntity', secondary=association_table_3, lazy='dynamic')
    to_resources_successful = db.relationship('ResourcePackEntity', secondary=association_table_4, lazy='dynamic')
    to_resources_interrupted = db.relationship('ResourcePackEntity', secondary=association_table_5, lazy='dynamic')
