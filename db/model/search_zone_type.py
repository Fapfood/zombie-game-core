from .resource_drop_probability import ResourceDropProbability
from .search_zone_action_type import SearchZoneActionType


class SearchZoneType:
    def __init__(self, name, resource_drop_table, search_zone_action_types):
        self.name = name
        self.resource_drop_table = frozenset(resource_drop_table)
        self.search_zone_action_types = frozenset(search_zone_action_types)

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.resource_drop_table != other.resource_drop_table:
            return False
        if self.search_zone_action_types != other.search_zone_action_types:
            return False
        return True

    def __hash__(self):
        return hash(self.name) + hash(self.resource_drop_table) + hash(self.search_zone_action_types)

    @staticmethod
    def from_yaml(yaml):
        el = SearchZoneType(name=yaml.get('name'),
                            resource_drop_table=[ResourceDropProbability.from_yaml(el)
                                                 for el in yaml.get('resource_drop_table', [])],
                            search_zone_action_types=[SearchZoneActionType.from_yaml(el)
                                                      for el in yaml.get('search_zone_action_types', [])],
                            )
        return el
