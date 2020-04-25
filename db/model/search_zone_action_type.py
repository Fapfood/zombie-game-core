class SearchZoneActionType:
    def __init__(self, name, probability):
        self.name = name
        self.probability = probability

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.probability != other.probability:
            return False
        return True

    def __hash__(self):
        return hash(self.name) + hash(self.probability)

    @staticmethod
    def from_yaml(yaml):
        el = SearchZoneActionType(name=yaml.get('name'), probability=yaml.get('probability'))
        return el
