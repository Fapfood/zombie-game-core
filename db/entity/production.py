from ..database import db


class ProductionEntity(db.Model):
    __tablename__ = 'production'
    id = db.Column(db.Integer, primary_key=True)
