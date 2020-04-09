class Production:
    def __init__(self, name, minutes, required_skills, required_tools,
                 from_resources, to_resources_successful, to_resources_interrupted):
        self.name = name
        self.minutes = minutes
        self.required_skills = required_skills
        self.required_tools = required_tools
        self.from_resources = from_resources
        self.to_resources_successful = to_resources_successful
        self.to_resources_interrupted = to_resources_interrupted

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.minutes != other.minutes:
            return False
        if len(self.required_skills) != len(other.required_skills):
            return False
        if set(self.required_skills) != set(other.required_skills):
            return False
        if len(self.required_tools) != len(other.required_tools):
            return False
        if set(self.required_tools) != set(other.required_tools):
            return False
        if len(self.from_resources) != len(other.from_resources):
            return False
        if set(self.from_resources) != set(other.from_resources):
            return False
        if len(self.to_resources_successful) != len(other.to_resources_successful):
            return False
        if set(self.to_resources_successful) != set(other.to_resources_successful):
            return False
        if len(self.to_resources_interrupted) != len(other.to_resources_interrupted):
            return False
        if set(self.to_resources_interrupted) != set(other.to_resources_interrupted):
            return False
        return True

    @staticmethod
    def from_yaml(yaml):
        p = Production(name=yaml['name'],
                       minutes=yaml['minutes'],
                       required_skills=[SkillLevel.from_yaml(e) for e in yaml['required_skills']],
                       required_tools=[ResourcePack.from_yaml(e) for e in yaml['required_tools']],
                       from_resources=[ResourcePack.from_yaml(e) for e in yaml['from_resources']],
                       to_resources_successful=[ResourcePack.from_yaml(e) for e in yaml['to_resources_successful']],
                       to_resources_interrupted=[ResourcePack.from_yaml(e) for e in yaml['to_resources_interrupted']],
                       )
        return p


class ResourcePack:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __eq__(self, other):
        return self.name == other.name and self.quantity == other.quantity

    @staticmethod
    def from_yaml(yaml):
        return ResourcePack(name=yaml['type.name'], quantity=yaml['quantity'])


class SkillLevel:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.level == other.level

    @staticmethod
    def from_yaml(yaml):
        return SkillLevel(name=yaml['type.name'], level=yaml['level'])
