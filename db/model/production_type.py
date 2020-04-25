from .resource_pack import ResourcePack
from .skill_pack import SkillPack


class ProductionType:
    def __init__(self, name, minutes, required_skills, required_tools,
                 from_resources, to_resources_successful, to_resources_interrupted):
        self.name = name
        self.minutes = minutes
        self.required_skills = frozenset(required_skills)
        self.required_tools = frozenset(required_tools)
        self.from_resources = frozenset(from_resources)
        self.to_resources_successful = frozenset(to_resources_successful)
        self.to_resources_interrupted = frozenset(to_resources_interrupted)

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.minutes != other.minutes:
            return False
        if self.required_skills != other.required_skills:
            return False
        if self.required_tools != other.required_tools:
            return False
        if self.from_resources != other.from_resources:
            return False
        if self.to_resources_successful != other.to_resources_successful:
            return False
        if self.to_resources_interrupted != other.to_resources_interrupted:
            return False
        return True

    def __hash__(self):
        return (hash(self.name) + hash(self.minutes) + hash(self.required_skills) + hash(self.required_tools) +
                hash(self.from_resources) + hash(self.to_resources_successful) + hash(self.to_resources_interrupted))

    @staticmethod
    def from_yaml(yaml):
        el = ProductionType(name=yaml.get('name'),
                            minutes=yaml.get('minutes'),
                            required_skills=[SkillPack.from_yaml(el) for el in yaml.get('required_skills', [])],
                            required_tools=[ResourcePack.from_yaml(el) for el in yaml.get('required_tools', [])],
                            from_resources=[ResourcePack.from_yaml(el) for el in yaml.get('from_resources', [])],
                            to_resources_successful=[ResourcePack.from_yaml(el)
                                                     for el in yaml.get('to_resources_successful', [])],
                            to_resources_interrupted=[ResourcePack.from_yaml(el)
                                                      for el in yaml.get('to_resources_interrupted', [])],
                            )
        return el
