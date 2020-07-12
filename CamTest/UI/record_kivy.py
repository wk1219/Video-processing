import threading
from functools import partial
from kivy.uix.image import Image
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
import datetime

class MainScreen(Screen):
    pass

class Menu(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class CombineScreen(FloatLayout):
    pass

Builder.load_string('''

<MainScreen>
    name: "main"

    FloatLayout:
        BoxLayout:
            size: root.width, root.height
            orientation: 'vertical'
            BoxLayout:
                orientation: 'horizontal'
                size: 800, 700
                Image:
                    id: vid
                    size: 800, 700
                    size_hint: 1, 0.6
                    allow_stretch: True
                    keep_ratio: True
                    pos_hint: {'center_x':0.5, 'top':0.8}


            BoxLayout:
                orientation: 'horizontal'
                size: 800, 100
                size_hint: (None, None)
                Button:
                    text: "Back"
                    font_size: 50
                    on_release:
                        app.root.current = "menu"
                Button:
                    text: "Home"
                    font_size: 50
                    on_release:
                        app.root.current = "menu"
                Button:
                    text: "Menu"
                    font_size: 50
                    on_release:
                        app.root.current = "menu"

<Menu>
    name: "menu"
    BoxLayout:
        BoxLayout:
            orientation: 'horizontal'
            size: 800, 100
            size_hint: (None, None)

            Button:
                text: "Back"
                font_size: 50
                on_release:
                    app.root.current = "menu"
            Button:
                text: "Home"
                font_size: 50
                on_release:
                    app.root.current = "menu"
            Button:
                text: "Menu"
                font_size: 50
                on_release:
                    app.root.current = "menu"
''')

norm_path = 'D:\\UI\\'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
class Main(App):
    def build(self):
        threading.Thread(target=self.doit, daemon=True).start()
        sm = ScreenManager()
        self.main_screen = MainScreen()
        self.menu = Menu()
        sm.add_widget(self.main_screen)
        sm.add_widget(self.menu)
        return sm

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

    def doit(self):
        # this code is run in a separate thread
        self.do_vid = True  # flag to stop loop

        cam = cv2.VideoCapture(0)
        path = self.normal_recording()[0]
        out = self.normal_recording()[1]
        framecnt = 0
        fps = int(cam.get(cv2.CAP_PROP_FPS))
        sec = 0
        # start processing loop
        while (self.do_vid):
            framecnt += 1
            ret, frame = cam.read()
            sec = framecnt / fps
            print("%d %d %d" % (framecnt, fps, sec))
            Clock.schedule_once(partial(self.display_frame, frame))
            out.write(frame)
            cv2.imshow('Hidden', frame)
            cv2.waitKey(1)
            if sec == 10:
                out.release()
                break

        nthread = threading.Thread(target=self.doit)
        nthread.start()

    def stop_vid(self):
        # stop the video capture loop
        self.do_vid = False

    def display_frame(self, frame, dt):
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(frame.tobytes(order=None), colorfmt='bgr', bufferfmt='ubyte')
        texture.flip_vertical()
        self.main_screen.ids.vid.texture = texture

# class KivyCamera(Image):
#     def create_time(self):
#         now = datetime.datetime.today().strftime("%y%m%d_%H%M%S")
#         return now
#
#     def create_file(self):
#         now = self.create_time()
#         file_name = now + '.mp4'
#         return file_name
#
#     def normal_recording(self):
#         __file_name = self.create_file()
#         path = norm_path + "NORM_" + __file_name
#         norm_out = cv2.VideoWriter(path, fourcc, 30.0, (640, 480))
#         return path, norm_out
#
#     def __init__(self, capture, fps, **kwargs):
#         super(KivyCamera, self).__init__(**kwargs)
#         self.capture = capture
#         path = self.normal_recording()[0]
#         out = self.normal_recording()[1]
#         self.update(dt=(1.0 / fps), out=out, path=path)
#         # Clock.schedule_interval(self.update, 1.0 / fps)
#
#
#     def update(self, dt, out, path):
#
#             # ret, frame = self.capture.read()
#             # if ret:
#             #     buf1 = cv2.flip(frame, 0)
#             #     buf = buf1.tostring()
#             #     image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#             #     image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
#             #     self.texture = image_texture
#
#             framecnt = 0
#             fps = int(self.capture.get(cv2.CAP_PROP_FPS))
#
#             while True:
#                 framecnt += 1
#                 ret, frame = self.capture.read()
#                 if ret:
#                     buf1 = cv2.flip(frame, 0)
#                     buf = buf1.tostring()
#                     image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#                     image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
#                     self.texture = image_texture
#                 sec = framecnt / fps
#                 rr = (self.capture.get(cv2.CAP_PROP_POS_FRAMES))
#
#                 print("%d %d %d %d" % (fps, framecnt, rr, sec))
#                 out.write(frame)
#
#                 if sec == 10:
#                     out.release()
#                     break
#




# class CamApp(App):
#     def build(self):
#         # self.capture = cv2.VideoCapture(0)
#         # self.my_camera = KivyCamera(capture=self.capture, fps=30)
#         return ui
#
#     # def on_start(self):
#     #     m = Main()
#     #     m.cam()
#     def on_stop(self):
#         self.capture.release()

# ui = Builder.load_file("vidui.kv")

if __name__ == '__main__':
    Main().run()