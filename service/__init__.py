from db import PersonDao
from db import ResourceDao
from db import ShapeMultiPolygonDao
from db import ShapePointDao
from db import ShapePolygonDao
from db import ShapeRingDao
from db import SkillDao
from db import ZoneRoomDao
from .person import PersonService
from .resource import ResourceService
from .shape import ShapeService
from .skill import SkillService
from .zone_room import ZoneRoomService

SkillSvc = SkillService(SkillDao)
PersonSvc = PersonService(PersonDao, SkillSvc)
ShapeSvc = ShapeService(ShapePointDao, ShapeRingDao, ShapePolygonDao, ShapeMultiPolygonDao)
ResourceSvc = ResourceService(ResourceDao)
ZoneRoomSvc = ZoneRoomService(ZoneRoomDao, ResourceSvc)
