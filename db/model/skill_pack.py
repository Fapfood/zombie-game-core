from .skill_level import SkillLevel


class SkillPack:
    def __init__(self, name, skills):
        self.name = name
        self.skills = frozenset(skills)

    def __eq__(self, other):
        return self.skills == other.skills

    def __hash__(self):
        return hash(self.name) + hash(self.skills)

    @staticmethod
    def from_yaml(yaml):
        el = SkillPack(name=yaml.get('name'),
                       skills=[SkillLevel.from_yaml(el) for el in yaml.get('skills', [])],
                       )
        return el
