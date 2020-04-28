from db import ProductionTypeDAO
from .resource import ResourceService
from .skill import SkillService


class ProductionService:
    def __init__(self,
                 production_type_dao: ProductionTypeDAO,
                 resource_service: ResourceService,
                 skill_service: SkillService,
                 ):
        self.production_type_dao = production_type_dao
        self.resource_service = resource_service
        self.skill_service = skill_service

    def get_or_create_production_types(self, lis):
        res = []
        for el in lis:
            entity = self.get_or_create_production_type(el)
            res.append(entity)
        return res

    def get_or_create_production_type(self, el):
        entity = self.production_type_dao.read_by_name(name=el.name)
        if entity is None:
            required_skills = self.skill_service.get_or_create_skill_packs(el.required_skills)
            required_tools = self.resource_service.get_or_create_resource_packs(el.required_tools)
            from_resources = self.resource_service.get_or_create_resource_packs(el.from_resources)
            to_resources_successful = self.resource_service.get_or_create_resource_packs(el.to_resources_successful)
            to_resources_interrupted = self.resource_service.get_or_create_resource_packs(el.to_resources_interrupted)
            entity = self.production_type_dao.create(name=el.name,
                                                     minutes=el.minutes,
                                                     required_skills=required_skills,
                                                     required_tools=required_tools,
                                                     from_resources=from_resources,
                                                     to_resources_successful=to_resources_successful,
                                                     to_resources_interrupted=to_resources_interrupted,
                                                     )
        return entity
