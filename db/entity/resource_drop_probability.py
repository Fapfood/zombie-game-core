from ..database import db


class ResourceDropProbabilityEntity(db.Model):
    __tablename__ = 'resource_drop_probability'
    id = db.Column(db.Integer, primary_key=True)
    probability = db.Column(db.Float, nullable=False)
    resource_type_id = db.Column(db.Integer, db.ForeignKey('resource_type.id'), nullable=False)
    type = db.relationship('ResourceTypeEntity')
