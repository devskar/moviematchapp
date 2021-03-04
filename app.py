import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from objects.player import Player

player = Player()


class RegisterWindow(Screen):
    def register(self, name):
        if player.client.connected and len(name) != 0:
            player.client.register(name)
            return True
        else:
            return False


class CreateOrJoinWindow(Screen):
    def create_room(self):
        player.create_room()


class JoinWindow(Screen):
    def join_room(self, room_id):
        player.join_room(room_id)


class RoomWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.layout = RoomMemberList()
        self.add_widget(self.layout)

    def button_click(self):
        self.layout.update()


class RoomMemberList(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

    def update(self):
        self.clear_widgets()
        names = player.get_room_member_names()

        for name in names:
            self.add_widget(Label(text=name, color=(1, 0, 1, 1)))
            print(name)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('moviematch.kv')


class MovieMatch(App):

    def build(self):
        Window.bind(on_request_close=self.close)
        return kv

    def close(self, *args):
        player.client.disconnect_from_server()
        return True


if __name__ == "__main__":
    Window.size = (360, 600)
    Window.clearcolor = (1, 1, 1, 1)
    MovieMatch().run()
