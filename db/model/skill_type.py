class SkillType:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    @staticmethod
    def from_yaml(yaml):
        el = SkillType(name=yaml.get('name'))
        return el
