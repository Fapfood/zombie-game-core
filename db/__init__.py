from .dao import BuildingDAO
from .dao import BuildingTypeDAO
from .dao import PersonDAO
from .dao import ProductionTypeDAO
from .dao import ResourceDAO
from .dao import ResourceDropProbabilityDAO
from .dao import ResourcePackDAO
from .dao import ResourceTypeDAO
from .dao import SearchZoneActionDAO
from .dao import SearchZoneActionTypeDAO
from .dao import SearchZoneDAO
from .dao import SearchZoneTypeDAO
from .dao import ShapeMultiPolygonDAO
from .dao import ShapePointDAO
from .dao import ShapePolygonDAO
from .dao import ShapeRingDAO
from .dao import SkillDAO
from .dao import SkillLevelDAO
from .dao import SkillPackDAO
from .dao import SkillTypeDAO
from .database import db

BuildingDao = BuildingDAO(db)
BuildingTypeDao = BuildingTypeDAO(db)
PersonDao = PersonDAO(db)
ProductionTypeDao = ProductionTypeDAO(db)
ResourceDao = ResourceDAO(db)
ResourceDropProbabilityDao = ResourceDropProbabilityDAO(db)
ResourcePackDao = ResourcePackDAO(db)
ResourceTypeDao = ResourceTypeDAO(db)
SearchZoneActionDao = SearchZoneActionDAO(db)
SearchZoneActionTypeDao = SearchZoneActionTypeDAO(db)
SearchZoneDao = SearchZoneDAO(db)
SearchZoneTypeDao = SearchZoneTypeDAO(db)
ShapeMultiPolygonDao = ShapeMultiPolygonDAO(db)
ShapePointDao = ShapePointDAO(db)
ShapePolygonDao = ShapePolygonDAO(db)
ShapeRingDao = ShapeRingDAO(db)
SkillDao = SkillDAO(db)
SkillLevelDao = SkillLevelDAO(db)
SkillPackDao = SkillPackDAO(db)
SkillTypeDao = SkillTypeDAO(db)
