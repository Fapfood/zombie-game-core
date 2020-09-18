from zombie_game_type import building_static_service

from db import PersonDao
from view.display import render_part


class BuildingController:
    def __init__(self, building_service, map):
        self.building_dao = building_service
        self.map = map

    def intersection(self, player):
        building_plot = self.map.building_interaction(player.pos)
        return building_plot

    def interact_with(self, player):
        building_plot = self.intersection(player)
        title = 'Interact'

        if building_plot is None:
            return self._room_not_found_message(title)

        building = self.building_dao.read_by_id(building_plot.id)
        if building.type is None:
            return self._type_not_assigned_message(title)

        if building.production_type is None:
            return self._line_not_assigned_message(title)

        if len(building.workers) == 0:
            return self._workers_not_assigned_message(title, building.type)

        workers = ', '.join(['{} {}'.format(w.first_name, w.last_name) for w in building.workers])
        return self._workers_assigned_message(title, workers, building.type)

    def assign_type_to(self, player):
        building_plot = self.intersection(player)
        title = 'Assign type to room'

        if building_plot is None:
            return self._room_not_found_message(title)

        building = self.building_dao.read_by_id(building_plot.id)

        building_types = building_static_service.get_all()
        groups = [
            {'id': 0,
             'parameter': 'building_type_id',
             'label': 'Building type:',
             'choices': [{'id': el.name, 'name': el.name,
                          'selected': building.type == el} for el in building_types],
             },
        ]
        return self._type_assigned_message(title, '/building/{}'.format(building.id), groups)

    def assign_line_to(self, player):
        building_plot = self.intersection(player)
        title = 'Assign production type to room'

        if building_plot is None:
            return self._room_not_found_message(title)

        building = self.building_dao.read_by_id(building_plot.id)
        if building.type is None:
            return self._type_not_assigned_message(title)

        production_types = building_static_service.get_by_name(building.type).available_productions
        groups = [
            {
                'id': 0,
                'parameter': 'production_type_id',
                'label': 'Production type:',
                'choices': [{'id': el.name, 'name': el.name,
                             'selected': building.production_type == el} for el in production_types],
            },
        ]
        return self._type_assigned_message(title, '/building/{}'.format(building.id), groups)

    def assign_workers_to(self, player):
        building_plot = self.intersection(player)
        title = 'Assign workers to room'

        if building_plot is None:
            return self._room_not_found_message(title)

        building = self.building_dao.read_by_id(building_plot.id)
        if building.type is None:
            return self._type_not_assigned_message(title)

        persons = PersonDao.read_all()
        assigned_persons = PersonDao.read_all_by_building_id(building.id)
        groups = [
            {
                'id': i,
                'parameter': 'worker',
                'label': 'Worker:',
                'choices': [{'id': el.id, 'name': '{} {}'.format(el.first_name, el.last_name),
                             'selected': len(assigned_persons) > i and assigned_persons[i] == el} for el in persons],
            }
            for i in range(building_static_service.get_by_name(building.type).max_workers)
        ]
        return self._workers_assigned_message2(title, '/building/{}'.format(building.id), groups)

    def _room_not_found_message(self, title):
        return self._red_message(title=title, message='Room to interact with NOT found.')

    def _type_not_assigned_message(self, title):
        return self._red_message(title=title, message='Type not assigned to this room.')

    def _line_not_assigned_message(self, title):
        return self._green_message(title=title, message='Production type not assigned to this room.')

    def _workers_not_assigned_message(self, title, type):
        return self._green_message(title=title, message='Workers not assigned to this {}.'.format(type))

    def _workers_assigned_message(self, title, workers, type):
        return self._green_message(title=title, message='{} are assigned to work in this {}.'.format(workers, type))

    @staticmethod
    def _type_assigned_message(title, url, groups):
        return render_part(template='modal/modal-form-2.0.html', modal_id='common-modal',
                           title=title, button_text='Assign', http_method='POST',
                           action_url=url, groups=groups)

    @staticmethod
    def _line_assigned_message(title, url, groups):
        return render_part(template='modal/modal-form-2.0.html', modal_id='common-modal',
                           title=title, button_text='Assign', http_method='POST',
                           action_url=url, groups=groups)

    @staticmethod
    def _workers_assigned_message2(title, url, groups):
        return render_part(template='modal/modal-form-2.0.html', modal_id='common-modal',
                           title=title, button_text='Assign', http_method='POST',
                           action_url=url, groups=groups)

    @staticmethod
    def _red_message(title, message):
        return render_part(template='modal/modal-message.html', modal_id='common-modal',
                           title=title, color='red', message=message)

    @staticmethod
    def _green_message(title, message):
        return render_part(template='modal/modal-message.html', modal_id='common-modal',
                           title=title, color='green', message=message)
