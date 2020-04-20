from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from yaml import load

from db import ProductionTypeDAO, ResourceTypeDAO, ResourcePackDAO, SkillTypeDAO, SkillLevelDAO, SkillPackDAO, \
    BuildingTypeDAO
from db.entity import SkillTypeEntity, ResourceTypeEntity
from service import ProductionService, SkillService, BuildingService
from service.model.building import BuildingType
from service.model.production import ProductionType


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

    SkillSvc = SkillService(SkillTypeDAO(Base), SkillLevelDAO(Base), SkillPackDAO(Base))
    ProductionSvc = ProductionService(ProductionTypeDAO(Base), ResourceTypeDAO(Base), ResourcePackDAO(Base), SkillSvc)
    BuildingSvc = BuildingService(BuildingTypeDAO(Base), ProductionSvc)

    with open('data/production_type.yml', encoding='utf8') as f:
        file = load(f.read())['list']

    for elem in file:
        ProductionSvc.get_or_create_production_type(ProductionType.from_yaml(elem))

    with open('data/building_type.yml', encoding='utf8') as f:
        file = load(f.read())['list']

    for elem in file:
        BuildingSvc.get_or_create_building_type(BuildingType.from_yaml(elem))


if __name__ == '__main__':
    migration()
