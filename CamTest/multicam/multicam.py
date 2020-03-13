import os

import time
import RPi.GPIO as gp
import cv2
import subprocess

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.setup(15, gp.OUT)
gp.setup(16, gp.OUT)
gp.setup(21, gp.OUT)
gp.setup(22, gp.OUT)

gp.output(11, True)
gp.output(12, True)
gp.output(15, True)
gp.output(16, True)
gp.output(21, True)
gp.output(22, True)


def main():
    while True:
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
        print("camera 1 selected")
        # time.sleep(10)
        command = "raspistill -o /home/pi/Desktop/hot.jpg"
        output = subprocess.call(command, shell=True)

        gp.output(7, False)
        gp.output(11, True)
        gp.output(12, False)
        print("camera 2 selected")
        # time.sleep(10)

        # command ="raspivid -o /home/pi/Desktop/tkktk.h264"
        channel = '"(tcpclientsrc host=127.0.0.1 port=5000 ! gdpdepay ! rtph264pay name=pay0 pt=96 )"'
        command = "/home/pi/gst-rtsp-0.10.8/examples/test-launch " + channel
        output = subprocess.call(command, shell=True)


if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)

#https://m.blog.naver.com/PostView.nhn?blogId=jwh1807&logNo=220867688758&proxyReferer=https%3A%2F%2Fwww.google.com%2F