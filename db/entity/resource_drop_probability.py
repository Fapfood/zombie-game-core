from ..database import db


class ResourceDropProbabilityEntity(db.Model):
    __tablename__ = 'resource_drop_probability'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    probability = db.Column(db.Float, nullable=False)
    resource_type_id = db.Column(db.Integer, db.ForeignKey('resource_type.id'), nullable=False)
    type = db.relationship('ResourceTypeEntity')
