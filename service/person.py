from random import choice

from service.person_helper import generate_gender, generate_first_name, generate_last_name, generate_attitude, \
    generate_levels


class PersonService:
    def __init__(self, personDao, skillTypeDao, skillLevelDao):
        self.personDao = personDao
        self.skillTypeDao = skillTypeDao
        self.skillLevelDao = skillLevelDao

    def create_person(self):
        gender = generate_gender()
        person = self.personDao.create(first_name=generate_first_name(gender),
                                       last_name=generate_last_name(),
                                       gender=gender,
                                       attitude=generate_attitude(),
                                       owned_skills=self._create_skill_levels(3, (2, 1)))
        return person

    def _create_skill_levels(self, n, bonuses):
        skill_levels = []
        skills = self._get_different_skills(n)
        levels = generate_levels(n, bonuses)
        for skl, lv in zip(skills, levels):
            skill_level = self.skillLevelDao.read_by_type_id_and_level(skl.id, lv)
            if skill_level is None:
                skill_level = self.skillLevelDao.create(type=skl, level=lv)
            skill_levels.append(skill_level)
        return skill_levels

    def _get_different_skills(self, n):
        all_types = self.skillTypeDao.read_all()
        skills = []
        for _ in range(n):
            while True:
                skill = choice(all_types)
                if skill not in skills:
                    skills.append(skill)
                    break
        return skills
