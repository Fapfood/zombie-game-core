from db import SearchRoomActionTypeDAO
from db import SearchRoomBlankDAO
from db import SearchRoomFillerDAO
from db import SearchRoomTypeDAO
from .resource import ResourceService


class SearchRoomService:
    def __init__(self,
                 search_room_action_type_dao: SearchRoomActionTypeDAO,
                 search_room_type_dao: SearchRoomTypeDAO,
                 search_room_filler_dao: SearchRoomFillerDAO,
                 search_room_blank_dao: SearchRoomBlankDAO,
                 resource_service: ResourceService,
                 ):
        self.search_room_action_type_dao = search_room_action_type_dao
        self.search_room_type_dao = search_room_type_dao
        self.search_room_filler_dao = search_room_filler_dao
        self.search_room_blank_dao = search_room_blank_dao
        self.resource_service = resource_service

    def get_or_create_search_room_fillers(self, lis):
        res = []
        for el in lis:
            entity = self.get_or_create_search_room_filler(el)
            res.append(entity)
        return res

    def get_or_create_search_room_filler(self, el):
        entity = self.search_room_filler_dao.read_by_name(name=el.name)
        if entity is None:
            type = self.get_or_create_search_room_type(el.type)
            resource_drop_table = self.resource_service.get_or_create_resource_drop_probabilities(
                el.resource_drop_table)
            search_room_action_types = self.get_or_create_search_room_action_types(el.search_room_action_types)
            entity = self.search_room_filler_dao.create(name=el.name,
                                                        type=type,
                                                        resource_drop_table=resource_drop_table,
                                                        search_room_action_types=search_room_action_types,
                                                        )
        return entity

    def get_or_create_search_room_types(self, lis):
        res = []
        for el in lis:
            entity = self.get_or_create_search_room_type(el)
            res.append(entity)
        return res

    def get_or_create_search_room_type(self, el):
        entity = self.search_room_type_dao.read_by_name(name=el.name)
        if entity is None:
            entity = self.search_room_type_dao.create(name=el.name)
        return entity

    def get_or_create_search_room_action_types(self, lis):
        res = []
        for el in lis:
            entity = self.get_or_create_search_room_action_type(el)
            res.append(entity)
        return res

    def get_or_create_search_room_action_type(self, el):
        entity = self.search_room_action_type_dao.read_by_name(name=el.name)
        if entity is None:
            entity = self.search_room_action_type_dao.create(name=el.name, probability=el.probability)
        return entity
