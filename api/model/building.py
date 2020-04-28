from flask_restplus import Model, fields

from .building_type import BuildingTypeModelSimple as BuildingTypeModel
from .person import PersonModel as PersonModel
from .production_type import ProductionTypeModel as ProductionTypeModel

BuildingModel = Model('Building', {
    'id': fields.Integer(required=True),
    'type': fields.Nested(BuildingTypeModel, required=False),
    'production_type': fields.Nested(ProductionTypeModel, required=False),
    'workers': fields.List(fields.Nested(PersonModel), required=False),
})
