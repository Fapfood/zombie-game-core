from db import BuildingTypeDao
from db import ProductionTypeDao
from db import ResourceDropProbabilityDao
from db import ResourcePackDao
from db import ResourceTypeDao
from db import SearchRoomActionTypeDao
from db import SearchRoomBlankDao
from db import SearchRoomFillerDao
from db import SearchRoomTypeDao
from db import SkillLevelDao
from db import SkillPackDao
from db import SkillTypeDao
from .building import BuildingService
from .production import ProductionService
from .resource import ResourceService
from .search_room import SearchRoomService
from .skill import SkillService

ResourceSvc = ResourceService(ResourceTypeDao, ResourcePackDao, ResourceDropProbabilityDao)
SkillSvc = SkillService(SkillTypeDao, SkillLevelDao, SkillPackDao)
ProductionSvc = ProductionService(ProductionTypeDao, ResourceSvc, SkillSvc)
BuildingSvc = BuildingService(BuildingTypeDao, ProductionSvc)
SearchRoomSvc = SearchRoomService(SearchRoomActionTypeDao, SearchRoomTypeDao, SearchRoomFillerDao, SearchRoomBlankDao,
                                  ResourceSvc)
