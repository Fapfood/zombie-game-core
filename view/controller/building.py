from zombie_game_type import building_static_service

from db import PersonDao
from view.display import render_part


class BuildingController:
    def __init__(self, building_service, building_room_service, map):
        self.building_service = building_service
        self.building_room_service = building_room_service
        self.map = map

    def intersection(self, player):
        building_plot = self.map.building_interaction(player.pos)
        return building_plot

    def inspect(self, player):
        building_plot = self.intersection(player)
        title = 'Interact'

        if building_plot is None:
            return self._building_not_found_message(title)

        building = self.building_service.read_by_id(building_plot.id)
        room = building.focused_on

        if room is None:
            return self._inspected_message(title)

        if room.type is None:
            return self._inspected_message(title, room.id)

        if room.production_type is None:
            return self._inspected_message(title, room.id, room.type)

        if len(room.workers) == 0:
            return self._inspected_message(title, room.id, room.type, room.production_type)

        workers = ', '.join(['{} {}'.format(w.first_name, w.last_name) for w in room.workers])
        return self._inspected_message(title, room.id, room.type, room.production_type, workers)

    def focus_on(self, player):
        building_plot = self.intersection(player)
        title = 'Focus'

        if building_plot is None:
            return self._building_not_found_message(title)

        building = self.building_service.read_by_id(building_plot.id)
        room = building.focused_on

        rooms = building.rooms
        groups = [
            {'id': 0,
             'parameter': 'room_id',
             'label': 'Room:',
             'choices': [{'id': el.id, 'name': '{}: {}'.format(el.id, el.type if el.type is not None else 'empty'),
                          'selected': room == el} for el in rooms],
             },
        ]
        return self._room_focused_message(title, '/building/{}'.format(building.id), groups)

    def assign_type_to(self, player):
        building_plot = self.intersection(player)
        title = 'Assign type to room'

        if building_plot is None:
            return self._building_not_found_message(title)

        building = self.building_service.read_by_id(building_plot.id)
        room = building.focused_on

        if room is None:
            return self._not_focused_on_room_message(title)

        building_types = building_static_service.get_all()
        groups = [
            {'id': 0,
             'parameter': 'building_type_id',
             'label': 'Building type:',
             'choices': [{'id': el.name, 'name': el.name,
                          'selected': room.type == el} for el in building_types],
             },
        ]
        return self._type_assigned_message(title, '/building/{}/room/{}'.format(building.id, room.id), groups)

    def assign_line_to(self, player):
        building_plot = self.intersection(player)
        title = 'Assign production type to room'

        if building_plot is None:
            return self._building_not_found_message(title)

        building = self.building_service.read_by_id(building_plot.id)
        room = building.focused_on

        if room is None:
            return self._not_focused_on_room_message(title)

        if room.type is None:
            return self._type_not_assigned_message(title)

        production_types = building_static_service.get_by_name(room.type).available_productions
        groups = [
            {
                'id': 0,
                'parameter': 'production_type_id',
                'label': 'Production type:',
                'choices': [{'id': el.name, 'name': el.name,
                             'selected': room.production_type == el} for el in production_types],
            },
        ]
        return self._type_assigned_message(title, '/building/{}/room/{}'.format(building.id, room.id), groups)

    def assign_workers_to(self, player):
        building_plot = self.intersection(player)
        title = 'Assign workers to room'

        if building_plot is None:
            return self._building_not_found_message(title)

        building = self.building_service.read_by_id(building_plot.id)
        room = building.focused_on

        if room is None:
            return self._not_focused_on_room_message(title)

        if room.type is None:
            return self._type_not_assigned_message(title)

        persons = PersonDao.read_all_owned()
        assigned_persons = PersonDao.read_all_by_building_room_id(room.id)
        groups = [
            {
                'id': i,
                'parameter': 'worker',
                'label': 'Worker:',
                'choices': [{'id': el.id, 'name': '{} {}'.format(el.first_name, el.last_name),
                             'selected': len(assigned_persons) > i and assigned_persons[i] == el} for el in persons],
            }
            for i in range(building_static_service.get_by_name(room.type).max_workers)
        ]
        return self._workers_assigned_message(title, '/building/{}/room/{}'.format(building.id, room.id), groups)

    def _building_not_found_message(self, title):
        return self._red_message(title=title, message='Building to interact with NOT found.')

    def _inspected_message(self, title, focused_on_id=None, type=None, line=None, workers=None):
        message = ''
        if focused_on_id is None:
            message += 'Building is not focused on any room.'
        else:
            message += 'Building is currently focused on room {}.'.format(focused_on_id)
            if type is None:
                message += '</br>Type not assigned to this room.'
            else:
                if line is None:
                    message += '</br>Production type not assigned to this {}.'.format(type)
                else:
                    message += '</br>Production type {} is assigned to this {}.'.format(line, type)
                if workers is not None:
                    message += '</br>{} are assigned to work in this {}.'.format(workers, type)
        return self._green_message(title=title, message=message)

    def _not_focused_on_room_message(self, title):
        return self._red_message(title=title, message='Building is not focused on any room.')

    def _type_not_assigned_message(self, title):
        return self._red_message(title=title, message='Type not assigned to this room.')

    def _line_not_assigned_message(self, title):
        return self._red_message(title=title, message='Production type not assigned to this room.')

    def _workers_not_assigned_message(self, title, type):
        return self._red_message(title=title, message='Workers not assigned to this {}.'.format(type))

    @staticmethod
    def _room_focused_message(title, url, groups):
        return render_part(template='modal/modal-form-2.0.html', modal_id='common-modal',
                           title=title, button_text='Focus', http_method='POST',
                           action_url=url, groups=groups)

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
    def _workers_assigned_message(title, url, groups):
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
