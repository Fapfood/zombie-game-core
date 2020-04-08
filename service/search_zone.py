class SearchZoneService:
    def __init__(self, searchZoneTypeDao, searchZoneDao, resourceTypeDao, resourceDao):
        self.searchZoneTypeDao = searchZoneTypeDao
        self.searchZoneDao = searchZoneDao
        self.resourceTypeDao = resourceTypeDao
        self.resourceDao = resourceDao

    def generate_search_zone(self, long, lat):
        search_zone = self.searchZoneDao.create()
        return search_zone

    def search_in(self, id):
        self.searchZoneDao.read_by_id(id)
