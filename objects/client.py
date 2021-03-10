import socketio
import sys

from kivymd.uix.list import TwoLineAvatarIconListItem as ListItem, IconLeftWidget

from objects.responses import ServerResponse as Response

SERVER_ADDRESS = 'http://localhost:5000'


class Client:

    def __init__(self, name):
        self.main_window = None
        self.name = name
        self.sio = socketio.Client()
        self.connected = False

    def set_main_window(self, main_window):
        self.main_window = main_window

    def connect_to_server(self):
        """Connect to the server"""
        self.sio.connect(SERVER_ADDRESS)
        self.init_events()

    def disconnect_from_server(self):
        self.sio.disconnect()
        sys.exit()

    def init_events(self):
        """Initialize events"""

        # CLIENT EVENTS
        @self.sio.event
        def connect():
            print('[SERVER] connected')
            self.connected = True

        @self.sio.event
        def disconnect():
            print('[SERVER] disconnected ')

        # ROOM EVENTS
        @self.sio.event
        def member_join(name):
            print(f'[ROOM] {name} joined')

            self.main_window.update_member_list()

        @self.sio.event
        def member_leave(name):
            print(f'[ROOM] {name} left')

            self.main_window.update_member_list()

    def register(self, name):
        return self.sio.call('register', data=name) == Response.SUCCESS.value

    # ROOM METHODS
    def create_room(self, name):
        return self.sio.call('create_room', data=name) == Response.SUCCESS.value

    def join_room(self, room_id):
        return self.sio.call('join_room', data=room_id) == Response.SUCCESS.value

    def leave_room(self):
        return self.sio.call('leave_room') == Response.SUCCESS.value

    def get_room_info(self):
        return self.sio.call('get_room_info')

    def get_room_movie(self):
        return self.sio.call('get_room_movie')

    def get_room_member(self):
        return self.sio.call('get_room_member')

