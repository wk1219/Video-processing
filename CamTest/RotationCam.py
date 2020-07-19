import cv2


capture = cv2.VideoCapture(0)
width = capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
height = capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()
    matrix = cv2.getRotationMatrix2D((640 / 2, 480 / 2), 90, 1)
    dst = cv2.warpAffine(frame, matrix, (640, 480))
    cv2.imshow("VideoFrame", dst)
    if cv2.waitKey(1) > 0: break


