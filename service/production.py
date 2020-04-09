class ProductionService:
    def __init__(self, productionDao, resourceTypeDao, resourcePackDao, skillTypeDao, skillLevelDao):
        self.productionDao = productionDao
        self.resourceTypeDao = resourceTypeDao
        self.resourcePackDao = resourcePackDao
        self.skillTypeDao = skillTypeDao
        self.skillLevelDao = skillLevelDao

    def get_or_create_production(self, production):
        required_skills = self._create_missing_skill_levels(production.required_skills)
        required_tools = self._create_missing_resource_packs(production.required_tools)
        from_resources = self._create_missing_resource_packs(production.from_resources)
        to_resources_successful = self._create_missing_resource_packs(production.to_resources_successful)
        to_resources_interrupted = self._create_missing_resource_packs(production.to_resources_interrupted)

        prod = self.productionDao.read_by_name(name=production.name)

        if prod is None:
            prod = self.productionDao.create(name=production.name, minutes=production.minutes,
                                             required_skills=required_skills,
                                             required_tools=required_tools,
                                             from_resources=from_resources,
                                             to_resources_successful=to_resources_successful,
                                             to_resources_interrupted=to_resources_interrupted)
        return prod

    def _create_missing_skill_levels(self, lis):
        res = []
        for el in lis:
            entity = self.skillLevelDao.read_by_type_name_and_level(type_name=el.name, level=el.level)
            if entity is None:
                type = self.skillTypeDao.read_by_name(name=el.name)
                if type is None:
                    type = self.skillTypeDao.create(name=el.name)
                type_id = type.id
                entity = self.skillLevelDao.create(skill_type_id=type_id, level=el.level)
            res.append(entity)
        return res

    def _create_missing_resource_packs(self, lis):
        res = []
        for el in lis:
            entity = self.resourcePackDao.read_by_type_name_and_quantity(type_name=el.name, quantity=el.quantity)
            if entity is None:
                type = self.resourceTypeDao.read_by_name(name=el.name)
                if type is None:
                    type = self.resourceTypeDao.create(name=el.name)
                type_id = type.id
                entity = self.resourcePackDao.create(resource_type_id=type_id, quantity=el.quantity)
            res.append(entity)
        return res
