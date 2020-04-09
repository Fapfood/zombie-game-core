from db import PersonDao, ProductionDao, SearchZoneDao, SearchZoneTypeDao, \
    ShapePointDao, ShapeRingDao, ShapePolygonDao, ShapeMultiPolygonDao, \
    ResourceDao, ResourceTypeDao, ResourcePackDao, SkillLevelDao, SkillTypeDao
from .person import PersonService
from .production import ProductionService
from .search_zone import SearchZoneService
from .shape import ShapeService

PersonSvc = PersonService(PersonDao, SkillTypeDao, SkillLevelDao)
ProductionSvc = ProductionService(ProductionDao, ResourceTypeDao, ResourcePackDao, SkillTypeDao, SkillLevelDao)
SearchZoneSvc = SearchZoneService(SearchZoneTypeDao, SearchZoneDao, ResourceTypeDao, ResourceDao)
ShapeSvc = ShapeService(ShapePointDao, ShapeRingDao, ShapePolygonDao, ShapeMultiPolygonDao)
