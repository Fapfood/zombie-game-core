from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.entity import BuildingTypeEntity, PersonEntity, ProductionEntity, \
    ResourceEntity, ResourcePackEntity, ResourceTypeEntity, SkillLevelEntity, SkillTypeEntity


def migration():
    engine = create_engine('sqlite:////Users/matr/dev/zombie-game-core/test.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    skill_type_1 = SkillTypeEntity(name='Ciesielstwo')
    session.add(skill_type_1)
    skill_type_2 = SkillTypeEntity(name='Stolarstwo')
    session.add(skill_type_2)

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

    person_1 = PersonEntity(name='Kamil', owned_skills=[skill_level_1])
    session.add(person_1)
    person_2 = PersonEntity(name='Maciej', owned_skills=[skill_level_2])
    session.add(person_2)

    resource_type_1 = ResourceTypeEntity(name='Kloda')
    session.add(resource_type_1)
    resource_type_2 = ResourceTypeEntity(name='Deska')
    session.add(resource_type_2)

    resource_1 = ResourceEntity(type=resource_type_1)
    session.add(resource_1)
    resource_2 = ResourceEntity(type=resource_type_2)
    session.add(resource_2)

    resource_pack_1 = ResourcePackEntity(type=resource_type_1, quantity=1)
    session.add(resource_pack_1)
    resource_pack_2 = ResourcePackEntity(type=resource_type_2, quantity=2)
    session.add(resource_pack_2)

    production_1 = ProductionEntity(minutes=15, required_skills=[skill_level_2],
                                    from_resources=[resource_pack_1],
                                    to_resources=[resource_pack_2])
    session.add(production_1)

    building_type_1 = BuildingTypeEntity(name='Tartak', max_workers=1, available_productions=[production_1])
    session.add(building_type_1)

    session.commit()
    session.close()


if __name__ == '__main__':
    migration()
