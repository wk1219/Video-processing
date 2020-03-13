import cv2
from os.path import getmtime, getctime, getatime
from datetime import datetime

file = r'C:\Users\sjms1\Desktop\Educate\capstone_design\블랙박스영상\Sample3_REC2_20191011_070036.avi'
cap = cv2.VideoCapture(file)

if not cap.isOpened():
    print("could not open :", file)
    exit(0)

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # length
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # frame width
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # frame height
fps = cap.get(cv2.CAP_PROP_FPS) # frame speed
video_length = int(length/fps) # video length (seconds)


mtime = datetime.fromtimestamp(getctime(file)).strftime('%Y-%m-%d %H:%M:%S')
print('length : ' + str(length))
print('resolution : ' + str(width) + ' x ' + str(height))
print('fps : ' + str(fps))
print('video length : ' + str(video_length) + ' sec')
print('creation time : ' + str(mtime))

# reference : https://webnautes.tistory.com/577