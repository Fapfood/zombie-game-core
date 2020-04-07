from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.entity import BuildingTypeEntity, ProductionEntity, \
    ResourcePackEntity, ResourceTypeEntity, \
    SearchZoneTypeEntity, SkillLevelEntity, SkillTypeEntity


def migration():
    engine = create_engine('sqlite:////Users/matr/dev/zombie-game-core/test.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    skill_type_1 = SkillTypeEntity(name='Ciesielstwo')
    session.add(skill_type_1)
    skill_type_2 = SkillTypeEntity(name='Stolarstwo')
    session.add(skill_type_2)
    skill_type_3 = SkillTypeEntity(name='Generic1')
    session.add(skill_type_3)
    skill_type_4 = SkillTypeEntity(name='Generic2')
    session.add(skill_type_4)
    skill_type_5 = SkillTypeEntity(name='Generic3')
    session.add(skill_type_5)
    skill_type_6 = SkillTypeEntity(name='Generic4')
    session.add(skill_type_6)

    skill_level_1 = SkillLevelEntity(type=skill_type_1, level=1)
    session.add(skill_level_1)
    skill_level_2 = SkillLevelEntity(type=skill_type_1, level=2)
    session.add(skill_level_2)
    skill_level_3 = SkillLevelEntity(type=skill_type_1, level=3)
    session.add(skill_level_3)

    skill_level_4 = SkillLevelEntity(type=skill_type_2, level=1)
    session.add(skill_level_4)
    skill_level_5 = SkillLevelEntity(type=skill_type_2, level=2)
    session.add(skill_level_5)
    skill_level_6 = SkillLevelEntity(type=skill_type_2, level=3)
    session.add(skill_level_6)

    resource_type_1 = ResourceTypeEntity(name='Kloda')
    session.add(resource_type_1)
    resource_type_2 = ResourceTypeEntity(name='Deska')
    session.add(resource_type_2)

    resource_pack_1 = ResourcePackEntity(type=resource_type_1, quantity=1)
    session.add(resource_pack_1)
    resource_pack_2 = ResourcePackEntity(type=resource_type_2, quantity=2)
    session.add(resource_pack_2)

    production_1 = ProductionEntity(minutes=15, required_skills=[skill_level_2],
                                    from_resources=[resource_pack_1],
                                    to_resources_successful=[resource_pack_2],
                                    to_resources_interrupted=[])
    session.add(production_1)

    building_type_1 = BuildingTypeEntity(name='Sawmill', max_workers=1,
                                         worker_icon_male='👷‍♂️', worker_icon_female='👷‍♀️',
                                         available_productions=[production_1])
    session.add(building_type_1)

    search_zone_type_1 = SearchZoneTypeEntity(name='Car')
    session.add(search_zone_type_1)

    session.commit()
    session.close()


if __name__ == '__main__':
    migration()
