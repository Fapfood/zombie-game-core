from .skill_type import SkillType


class SkillLevel:
    def __init__(self, name, type, level):
        self.name = name
        self.type = type
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type and self.level == other.level

    def __hash__(self):
        return hash(self.name) + hash(self.type) + hash(self.level)

    @staticmethod
    def from_yaml(yaml):
        el = SkillLevel(name=yaml.get('name'),
                        type=SkillType.from_yaml(yaml.get('type')),
                        level=yaml.get('level'),
                        )
        return el
