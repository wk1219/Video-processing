# -*-coding:utf8;-*-

import os
from kivy.uix.image import Image
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.uix.switch import Switch
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.video import Video
from kivy.uix.camera import Camera

import cv2


LabelBase.register(name="malgun",
                   fn_regular="malgun.ttf")

class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)


    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # convert it to texture
            texture = self.texture
            w, h = frame.shape[1], frame.shape[0]
            if not texture or texture.width != w or texture.height != h:
                self.texture = texture = Texture.create(size=(w, h))
                texture.flip_vertical()
            texture.blit_buffer(frame.tobytes(), colorfmt='bgr')
            self.canvas.ask_update()

class Main(Screen):
    pass

class Menu(Screen):
    pass

    def drowsiness_switch(selfself, switchObject, switchValue):
        if(switchValue):
            print('Switch is On:')
        else:
            print('Switch is OFF')

class Setting(Screen):
    pass

    def drowsiness_switch(selfself, switchObject, switchValue):
        if(switchValue):
            print('Switch is On:')
        else:
            print('Switch is OFF')

class Video_list(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = KivyCamera(capture=self.capture, fps=30)
        return ui

    def on_stop(self):
        self.capture.release()


ui = Builder.load_file("UI.kv")

if __name__ == '__main__':
    MyApp().run()
