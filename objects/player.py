from objects.client import Client


class Player:
    def __init__(self):

        self.name = None
        self.client = Client(self.name)

#        self.client.connect_to_server()

        self.current_room_id = None

    # ROOM METHODS
    def create_room(self):
        self.client.create_room()

    def join_room(self, room_id):
        self.client.join_room(room_id)

    def leave_room(self):
        self.client.leave_room()

    def get_room_member_names(self):
        return self.client.get_room_member()
