from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from yaml import load

from db import ProductionTypeDAO, ResourceTypeDAO, ResourcePackDAO, SkillTypeDAO, SkillLevelDAO, SkillPackDAO, \
    BuildingTypeDAO, ResourceDAO, SkillDAO, PersonDAO, BuildingDAO
from db import ShapePointDAO, ShapeRingDAO, ShapePolygonDAO, ShapeMultiPolygonDAO
from db.entity import SkillTypeEntity, ResourceTypeEntity
from service import ProductionService, SkillService, BuildingService, ShapeService, ResourceService, PersonService
from service.model.building import BuildingType
from service.model.production import ProductionType
from service.model.shape import Polygon, MultiPolygon
from service.shape_helper import ring_regular


def migration():
    engine = create_engine('sqlite:////Users/matr/dev/zombie-game-core/test.db')
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.session = session

    with open('data/resource_type.yml', encoding='utf8') as f:
        file = load(f.read())['list']

    for elem in file:
        if session.query(ResourceTypeEntity).filter_by(name=elem['name']).one_or_none() is None:
            db_elem = ResourceTypeEntity(**elem)
            session.add(db_elem)

    with open('data/skill_type.yml', encoding='utf8') as f:
        file = load(f.read())['list']

    for elem in file:
        if session.query(SkillTypeEntity).filter_by(name=elem['name']).one_or_none() is None:
            db_elem = SkillTypeEntity(**elem)
            session.add(db_elem)

    session.commit()
    session.close()

    ShapeSvc = ShapeService(ShapePointDAO(Base), ShapeRingDAO(Base), ShapePolygonDAO(Base), ShapeMultiPolygonDAO(Base))
    SkillSvc = SkillService(SkillTypeDAO(Base), SkillLevelDAO(Base), SkillPackDAO(Base))
    ResourceSvc = ResourceService(ResourceTypeDAO(Base), ResourcePackDAO(Base))
    ProductionSvc = ProductionService(ProductionTypeDAO(Base), ResourceSvc, SkillSvc)
    BuildingSvc = BuildingService(BuildingTypeDAO(Base), ProductionSvc)
    PersonSvc = PersonService(PersonDAO(Base), SkillTypeDAO(Base), SkillDAO(Base))

    with open('data/production_type.yml', encoding='utf8') as f:
        file = load(f.read())['list']

    for elem in file:
        ProductionSvc.get_or_create_production_type(ProductionType.from_yaml(elem))

    with open('data/building_type.yml', encoding='utf8') as f:
        file = load(f.read())['list']

    for elem in file:
        BuildingSvc.get_or_create_building_type(BuildingType.from_yaml(elem))

    # ResourceDao = ResourceDAO(Base)
    # ResourceDao.create(resource_type_id=8, quality=100, decay=0)
    # ResourceDao.create(resource_type_id=9, quality=90, decay=0)
    # ResourceDao.create(resource_type_id=9, quality=100, decay=0)
    # ResourceDao.create(resource_type_id=1, quality=90, decay=0)
    # PersonSvc.generate_person(19.921910, 50.037894)
    # PersonSvc.generate_person(19.921710, 50.037894)
    # PersonSvc.generate_person(19.921510, 50.037894)
    # PersonSvc.generate_person(19.921310, 50.037894)
    # BuildingDao = BuildingDAO(Base)
    # ring = ring_regular((19.921910, 50.037994), 5, 4, 45)
    # multipolygon = MultiPolygon(Polygon(ring))
    # multipolygon_record = ShapeSvc.create_multipolygon(multipolygon)
    # BuildingDao.create(shape=multipolygon_record)
    # ring = ring_regular((19.921710, 50.037994), 5, 4, 45)
    # multipolygon = MultiPolygon(Polygon(ring))
    # multipolygon_record = ShapeSvc.create_multipolygon(multipolygon)
    # BuildingDao.create(shape=multipolygon_record)


if __name__ == '__main__':
    migration()
