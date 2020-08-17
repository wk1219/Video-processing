import os
from os import listdir
import glob
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import BooleanProperty, ListProperty, StringProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.videoplayer import VideoPlayer

path = 'C:\\Users\\sjms1\\Desktop\\video'
index = 0
select = False


def file_list(in_path):
    vidlist = glob.glob(in_path + '\\*.mp4')
    return vidlist


class VideoWidget(Screen):
    # key = 0
    # check = False
    # file = ''

    # Modify Constructor
    def __init__(self, **kwargs):
        super(VideoWidget, self).__init__(**kwargs)
        # self.key = key
        # self.check = check
        # self.file = file


    def vidname(self, key, check, file):
        source = file_list(path)
        vidlist = Video_list().data_items_norm
        # print(source)

        self.file = file
        self.key = key
        self.check = check

        print("#" * 50)
        print("key : " + str(key))
        print("check : " + str(check))

        # Modify
        for i in range(0, len(vidlist)):
            if check == True:
                file = source[key]

        print("file : " + str(self.file))
        print("#" * 50)
        return self.file

    def get_source(self):
        return self.file

    def load_vid(self):
        # video = self.vidname(self.key, self.check, self.file)
        video = self.file
        print("Video : " + str(video))
        # print("KEY : " + str(self.key))
        # print("CHECK : " + str(self.check))
        # print("FILE : " + str(self.file))
        vid = VideoPlayer(source=video, state='play', options={'allow_stretch': True, 'eos': 'loop'}, pos=(0, 100),
                          size_hint=(None, None), size=(800, 500))
        but = Button(text="HOHO", size_hint=(None, None), size=(400, 100))
        self.add_widget(vid)
        self.add_widget(but)
        return video

    def path_test(self):
        pt = os.path.join(path, 'video.mp4')
        return pt

    def on_leave(self):
        pass


class ScreenVideo(Screen):
    key = ''
    check = False
    file = ''
    def vidname(self, key, check):
        source = file_list(path)
        vidlist = Video_list().data_items_norm
        # print(source)
        # print("#" * 50)
        # print("key : " + str(key))
        # print("Check : " + str(check))

        # Modify
        for i in range(0, len(vidlist)):
            if check == True:
                self.file = source[key]

        # print(self.file)
        # print("#" * 50)
        return self.file

    def get_source(self):
        return self.file

    def load_vid(self):
        video = self.vidname(self.key, self.check)
        # print("HOHO")
        # print(video)
        # vid = VideoPlayer(source=video, state='play', options={'allow_stretch': False, 'eos': 'loop'}, size=(800, 700))
        # self.add_widget(vid)
        return video

    def path_test(self):
        pt = os.path.join(path, 'video.mp4')
        return pt

    def on_leave(self):
        pass


class WindowManager(ScreenManager):
    pass


class Menu(Screen):
    pass


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton(RecycleDataViewBehavior, Button):
    source = ''
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    val = (None, None)

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
        App.get_running_app().root.current = "video_widget"

    def on_press(self):
        data = self.text
        self.source = os.path.join(path, data)
        print("Selectable : %s" % self.selectable)
        print("Selected : %s" % self.selected)
        print("Index : %s" % self.index)
        if self.index == None:
            print("FileName : None")
        else:
            print("FileName : %s" % data)
            print("Abstract path : %s" % self.source)
        vw = VideoWidget()
        vw.vidname(self.index, self.selectable, self.text)
        print("=" * 50)
        return self.selectable

    def get_source(self):
        return self.source

    def get_val(self):
        self.val = (self.index, self.selectable)
        return self.val


class Video_list(Screen):
    data_items_norm = ListProperty([])
    video_items = []
    def __init__(self, **kwargs):
        super(Video_list, self).__init__(**kwargs)
        self.get_board()

    def get_board(self):
        self.video_items = file_list(path)
        for i in range(0, len(self.video_items)):
            self.data_items_norm.append(os.path.split(self.video_items[i])[1])
        return self.data_items_norm


class VideoPlayerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu = Menu()
        self.video_list = Video_list()
        self.sv = ScreenVideo()
        self.video_widget = VideoWidget()

    def build(self):
        sm = ScreenManager()
        sm.add_widget(self.sv)
        sm.add_widget(self.menu)
        sm.add_widget(self.video_list)
        sm.add_widget(self.video_widget)
        return sm


ui = Builder.load_file("play.kv")

if __name__ == "__main__":
    VideoPlayerApp().run()

# reference need : https://kivy.org/doc/stable/_modules/kivy/uix/videoplayer.html
# https://github.com/jcomish/kivy-video-app/blob/master/main.py
