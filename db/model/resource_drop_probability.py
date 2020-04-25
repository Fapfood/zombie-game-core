from .resource_type import ResourceType


class ResourceDropProbability:
    def __init__(self, name, type, probability):
        self.name = name
        self.type = type
        self.probability = probability

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type and self.probability == other.probability

    def __hash__(self):
        return hash(self.name) + hash(self.type) + hash(self.probability)

    @staticmethod
    def from_yaml(yaml):
        el = ResourceDropProbability(name=yaml.get('name'),
                                     type=ResourceType.from_yaml(yaml.get('type')),
                                     probability=yaml.get('probability'),
                                     )
        return el
