from service.person_helper import (generate_gender, generate_first_name, generate_last_name,
                                   generate_age, generate_attitude, generate_icon)


class PersonService:
    def __init__(self, person_dao, skill_svc):
        self.person_dao = person_dao
        self.skill_svc = skill_svc

    def generate_person(self, long, lat, icon=None):
        gender = generate_gender()
        age = generate_age()
        skills = self.skill_svc.generate_skills(3, (2, 1))
        icon = icon if icon is not None else generate_icon(gender, age)
        person = self.person_dao.create(first_name=generate_first_name(gender),
                                        last_name=generate_last_name(),
                                        gender=gender,
                                        age=age,
                                        base_icon=icon,
                                        attitude=generate_attitude(),
                                        long=long,
                                        lat=lat,
                                        skills=skills,
                                        )
        return person
