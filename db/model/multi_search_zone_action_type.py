from .resource_pack import ResourcePack
from .skill_pack import SkillPack


class MultiSearchZoneActionType:
    def __init__(self, name, required_number_of_people, required_skills, required_tools):
        self.name = name
        self.required_number_of_people = required_number_of_people
        self.required_skills = frozenset(required_skills)
        self.required_tools = frozenset(required_tools)

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.required_number_of_people != other.required_number_of_people:
            return False
        if self.required_skills != other.required_skills:
            return False
        if self.required_tools != other.required_tools:
            return False
        return True

    def __hash__(self):
        return (hash(self.name) + hash(self.required_number_of_people) + hash(self.required_skills) +
                hash(self.required_tools))

    @staticmethod
    def from_yaml(yaml):
        el = MultiSearchZoneActionType(name=yaml.get('name'),
                                       required_number_of_people=yaml.get('required_number_of_people'),
                                       required_skills=[SkillPack.from_yaml(el)
                                                        for el in yaml.get('required_skills', [])],
                                       required_tools=[ResourcePack.from_yaml(el)
                                                       for el in yaml.get('required_tools', [])],
                                       )
        return el
