from flask_restplus import Model, fields

from .building_type import BuildingTypeModelSimple as BuildingTypeModel
from .person import PersonModel as PersonModel
from .production_type import ProductionTypeModel as ProductionTypeModel

BuildingModel = Model('Building', {
    'id': fields.Integer(required=True, description='Building id'),
    'type': fields.Nested(BuildingTypeModel, required=False, description='Building type'),
    'production_type': fields.Nested(ProductionTypeModel, required=False, description='Production type'),
    'workers': fields.List(required=False, cls_or_instance=fields.Nested(PersonModel), description='Workers'),
})
