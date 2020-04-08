from .dao import BuildingDAO, BuildingTypeDAO, PersonDAO, ProductionDAO, \
    ResourceDAO, ResourceDropProbabilityDAO, ResourcePackDAO, ResourceTypeDAO, \
    SearchZoneDAO, SearchZoneActionDAO, SearchZoneTypeDAO, \
    ShapePointDAO, ShapeRingDAO, ShapePolygonDAO, ShapeMultiPolygonDAO, \
    SkillDAO, SkillLevelDAO, SkillTypeDAO
from .database import db

BuildingDao = BuildingDAO(db)
BuildingTypeDao = BuildingTypeDAO(db)
PersonDao = PersonDAO(db)
ProductionDao = ProductionDAO(db)
ResourceDao = ResourceDAO(db)
ResourceDropProbabilityDao = ResourceDropProbabilityDAO(db)
ResourcePackDao = ResourcePackDAO(db)
ResourceTypeDao = ResourceTypeDAO(db)
SearchZoneDao = SearchZoneDAO(db)
SearchZoneActionDao = SearchZoneActionDAO(db)
SearchZoneTypeDao = SearchZoneTypeDAO(db)
ShapePointDao = ShapePointDAO(db)
ShapeRingDao = ShapeRingDAO(db)
ShapePolygonDao = ShapePolygonDAO(db)
ShapeMultiPolygonDao = ShapeMultiPolygonDAO(db)
SkillDao = SkillDAO(db)
SkillLevelDao = SkillLevelDAO(db)
SkillTypeDao = SkillTypeDAO(db)
