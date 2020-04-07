from .dao import BuildingDAO, BuildingTypeDAO, PersonDAO, ProductionDAO, \
    ResourceDAO, ResourcePackDAO, ResourceTypeDAO, SearchZoneDAO, SearchZoneTypeDAO, \
    ShapePointDAO, ShapeRingDAO, ShapePolygonDAO, ShapeMultiPolygonDAO, \
    SkillLevelDAO, SkillTypeDAO
from .database import db
from .migration import migration

BuildingDao = BuildingDAO(db)
BuildingTypeDao = BuildingTypeDAO(db)
PersonDao = PersonDAO(db)
ProductionDao = ProductionDAO(db)
ResourceDao = ResourceDAO(db)
ResourcePackDao = ResourcePackDAO(db)
ResourceTypeDao = ResourceTypeDAO(db)
SearchZoneDao = SearchZoneDAO(db)
SearchZoneTypeDao = SearchZoneTypeDAO(db)
ShapePointDao = ShapePointDAO(db)
ShapeRingDao = ShapeRingDAO(db)
ShapePolygonDao = ShapePolygonDAO(db)
ShapeMultiPolygonDao = ShapeMultiPolygonDAO(db)
SkillLevelDao = SkillLevelDAO(db)
SkillTypeDao = SkillTypeDAO(db)
