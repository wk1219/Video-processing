import cv2
import numpy as np


def open_cam_rtsp(uri, width, height, latency):
	gst_str = ('rtspsrc location={} latency={} ! '
               'rtph264depay ! h264parse ! avdec_h264 ! '
               ' autovideoconvert ! autovideosink ').format(uri, latency)
	print(gst_str)
	return cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

cap = cv2.VideoCapture("rtsp://127.0.0.1:7000/unbox", cv2.CAP_GSTREAMER)

if not cap.isOpened():
	print('VideoCapture not opened')
	exit(0)

while True:
	ret, frame = cap.read()

	if not ret:
		print('empty frame')
		break

	cv2.imshow('display', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	cap.release()

cv2.destroyAllWindows()