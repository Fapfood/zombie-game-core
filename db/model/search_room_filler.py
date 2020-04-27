from .resource_drop_probability import ResourceDropProbability
from .search_room_action_type import SearchRoomActionType
from .search_room_type import SearchRoomType


class SearchRoomFiller:
    def __init__(self, name, type, resource_drop_table, search_room_action_types):
        self.name = name
        self.type = type
        self.resource_drop_table = frozenset(resource_drop_table)
        self.search_room_action_types = frozenset(search_room_action_types)

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.type != other.type:
            return False
        if self.resource_drop_table != other.resource_drop_table:
            return False
        if self.search_room_action_types != other.search_room_action_types:
            return False
        return True

    def __hash__(self):
        return hash(self.name) + hash(self.type) + hash(self.resource_drop_table) + hash(self.search_room_action_types)

    @staticmethod
    def from_yaml(yaml):
        el = SearchRoomFiller(name=yaml.get('name'),
                              type=SearchRoomType.from_yaml(yaml.get('type')),
                              resource_drop_table=[ResourceDropProbability.from_yaml(el)
                                                   for el in yaml.get('resource_drop_table', [])],
                              search_room_action_types=[SearchRoomActionType.from_yaml(el)
                                                        for el in yaml.get('search_room_action_types', [])],
                              )
        return el
