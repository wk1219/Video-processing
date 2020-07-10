from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
import datetime

norm_path = 'D:\\UI\\'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

class KivyCamera(Image):

    def create_time(self):
        now = datetime.datetime.today().strftime("%y%m%d_%H%M%S")
        return now

    def create_file(self):
        now = self.create_time()
        file_name = now + '.mp4'
        return file_name

    def normal_recording(self):
        __file_name = self.create_file()
        path = norm_path + "NORM_" + __file_name
        norm_out = cv2.VideoWriter(path, fourcc, 30.0, (640, 480))
        return path, norm_out

    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        path = self.normal_recording()[0]
        out = self.normal_recording()[1]
        Clock.schedule_interval(self.update, 1.0 / fps)


    def update(self, dt, out, path):
            ret, frame = self.capture.read()
            if ret:
                buf1 = cv2.flip(frame, 0)
                buf = buf1.tostring()
                image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
                image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                self.texture = image_texture
                out.write(frame)



class Main(Screen):
    def cam(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = KivyCamera(capture=self.capture, fps=30)

class Menu(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class CombineScreen(FloatLayout):
    pass

class CamApp(App):
    def build(self):
        # self.capture = cv2.VideoCapture(0)
        # self.my_camera = KivyCamera(capture=self.capture, fps=30)
        return ui

    def on_stop(self):
        self.capture.release()

ui = Builder.load_file("vidui.kv")

if __name__ == '__main__':
    CamApp().run()