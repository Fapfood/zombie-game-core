from ..entity import PersonEntity


class PersonDAO:
    def __init__(self, db):
        self.db = db
        self.class_entity = PersonEntity

    def read_by_id(self, id):
        obj = self.db.session.query(self.class_entity).filter_by(id=id).one_or_none()
        return obj

    def read_all(self):
        objs = self.db.session.query(self.class_entity).all()
        return objs

    def read_all_by_names(self, names):
        objs = self.db.session.query(self.class_entity).filter(self.class_entity.name.in_(names)).all()
        return objs

    def create(self, **kwargs):
        obj = self.class_entity(**kwargs)
        self.db.session.add(obj)
        self.db.session.commit()
        return obj

    def update_by_id(self, id, **kwargs):
        obj = self.read_by_id(id)
        if obj is not None:
            obj.update(**kwargs)
            self.db.session.commit()
            return obj
        else:
            return None

    def delete(self, id):
        obj = self.read_by_id(id)
        if obj is not None:
            self.db.session.delete(obj)
            self.db.session.commit()
