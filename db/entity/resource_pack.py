from ..database import db


class ResourcePackEntity(db.Model):
    __tablename__ = 'resource_pack'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    resource_type_id = db.Column(db.Integer, db.ForeignKey('resource_type.id'), nullable=False)
    type = db.relationship('ResourceTypeEntity')

    def __le__(self, other):
        if self.resource_type_id != other.resource_type_id:
            return False
        if self.quantity <= other.quantity:
            return True
        return False

    def __lt__(self, other):
        if self.resource_type_id != other.resource_type_id:
            return False
        if self.quantity < other.quantity:
            return True
        return False

    def __ge__(self, other):
        if self.resource_type_id != other.resource_type_id:
            return False
        if self.quantity >= other.quantity:
            return True
        return False

    def __gt__(self, other):
        if self.resource_type_id != other.resource_type_id:
            return False
        if self.quantity > other.quantity:
            return True
        return False
