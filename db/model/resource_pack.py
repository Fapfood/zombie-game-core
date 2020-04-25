from .resource_type import ResourceType


class ResourcePack:
    def __init__(self, name, type, quantity):
        self.name = name
        self.type = type
        self.quantity = quantity

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type and self.quantity == other.quantity

    def __hash__(self):
        return hash(self.name) + hash(self.type) + hash(self.quantity)

    @staticmethod
    def from_yaml(yaml):
        el = ResourcePack(name=yaml.get('name'),
                          type=ResourceType.from_yaml(yaml.get('type')),
                          quantity=yaml.get('quantity'),
                          )
        return el
