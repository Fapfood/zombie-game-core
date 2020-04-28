from db import ResourceDropProbabilityDAO
from db import ResourcePackDAO
from db import ResourceTypeDAO


class ResourceService:
    def __init__(self,
                 resource_type_dao: ResourceTypeDAO,
                 resource_pack_dao: ResourcePackDAO,
                 resource_drop_probability_dao: ResourceDropProbabilityDAO,
                 ):
        self.resource_type_dao = resource_type_dao
        self.resource_pack_dao = resource_pack_dao
        self.resource_drop_probability_dao = resource_drop_probability_dao

    def get_or_create_resource_drop_probabilities(self, lis):
        res = []
        for el in lis:
            entity = self.get_or_create_resource_drop_probability(el)
            res.append(entity)
        return res

    def get_or_create_resource_drop_probability(self, el):
        entity = self.resource_drop_probability_dao.read_by_name(name=el.name)
        if entity is None:
            type = self.get_or_create_resource_type(el.type)
            entity = self.resource_drop_probability_dao.create(name=el.name, type=type, probability=el.probability)
        return entity

    def get_or_create_resource_packs(self, lis):
        res = []
        for el in lis:
            entity = self.get_or_create_resource_pack(el)
            res.append(entity)
        return res

    def get_or_create_resource_pack(self, el):
        entity = self.resource_pack_dao.read_by_name(name=el.name)
        if entity is None:
            type = self.get_or_create_resource_type(el.type)
            entity = self.resource_pack_dao.create(name=el.name, type=type, quantity=el.quantity)
        return entity

    def get_or_create_resource_types(self, lis):
        res = []
        for el in lis:
            entity = self.get_or_create_resource_type(el)
            res.append(entity)
        return res

    def get_or_create_resource_type(self, el):
        entity = self.resource_type_dao.read_by_name(name=el.name)
        if entity is None:
            entity = self.resource_type_dao.create(name=el.name)
        return entity
