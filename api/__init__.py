from flask_restplus import Api

from .building import api as building
from .person import api as person
from .production import api as production
from .resource import api as resource
from .shape import api as shape
from .zone_room import api as zone_room

api = Api(
    title='Zombie Game',
    version='0.1',
    description='The description of the game',
)

api.add_namespace(building)
api.add_namespace(person)
api.add_namespace(production)
api.add_namespace(resource)
api.add_namespace(zone_room)
api.add_namespace(shape)
