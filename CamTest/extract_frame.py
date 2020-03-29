import cv2

cap = cv2.VideoCapture('NORM_200310_195611.mp4')

count = 0
while(cap.isOpened()):
    ret, image = cap.read()
    if (int(cap.get(1)) % 300 == 0):      # Extract specific frame
        print("Saved frame number : " + str(int(cap.get(1))))
        cv2.imwrite("frame\\frame%d.jpg" % count, image)
        print("Saved frame%d.jpg" % count)
        count += 1
cap.release()