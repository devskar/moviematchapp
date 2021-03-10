from objects.client import Client


class Player:
    def __init__(self):

        self.name = None
        self.client = Client(self.name)

        self.client.connect_to_server()

        self.current_room_id = None

    # ROOM METHODS
    def create_room(self, name):
        return self.client.create_room(name)

    def join_room(self, room_id):
        return self.client.join_room(room_id)

    def leave_room(self):
        return self.client.leave_room()

    def get_room_info(self):
        return self.client.get_room_info()

    def get_room_member_names(self):
        return self.client.get_room_member()

    def get_current_movie(self):
        return self.client.get_room_movie()

    def match_current_movie(self):
        self.client.match_movie()

    def nomatch_current_movie(self):
        self.client.nomatch_movie()