from kivy.lang import Builder
from kivy.uix.behaviors import DragBehavior
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.uix.image import AsyncImage

from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.list import TwoLineListItem

from kivymd.uix.screen import MDScreen
from kivymd.utils.fitimage import FitImage

from objects.player import Player

player = Player()


class RegisterWindow(MDScreen):
    def register(self, name):
        if len(name) != 0 and player.client.connected:
            if player.client.register(name):
                print(f'[SERVER] registered as {name}')

                self.manager.transition.direction = 'left'
                app.root.current = "createorjoin"


class CreateOrJoinWindow(MDScreen):
    def join(self):
        self.manager.transition.direction = 'left'
        app.root.current = 'join'

    def create(self):
        self.manager.transition.direction = 'left'
        app.root.current = 'create'


class CreateWindow(MDScreen):
    def create(self, name):
        if player.create_room(name):
            print(f'[ROOM] created room {name}')

            self.manager.transition.direction = 'left'
            app.root.current = 'main'


class JoinWindow(MDScreen):
    def join(self, room_id):
        if player.join_room(room_id):
            print(f'[ROOM] joined room {room_id}')

            self.manager.transition.direction = 'left'
            app.root.current = 'main'


class DragImage(DragBehavior, AsyncImage):
    def on_touch_move(self, touch):
        touch.dy = 0
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)


class MainWindow(MDScreen):
    def on_pre_enter(self):

        """Fixes navigation bar bug"""
        temp = MDBottomNavigationItem(name='test', text='test', icon='alien-outline')
        self.ids.nav.add_widget(temp)
        self.ids.nav.remove_widget(temp)

        self.ids.nav.switch_tab('swipe')

        player.client.set_main_window(self)

        self.update_room_info()
        self.update_member_list()
        self.update_movie()

    def update_movie(self):
        movie = player.get_current_movie()
        poster_url = movie['poster_url']

        swipe_img = self.ids.swipe_img

        swipe_img.source = poster_url

    def update_member_list(self):

        list = self.ids.member_list

        list.clear_widgets()

        for name in player.get_room_member_names():
            item = TwoLineListItem(text=name, secondary_text='member')
            list.add_widget(item)

    def update_room_info(self):
        id, name = player.get_room_info()

        self.ids.room_name.text = name
        self.ids.room_id.text = 'ID:' + str(id)

    def leave(self):
        if player.leave_room():
            print('[ROOM] left room')
            self.manager.transition.direction = 'left'
            app.root.current = 'createorjoin'


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    title = 'MovieMatch'

    def build(self):
        return Builder.load_file('moviematch.kv')

    def on_start(self):
        pass

    def on_stop(self):
        player.client.leave_room()
        player.client.disconnect_from_server()


Window.size = (360, 600)
app = MainApp()
app.run()
