from ..database import db


class ResourceTypeEntity(db.Model):
    __tablename__ = 'resource_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    weight = db.Column(db.Float, nullable=False, default=1)

