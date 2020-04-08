from db import PersonDao, SearchZoneDao, SearchZoneTypeDao, \
    ShapePointDao, ShapeRingDao, ShapePolygonDao, ShapeMultiPolygonDao, \
    SkillLevelDao, SkillTypeDao, ResourceDao, ResourceTypeDao
from .person import PersonService
from .search_zone import SearchZoneService
from .shape import ShapeService

PersonSvc = PersonService(PersonDao, SkillTypeDao, SkillLevelDao)
SearchZoneSvc = SearchZoneService(SearchZoneTypeDao, SearchZoneDao, ResourceTypeDao, ResourceDao)
ShapeSvc = ShapeService(ShapePointDao, ShapeRingDao, ShapePolygonDao, ShapeMultiPolygonDao)
