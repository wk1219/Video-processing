import os
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
from kivy.uix.recycleview import RecycleView
import pymysql

path = 'C:\\Users\\sjms1\\Desktop\\video'
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

class Menu(Screen):
    pass

class Video_list(Screen):
    data_items_norm = ListProperty([])
    def get_board(self):
        self.data_items_norm.append('App_download.mp4')
        self.data_items_norm.append('NORM_200407_215033.mp4')
        self.data_items_norm.append('video.mp4')

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton(RecycleDataViewBehavior, Button):
    source = ''
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected

    def on_release(self, *args):
        App.get_running_app().root.current = "root"

    def on_press(self):
        data = self.text
        self.source = os.path.join(path, data)
        data_index = self.index

    def get_source(self):
        return self.source

class VideoPlayerApp(App):
    def build(self):
        sm = ScreenManager()
        self.root = RootWidget()
        self.menu = Menu()
        self.video_list = Video_list()
        sm.add_widget(self.root)
        sm.add_widget(self.menu)
        sm.add_widget(self.video_list)
        return sm

ui = Builder.load_file("play.kv")

if __name__ == "__main__":
    VideoPlayerApp().run()

# reference need : https://kivy.org/doc/stable/_modules/kivy/uix/videoplayer.html