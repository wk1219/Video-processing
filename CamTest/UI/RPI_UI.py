# -*-coding:utf8;-*-

import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.uix.switch import Switch
from kivy.uix.video import Video
import cv2


LabelBase.register(name="malgun",
                   fn_regular="malgun.ttf")

class Main(Screen):
    pass
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.video = Video(source="test.mp4")
        self.add_widget(self.video)
    # def recording(selfself):
    #     cap = cv2.VideoCapture(0)
    #     while True:
    #         ret, frame = cap.read()
    #
    #         if ret:
    #             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #             cv2.imshow('video', gray)
    #             k = cv2.waitKey(1) & 0xFF
    #             if k == 27:
    #                 break
    #         else:
    #             print('error')
    #     cap.release()
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
        return ui



ui = Builder.load_file("UI.kv")

if __name__ == '__main__':
    MyApp().run()
