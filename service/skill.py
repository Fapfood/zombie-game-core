from random import sample

from zombie_game_type import skill_static_service

from service.person_helper import generate_levels


class SkillService:
    def __init__(self, skill_dao):
        self.skill_dao = skill_dao

    def generate_skills(self, n, bonuses):
        res = []
        skills = self._get_sample_skill_types(n)
        levels = generate_levels(n, bonuses)
        for skl, lv in zip(skills, levels):
            skill = self.skill_dao.create(type=skl, level=lv)
            res.append(skill)
        return res

    @staticmethod
    def _get_sample_skill_types(n):
        all_types = skill_static_service.get_all_names()
        skills = sample(all_types, n)
        return skills

    @staticmethod
    def compare_packs(required, owned):
        satisfied_skills_count = 0
        missing_levels = 0
        additional_levels = 0
        for skill_1 in required:
            for skill_2 in owned:
                if skill_1.type.name == skill_2.type.name:
                    satisfied_skills_count += 1
                    if skill_2.level > skill_1.level:
                        diff = skill_2.level - skill_1.level
                        additional_levels += diff
                    if skill_1.level > skill_2.level:
                        diff = skill_1.level - skill_2.level
                        missing_levels += diff

        if satisfied_skills_count < len(required):
            return False
        if missing_levels > 0:
            return False
        return True
