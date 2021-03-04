import socketio
import sys
SERVER_ADDRESS = 'http://localhost:5000'


class Client:

    def __init__(self, name):
        self.name = name
        self.sio = socketio.Client()
        self.connected = False

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
        def new_member(name):
            print(f'[ROOM] member joined: {name}')

    def register(self, name):
        self.sio.emit('register', data=name)
        print(f'[SERVER] registered as {name}')

    # ROOM METHODS
    def create_room(self):
        self.sio.emit('create_room')
        print('[ROOM] created room')

    def join_room(self, room_id):
        self.sio.emit('join_room', data=room_id)
        print(f'[ROOM] joined room {room_id}')

    def leave_room(self):
        self.sio.emit('leave_room')
        print(f'[ROOM] left room')

    def get_room_member(self):
        names = self.sio.call('get_room_member')
        return names
