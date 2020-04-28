from db import BuildingTypeDAO
from .production import ProductionService


class BuildingService:
    def __init__(self,
                 building_type_dao: BuildingTypeDAO,
                 production_service: ProductionService,
                 ):
        self.building_type_dao = building_type_dao
        self.production_service = production_service

    def get_or_create_building_types(self, lis):
        res = []
        for el in lis:
            entity = self.get_or_create_building_type(el)
            res.append(entity)
        return res

    def get_or_create_building_type(self, el):
        entity = self.building_type_dao.read_by_name(name=el.name)
        if entity is None:
            available_productions = self.production_service.get_or_create_production_types(el.available_productions)
            entity = self.building_type_dao.create(name=el.name,
                                                   max_workers=el.max_workers,
                                                   worker_icon_male=el.worker_icon_male,
                                                   worker_icon_female=el.worker_icon_female,
                                                   available_productions=available_productions,
                                                   )
        return entity
