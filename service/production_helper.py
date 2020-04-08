class Production:
    def __init__(self, minutes, required_skills, required_tools,
                 from_resources, to_resources_successful, to_resources_interrupted):
        self.minutes = minutes
        self.required_skills = required_skills
        self.required_tools = required_tools
        self.from_resources = from_resources
        self.to_resources_successful = to_resources_successful
        self.to_resources_interrupted = to_resources_interrupted

    def __eq__(self, other):
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


class ResourcePack:
    def __init__(self, type, quantity):
        self.type = type
        self.quantity = quantity

    def __eq__(self, other):
        return self.type == other.type and self.quantity == other.quantity


class SkillLevel:
    def __init__(self, type, level):
        self.type = type
        self.level = level

    def __eq__(self, other):
        return self.type == other.type and self.level == other.level
