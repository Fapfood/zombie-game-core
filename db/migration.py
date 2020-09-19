from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from zombie_game_type import resource_static_service

from db.dao import BuildingDAO
from db.dao import BuildingRoomDAO
from db.dao import PersonDAO
from db.dao import ResourceDAO
from db.dao import ShapeMultiPolygonDAO
from db.dao import ShapePointDAO
from db.dao import ShapePolygonDAO
from db.dao import ShapeRingDAO
from db.dao import SkillDAO
from db.dao import ZoneActionDAO
from db.dao import ZoneDAO
from db.dao import ZoneRoomActionDAO
from db.dao import ZoneRoomDAO
from openstreetmap import open_street_map_building
from service import BuildingRoomService
from service import BuildingService
from service import PersonService
from service import ResourceService
from service import ShapeService
from service import SkillService
from service import ZoneRoomService
from service.shape_helper import Polygon, MultiPolygon, ring_regular

DB_STRING = 'sqlite:////Users/matr/dev/zombie-game-core/test.db'


def only_once_migration():
    engine = create_engine(DB_STRING)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()
    Base.session = session

    BuildingDao = BuildingDAO(Base)
    BuildingRoomDao = BuildingRoomDAO(Base)
    PersonDao = PersonDAO(Base)
    ResourceDao = ResourceDAO(Base)
    ZoneRoomActionDao = ZoneRoomActionDAO(Base)
    ZoneRoomDao = ZoneRoomDAO(Base)
    SearchZoneActionDao = ZoneActionDAO(Base)
    SearchZoneDao = ZoneDAO(Base)
    ShapeMultiPolygonDao = ShapeMultiPolygonDAO(Base)
    ShapePointDao = ShapePointDAO(Base)
    ShapePolygonDao = ShapePolygonDAO(Base)
    ShapeRingDao = ShapeRingDAO(Base)
    SkillDao = SkillDAO(Base)

    SkillSvc = SkillService(SkillDao)
    PersonSvc = PersonService(PersonDao, SkillSvc)
    BuildingRoomSvc = BuildingRoomService(BuildingRoomDao, PersonSvc)
    ShapeSvc = ShapeService(ShapePointDao, ShapeRingDao, ShapePolygonDao, ShapeMultiPolygonDao)
    BuildingSvc = BuildingService(BuildingDao, BuildingRoomSvc, ShapeSvc)
    ResourceSvc = ResourceService(ResourceDao)
    # ProductionSvc = ProductionService(ProductionDao, PersonSvc, ResourceSvc)
    ZoneRoomSvc = ZoneRoomService(ZoneRoomDao, ResourceSvc)

    ResourceSvc.generate_resource(resource_static_service.get_by_name('log'), owned=True)
    ResourceSvc.generate_resource(resource_static_service.get_by_name('log'), owned=True)
    ResourceSvc.generate_resource(resource_static_service.get_by_name('saw'), owned=True)
    ResourceSvc.generate_resource(resource_static_service.get_by_name('battery'), owned=True)

    PersonSvc.generate_person(19.922110, 50.037794, owned=True)
    PersonSvc.generate_person(19.921910, 50.037794, owned=True)
    PersonSvc.generate_person(19.921710, 50.037794, owned=True)
    PersonSvc.generate_person(19.921510, 50.037794, owned=True)

    PersonSvc.generate_person(19.921310, 50.038194, icon='🧟‍♂️')

    point = (19.921910, 50.037794)
    ring = ring_regular(point, 5, 4, 45)
    multipolygon = MultiPolygon(Polygon(ring))
    BuildingSvc.create(multipolygon=multipolygon)

    for way_id in ['233371478', '386876478', '386876425']:
        ring = open_street_map_building(way_id)
        multipolygon = MultiPolygon(Polygon(ring))
        BuildingSvc.create(multipolygon=multipolygon)

    point = (19.921610, 50.038194)
    ring = ring_regular(point, 10, 10)
    multipolygon = MultiPolygon(Polygon(ring))
    multipolygon_record = ShapeSvc.create_multipolygon(multipolygon)
    ZoneRoomSvc.generate_zone_room(shape=multipolygon_record, long=point[0], lat=point[1])

    for way_id in ['233371463', '233371452', '233371446', '233371447', '233371443']:
        ring = open_street_map_building(way_id)
        multipolygon = MultiPolygon(Polygon(ring))
        point = multipolygon.shape.centroid.coords[0]
        multipolygon_record = ShapeSvc.create_multipolygon(multipolygon)
        ZoneRoomSvc.generate_zone_room(shape=multipolygon_record, long=point[0], lat=point[1])


if __name__ == '__main__':
    only_once_migration()
