from zombie_game_type import production_static_service

from service import BuildingService
from service import ProductionService
from service import ResourceService
from view.display import render_part


class ProductionController:
    def __init__(self, production_service: ProductionService,
                 building_service: BuildingService,
                 resource_service: ResourceService,
                 map):
        self.production_service = production_service
        self.building_service = building_service
        self.resource_service = resource_service
        self.map = map

    def intersection(self, player):
        building_plot = self.map.building_interaction(player.pos)
        return building_plot

    def start_production(self, player):
        building_plot = self.intersection(player)
        title = 'Produce'

        if building_plot is None:
            return self._building_not_found_message(title)

        building = self.building_service.read_by_id(building_plot.id)
        room = building.focused_on

        if room is None:
            return self._not_focused_on_room_message(title)

        if room.type is None:
            return self._type_not_assigned_message(title)

        if room.production_type is None:
            return self._line_not_assigned_message(title)

        if len(room.workers) == 0:
            return self._workers_not_assigned_message(title)

        workers = room.workers
        multigroups1 = [
            {
                'label': 'Workers:',
                'groups': [
                    {
                        'id': 0,
                        'parameter': 'worker',
                        'label': 'Required {}:'.format(skill_pack.name),
                        'choices': [
                            {'id': el.id,
                             'name': '{} {}'.format(el.first_name, el.last_name)}
                            for el in workers],
                    }
                    for skill_pack in production_static_service.get_by_name(room.production_type).required_skills
                ]
            }
        ]
        multigroups2 = [
            {
                'label': 'Required tools:',
                'groups': [
                    {
                        'id': 0,
                        'parameter': 'tool',
                        'label': 'Required {}:'.format(resource_pack.resource.name),
                        'choices': [
                            {'id': el.id,
                             'name': '{} &#x2B50; {} &#x1F480; {}'.format(el.type, el.quality, el.decay)}
                            for el in
                            self.resource_service.read_all_owned_and_available_by_type(resource_pack.resource.name)],
                    }
                    for resource_pack in production_static_service.get_by_name(room.production_type).required_tools
                    for _ in range(resource_pack.quantity)
                ]
            }
        ]
        multigroups3 = [
            {
                'label': 'Required resources:',
                'groups': [
                    {
                        'id': 0,
                        'parameter': 'resource',
                        'label': 'Required {}:'.format(resource_pack.resource.name),
                        'choices': [
                            {'id': el.id,
                             'name': '{} &#x2B50; {} &#x1F480; {}'.format(el.type, el.quality, el.decay)}
                            for el in
                            self.resource_service.read_all_owned_and_available_by_type(resource_pack.resource.name)],
                    }
                    for resource_pack in production_static_service.get_by_name(room.production_type).from_resources
                    for _ in range(resource_pack.quantity)
                ]
            }
        ]
        multigroups = multigroups1 + multigroups2 + multigroups3

        return render_part(template='modal/modal-multiform.html', modal_id='common-modal',
                           title='Produce', button_text='Produce', http_method='POST',
                           action_url='/production?type={}'.format(room.production_type), multigroups=multigroups)

    def _building_not_found_message(self, title):
        return self._red_message(title=title, message='Building to interact with NOT found.')

    def _not_focused_on_room_message(self, title):
        return self._red_message(title=title, message='Building is not focused on any room.')

    def _type_not_assigned_message(self, title):
        return self._red_message(title=title, message='Type not assigned to this room.')

    def _line_not_assigned_message(self, title):
        return self._red_message(title=title, message='Production type not assigned to this room.')

    def _workers_not_assigned_message(self, title):
        return self._red_message(title=title, message='Workers not assigned to this room.')

    @staticmethod
    def _red_message(title, message):
        return render_part(template='modal/modal-message.html', modal_id='common-modal',
                           title=title, color='red', message=message)
