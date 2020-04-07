from db import PersonDao, \
    ShapePointDao, ShapeRingDao, ShapePolygonDao, ShapeMultiPolygonDao, \
    SkillLevelDao, SkillTypeDao
from .person import PersonService
from .shape import ShapeService

PersonSvc = PersonService(PersonDao, SkillTypeDao, SkillLevelDao)
ShapeSvc = ShapeService(ShapePointDao, ShapeRingDao, ShapePolygonDao, ShapeMultiPolygonDao)
