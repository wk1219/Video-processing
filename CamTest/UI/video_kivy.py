from tkinter import Button

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class RootWidget(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class VideoPlayerApp(App):
    def name(self):
        text = 'NORM_200722_230835.mp4'
        print(text)
        # namebutton = self.root.ids.abc
        # namebutton.add_widget(Button(text='hello'))
        return text

    def build(self):
        self.txt = self.name()
        sm = ScreenManager()
        self.root = RootWidget()
        sm.add_widget(self.root)
        return sm

ui = Builder.load_file("play.kv")

if __name__ == "__main__":
    VideoPlayerApp().run()

# reference need : https://kivy.org/doc/stable/_modules/kivy/uix/videoplayer.html