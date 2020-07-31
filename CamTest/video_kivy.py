from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

class RootWidget(BoxLayout):
    pass

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
