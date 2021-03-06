class BaseDAO:
    def __init__(self, db, class_entity):
        self.db = db
        self.class_entity = class_entity

    def commit(self, obj):
        self.db.session.merge(obj)
        self.db.session.flush()
        self.db.session.commit()

    def _query_by_id(self, id):
        obj = self.db.session.query(self.class_entity).filter_by(id=id)
        return obj

    def read_by_id(self, id):
        obj = self._query_by_id(id).one_or_none()
        return obj

    def read_all(self):
        objs = self.db.session.query(self.class_entity).all()
        return objs

    def read_all_by(self, **kwargs):
        objs = self.db.session.query(self.class_entity).filter_by(**kwargs).all()
        return objs

    def create(self, **kwargs):
        obj = self.class_entity(**kwargs)
        self.db.session.add(obj)
        self.commit(obj)
        return obj

    def update_by_id(self, id, **kwargs):
        query = self._query_by_id(id)
        query.update(kwargs)
        obj = query.one_or_none()
        self.commit(obj)
        return obj

    # def update_by_id(self, id, **kwargs):
    #     obj = self.read_by_id(id)
    #     if obj is not None:
    #         obj.update(**kwargs)
    #         self.commit()
    #     return obj

    def delete_by_id(self, id):
        obj = self.read_by_id(id)
        self.db.session.delete(obj)
        self.commit(obj)

    # def delete(self, id):
    #     obj = self.read_by_id(id)
    #     if obj is not None:
    #         self.db.session.delete(obj)
    #         self.commit()
