from ..entity import ResourceEntity


class ResourceDAO:
    def __init__(self, db):
        self.db = db
        self.class_entity = ResourceEntity

    def read_by_id(self, id):
        obj = self.db.session.query(self.class_entity).filter_by(id=id).one_or_none()
        return obj

    def read_all(self):
        objs = self.db.session.query(self.class_entity).all()
        return objs

    def read_all_by_names(self, names):
        objs = self.db.session.query(self.class_entity).filter(self.class_entity.name.in_(names)).all()
        return objs

    def read_all_by_type_id(self, id):
        # obj = self.db.session.query(self.class_entity).join(ResourceTypeEntity).filter(
        #     ResourceTypeEntity.id == id).all()
        obj = self.db.session.query(self.class_entity).filter_by(resource_type_id=id).all()
        return obj

    def create(self, **kwargs):
        obj = self.class_entity(**kwargs)
        self.db.session.add(obj)
        self.db.session.commit()
        return obj

    def update_by_id(self, id, **kwargs):
        query = self.db.session.query(self.class_entity).filter_by(id=id)
        query.update(kwargs)
        obj = query.one_or_none()
        self.db.session.commit()
        return obj

    def change_quantity(self, id, change_by):
        obj = self.read_by_id(id)
        obj.quantity += change_by
        self.db.session.commit()
        return obj

    def delete(self, id):
        obj = self.read_by_id(id)
        self.db.session.delete(obj)
        self.db.session.commit()
