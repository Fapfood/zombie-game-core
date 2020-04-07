class SearchZoneService:
    def __init__(self, searchZoneDao, resourceTypeDao, resourceDao):
        self.searchZoneDao = searchZoneDao
        self.resourceTypeDao = resourceTypeDao
        self.resourceDao = resourceDao

    def search_in(self, id):
        self.searchZoneDao.read_by_id(id)
