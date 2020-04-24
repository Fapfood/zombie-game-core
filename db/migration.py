from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from yaml import load, FullLoader

from db import ProductionTypeDAO, ResourceTypeDAO, ResourcePackDAO, SkillTypeDAO, SkillLevelDAO, SkillPackDAO, \
    BuildingTypeDAO, ResourceDAO, SkillDAO, PersonDAO, BuildingDAO, SearchZoneDAO, SearchZoneTypeDAO, \
    SearchZoneActionTypeDAO, ResourceDropProbabilityDAO
from db import ShapePointDAO, ShapeRingDAO, ShapePolygonDAO, ShapeMultiPolygonDAO
from db.entity import SkillTypeEntity, ResourceTypeEntity
from service import ProductionService, SkillService, BuildingService, ShapeService, ResourceService, PersonService, \
    SearchZoneService
from service.model.building import BuildingType
from service.model.production import ProductionType
from service.model.search_zone import SearchZoneType
from service.model.shape import Polygon, MultiPolygon
from service.shape_helper import ring_regular


def migration():
    engine = create_engine('sqlite:////Users/matr/dev/zombie-game-core/test.db')
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.session = session

    with open('data/resource_type.yml', encoding='utf8') as f:
        file = load(f.read(), Loader=FullLoader)['list']

    for elem in file:
        if session.query(ResourceTypeEntity).filter_by(name=elem['name']).one_or_none() is None:
            db_elem = ResourceTypeEntity(**elem)
            session.add(db_elem)

    with open('data/skill_type.yml', encoding='utf8') as f:
        file = load(f.read(), Loader=FullLoader)['list']

    for elem in file:
        if session.query(SkillTypeEntity).filter_by(name=elem['name']).one_or_none() is None:
            db_elem = SkillTypeEntity(**elem)
            session.add(db_elem)

    session.commit()
    session.close()

    ShapeSvc = ShapeService(ShapePointDAO(Base), ShapeRingDAO(Base), ShapePolygonDAO(Base), ShapeMultiPolygonDAO(Base))
    SkillSvc = SkillService(SkillTypeDAO(Base), SkillLevelDAO(Base), SkillPackDAO(Base))
    ResourceSvc = ResourceService(ResourceTypeDAO(Base), ResourcePackDAO(Base), ResourceDropProbabilityDAO(Base),
                                  ResourceDAO(Base))
    ProductionSvc = ProductionService(ProductionTypeDAO(Base), ResourceSvc, SkillSvc)
    BuildingSvc = BuildingService(BuildingTypeDAO(Base), ProductionSvc)
    PersonSvc = PersonService(PersonDAO(Base), SkillTypeDAO(Base), SkillDAO(Base))
    SearchZoneSvc = SearchZoneService(SearchZoneActionTypeDAO(Base), SearchZoneTypeDAO(Base), SearchZoneDAO(Base),
                                      ResourceSvc, SkillSvc)

    with open('data/production_type.yml', encoding='utf8') as f:
        file = load(f.read(), Loader=FullLoader)['list']

    for elem in file:
        ProductionSvc.get_or_create_production_type(ProductionType.from_yaml(elem))

    with open('data/building_type.yml', encoding='utf8') as f:
        file = load(f.read(), Loader=FullLoader)['list']

    for elem in file:
        BuildingSvc.get_or_create_building_type(BuildingType.from_yaml(elem))

    with open('data/search_zone_type.yml', encoding='utf8') as f:
        file = load(f.read(), Loader=FullLoader)['list']

    for elem in file:
        SearchZoneSvc.get_or_create_search_zone_type(SearchZoneType.from_yaml(elem))

    def only_once_migration():
        ResourceDao = ResourceDAO(Base)
        ResourceDao.create(resource_type_id=8, quality=100, decay=0, owned=True)
        ResourceDao.create(resource_type_id=9, quality=90, decay=0, owned=True)
        ResourceDao.create(resource_type_id=9, quality=100, decay=0, owned=True)
        ResourceDao.create(resource_type_id=1, quality=90, decay=0, owned=True)

        PersonSvc.generate_person(19.921910, 50.037894)
        PersonSvc.generate_person(19.921710, 50.037894)
        PersonSvc.generate_person(19.921510, 50.037894)
        PersonSvc.generate_person(19.921310, 50.037894)

        PersonSvc.generate_person(19.921310, 50.038194, icon='🧟‍♂️')

        BuildingDao = BuildingDAO(Base)
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
        SearchZoneSvc.generate_search_zone(shape=multipolygon_record, long=point[0], lat=point[1])

    only_once_migration()


if __name__ == '__main__':
    migration()
