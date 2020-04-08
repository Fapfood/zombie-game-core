class ProductionService:
    def __init__(self, productionDao, resourceTypeDao, resourcePackDao, skillTypeDao, skillLevelDao):
        self.productionDao = productionDao
        self.resourceTypeDao = resourceTypeDao
        self.resourcePackDao = resourcePackDao
        self.skillTypeDao = skillTypeDao
        self.skillLevelDao = skillLevelDao

    def check_if_production_exist(self, production):
        for skill in production.required_skills:
            self.skillTypeDao.read_all_by(name=skill.type)
            self.skillLevelDao.read_all_by(level=skill.level, skill_type_id=skill.type)
        pass

    def create_production(self, production):
        pass
