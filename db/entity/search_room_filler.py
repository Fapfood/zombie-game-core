from ..database import db

association_table_1 = db.Table('resource_drop_probability_x_search_room_filler', db.Model.metadata,
                               db.Column('resource_drop_probability_id', db.Integer,
                                         db.ForeignKey('resource_drop_probability.id')),
                               db.Column('search_room_filler_id', db.Integer, db.ForeignKey('search_room_filler.id')),
                               )

association_table_2 = db.Table('search_room_action_type_x_search_room_filler', db.Model.metadata,
                               db.Column('search_room_action_type_id', db.Integer,
                                         db.ForeignKey('search_room_action_type.id')),
                               db.Column('search_room_filler_id', db.Integer, db.ForeignKey('search_room_filler.id')),
                               )


class SearchRoomFillerEntity(db.Model):
    __tablename__ = 'search_room_filler'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    search_room_type_id = db.Column(db.Integer, db.ForeignKey('search_room_type.id'), nullable=False)
    type = db.relationship('SearchRoomTypeEntity')
    resource_drop_table = db.relationship('ResourceDropProbabilityEntity', secondary=association_table_1)
    search_room_action_types = db.relationship('SearchRoomActionTypeEntity', secondary=association_table_2)
