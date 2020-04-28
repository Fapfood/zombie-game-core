from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from yaml import FullLoader
from yaml import load

from db.dao import BuildingDAO
from db.dao import BuildingTypeDAO
from db.dao import PersonDAO
from db.dao import ProductionDAO
from db.dao import ProductionTypeDAO
from db.dao import ResourceDAO
from db.dao import ResourceDropProbabilityDAO
from db.dao import ResourcePackDAO
from db.dao import ResourceTypeDAO
from db.dao import SearchRoomActionDAO
from db.dao import SearchRoomActionTypeDAO
from db.dao import SearchRoomBlankDAO
from db.dao import SearchRoomDAO
from db.dao import SearchRoomFillerDAO
from db.dao import SearchRoomTypeDAO
from db.dao import SearchZoneActionDAO
from db.dao import SearchZoneActionTypeDAO
from db.dao import SearchZoneDAO
from db.dao import SearchZoneTypeDAO
from db.dao import ShapeMultiPolygonDAO
from db.dao import ShapePointDAO
from db.dao import ShapePolygonDAO
from db.dao import ShapeRingDAO
from db.dao import SkillDAO
from db.dao import SkillLevelDAO
from db.dao import SkillPackDAO
from db.dao import SkillTypeDAO
from db.model import BuildingType
from db.model import ProductionType
from db.model import ResourceType
from db.model import SearchRoomFiller
from db.model import SearchRoomType
from db.model import SkillType
from service.shape_helper import Polygon, MultiPolygon, ring_regular
from service.type import BuildingService
from service.type import ProductionService
from service.type import ResourceService
from service.type import SearchRoomService
from service.type import SkillService

DB_STRING = 'sqlite:////Users/matr/dev/zombie-game-core/test.db'


def type_migration():
    engine = create_engine(DB_STRING)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()
    Base.session = session

    BuildingTypeDao = BuildingTypeDAO(Base)
    ProductionTypeDao = ProductionTypeDAO(Base)
    ResourceDropProbabilityDao = ResourceDropProbabilityDAO(Base)
    ResourcePackDao = ResourcePackDAO(Base)
    ResourceTypeDao = ResourceTypeDAO(Base)
    SearchRoomActionTypeDao = SearchRoomActionTypeDAO(Base)
    SearchRoomBlankDao = SearchRoomBlankDAO(Base)
    SearchRoomFillerDao = SearchRoomFillerDAO(Base)
    SearchRoomTypeDao = SearchRoomTypeDAO(Base)
    SearchZoneActionTypeDao = SearchZoneActionTypeDAO(Base)
    SearchZoneTypeDao = SearchZoneTypeDAO(Base)
    SkillLevelDao = SkillLevelDAO(Base)
    SkillPackDao = SkillPackDAO(Base)
    SkillTypeDao = SkillTypeDAO(Base)

    ResourceSvc = ResourceService(ResourceTypeDao, ResourcePackDao, ResourceDropProbabilityDao)
    SkillSvc = SkillService(SkillTypeDao, SkillLevelDao, SkillPackDao)
    ProductionSvc = ProductionService(ProductionTypeDao, ResourceSvc, SkillSvc)
    BuildingSvc = BuildingService(BuildingTypeDao, ProductionSvc)
    SearchRoomSvc = SearchRoomService(SearchRoomActionTypeDao, SearchRoomTypeDao, SearchRoomFillerDao,
                                      SearchRoomBlankDao,
                                      ResourceSvc)

    with open('data/resource_type.yml', encoding='utf8') as f:
        lis = load(f.read(), Loader=FullLoader)['list']
    for el in lis:
        ResourceSvc.get_or_create_resource_type(ResourceType.from_yaml(el))

    with open('data/skill_type.yml', encoding='utf8') as f:
        lis = load(f.read(), Loader=FullLoader)['list']
    for el in lis:
        SkillSvc.get_or_create_skill_type(SkillType.from_yaml(el))

    with open('data/production_type.yml', encoding='utf8') as f:
        lis = load(f.read(), Loader=FullLoader)['list']
    for el in lis:
        ProductionSvc.get_or_create_production_type(ProductionType.from_yaml(el))

    with open('data/building_type.yml', encoding='utf8') as f:
        lis = load(f.read(), Loader=FullLoader)['list']
    for el in lis:
        BuildingSvc.get_or_create_building_type(BuildingType.from_yaml(el))

    with open('data/search_room_type.yml', encoding='utf8') as f:
        lis = load(f.read(), Loader=FullLoader)['list']
    for el in lis:
        SearchRoomSvc.get_or_create_search_room_type(SearchRoomType.from_yaml(el))

    with open('data/search_room_filler.yml', encoding='utf8') as f:
        lis = load(f.read(), Loader=FullLoader)['list']
    for el in lis:
        SearchRoomSvc.get_or_create_search_room_filler(SearchRoomFiller.from_yaml(el))


def only_once_migration():
    BuildingDao = BuildingDAO(Base)
    PersonDao = PersonDAO(Base)
    ProductionDao = ProductionDAO(Base)
    ResourceDao = ResourceDAO(Base)
    SearchRoomActionDao = SearchRoomActionDAO(Base)
    SearchRoomDao = SearchRoomDAO(Base)
    SearchZoneActionDao = SearchZoneActionDAO(Base)
    SearchZoneDao = SearchZoneDAO(Base)
    ShapeMultiPolygonDao = ShapeMultiPolygonDAO(Base)
    ShapePointDao = ShapePointDAO(Base)
    ShapePolygonDao = ShapePolygonDAO(Base)
    ShapeRingDao = ShapeRingDAO(Base)
    SkillDao = SkillDAO(Base)

    ResourceDao.create(resource_type_id=8, quality=100, decay=0, owned=True)
    ResourceDao.create(resource_type_id=9, quality=90, decay=0, owned=True)
    ResourceDao.create(resource_type_id=9, quality=100, decay=0, owned=True)
    ResourceDao.create(resource_type_id=1, quality=90, decay=0, owned=True)

    PersonSvc.generate_person(19.921910, 50.037894)
    PersonSvc.generate_person(19.921710, 50.037894)
    PersonSvc.generate_person(19.921510, 50.037894)
    PersonSvc.generate_person(19.921310, 50.037894)

    PersonSvc.generate_person(19.921310, 50.038194, icon='🧟‍♂️')

    point = (19.921910, 50.037994)
    ring = ring_regular(point, 5, 4, 45)
    multipolygon = MultiPolygon(Polygon(ring))
    multipolygon_record = ShapeSvc.create_multipolygon(multipolygon)
    BuildingDao.create(shape=multipolygon_record)
    point = (19.921710, 50.037994)
    ring = ring_regular(point, 5, 4, 45)
    multipolygon = MultiPolygon(Polygon(ring))
    multipolygon_record = ShapeSvc.create_multipolygon(multipolygon)
    BuildingDao.create(shape=multipolygon_record)

    point = (19.921410, 50.037994)
    ring = ring_regular(point, 10, 10)
    multipolygon = MultiPolygon(Polygon(ring))
    multipolygon_record = ShapeSvc.create_multipolygon(multipolygon)
    SearchRoomSvc.generate_search_room(shape=multipolygon_record, long=point[0], lat=point[1])


if __name__ == '__main__':
    type_migration()
