from .dao import BuildingDAO
from .dao import PersonDAO
from .dao import ResourceDAO
from .dao import ShapeMultiPolygonDAO
from .dao import ShapePointDAO
from .dao import ShapePolygonDAO
from .dao import ShapeRingDAO
from .dao import SkillDAO
from .dao import ZoneActionDAO
from .dao import ZoneDAO
from .dao import ZoneDoorDAO
from .dao import ZoneRoomActionDAO
from .dao import ZoneRoomDAO
from .database import db

BuildingDao = BuildingDAO(db)
PersonDao = PersonDAO(db)
ResourceDao = ResourceDAO(db)
ShapeMultiPolygonDao = ShapeMultiPolygonDAO(db)
ShapePointDao = ShapePointDAO(db)
ShapePolygonDao = ShapePolygonDAO(db)
ShapeRingDao = ShapeRingDAO(db)
SkillDao = SkillDAO(db)
ZoneDao = ZoneDAO(db)
ZoneActionDao = ZoneActionDAO(db)
ZoneDoorDao = ZoneDoorDAO(db)
ZoneRoomDao = ZoneRoomDAO(db)
ZoneRoomActionDao = ZoneRoomActionDAO(db)
