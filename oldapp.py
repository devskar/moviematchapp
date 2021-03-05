import kivymd

from kivymd.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen as Screen
from kivy.core.window import Window
from kivymd.uix.gridlayout import MDGridLayout as GridLayout
from kivymd.uix.label import MDLabel as Label

from objects.player import Player




class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('temp.kv')


class MovieMatch(App):

    def build(self):
        Window.bind(on_request_close=self.close)
        return kv

    def close(self, *args):
        player.client.disconnect_from_server()
        return True


if __name__ == "__main__":
    Window.size = (360, 600)
#    Window.clearcolor = (1, 1, 1, 1)
    MovieMatch().run()
