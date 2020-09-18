from zombie_game_type import zone_room_filler_static_service


class ZoneRoomService:
    def __init__(self, zone_room_dao, resource_svc):
        self.zone_room_dao = zone_room_dao
        self.resource_svc = resource_svc

    def generate_zone_room(self, shape, long, lat):
        type = self._get_sample_zone_room_type()
        resources = self.resource_svc.generate_resources(type.resource_drop_table)
        zone_room = self.zone_room_dao.create(shape=shape, long=long, lat=lat, type=type.name, resources=resources)
        return zone_room

    @staticmethod
    def _get_sample_zone_room_type():
        return zone_room_filler_static_service.get_random()
