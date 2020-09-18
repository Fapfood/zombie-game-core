from random import random, randint


class ResourceService:
    def __init__(self, resource_dao):
        self.resource_dao = resource_dao

    def generate_resources(self, drop_probability_lis):
        res = []
        for el in drop_probability_lis:
            if random() <= el.probability:
                entity = self.generate_resource(el.resource)
                res.append(entity)
        return res

    def generate_resource(self, type, owned=False):
        owned = owned
        available = owned
        quality = randint(50, 100)
        decay = randint(0, 50)
        entity = self.resource_dao.create(available=available, owned=owned, quality=quality, decay=decay,
                                          type=type.name, icon=type.icon)
        return entity

    @staticmethod
    def compare_packs(required, owned):
        required_ids = [r.type.id for r in required for _ in range(r.quantity)]

        if len(set([r.id for r in owned])) < len(required_ids):
            return False

        for el in owned:
            required_ids.remove(el.type.id)
        if len(required_ids) > 0:
            return False

        return True
