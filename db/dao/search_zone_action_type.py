from ..base_dao import BaseDAO
from ..entity import SearchZoneActionTypeEntity


class SearchZoneActionTypeDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SearchZoneActionTypeEntity)

    def read_by_name(self, name):
        obj = self.db.session.query(self.class_entity).filter_by(name=name).one_or_none()
        return obj
