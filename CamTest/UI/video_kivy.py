from tkinter import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty, ListProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
import pymysql

class RootWidget(Screen):
    def vidname(self):
        vid_list = []
        text = 'IMPT_200531_180221.mp4'
        print(text)
        vid_list.append(text)
        vid_list.append('test.mp4')
        return vid_list[1]

class WindowManager(ScreenManager):
    pass

class VideoPlayerApp(App):
    def build(self):

        sm = ScreenManager()
        self.root = RootWidget()
        sm.add_widget(self.root)
        return sm

ui = Builder.load_file("play.kv")

if __name__ == "__main__":
    VideoPlayerApp().run()

# reference need : https://kivy.org/doc/stable/_modules/kivy/uix/videoplayer.html