from db import SkillLevelDAO
from db import SkillPackDAO
from db import SkillTypeDAO


class SkillService:
    def __init__(self,
                 skill_type_dao: SkillTypeDAO,
                 skill_level_dao: SkillLevelDAO,
                 skill_pack_dao: SkillPackDAO,
                 ):
        self.skill_type_dao = skill_type_dao
        self.skill_level_dao = skill_level_dao
        self.skill_pack_dao = skill_pack_dao

    def get_or_create_skill_packs(self, lis):
        res = []
        for el in lis:
            entity = self.get_or_create_skill_pack(el)
            res.append(entity)
        return res

    def get_or_create_skill_pack(self, el):
        entity = self.skill_pack_dao.read_by_name(name=el.name)
        if entity is None:
            skills = self.get_or_create_skill_levels(el.skills)
            entity = self.skill_pack_dao.create(name=el.name, skills=skills)
        return entity

    def get_or_create_skill_levels(self, lis):
        res = []
        for el in lis:
            entity = self.get_or_create_skill_level(el)
            res.append(entity)
        return res

    def get_or_create_skill_level(self, el):
        entity = self.skill_level_dao.read_by_name(name=el.name)
        if entity is None:
            type = self.get_or_create_skill_type(el.type)
            entity = self.skill_level_dao.create(name=el.name, type=type, level=el.level)
        return entity

    def get_or_create_skill_types(self, lis):
        res = []
        for el in lis:
            entity = self.get_or_create_skill_type(el)
            res.append(entity)
        return res

    def get_or_create_skill_type(self, el):
        entity = self.skill_type_dao.read_by_name(name=el.name)
        if entity is None:
            entity = self.skill_type_dao.create(name=el.name)
        return entity
