import cv2
import sys
import threading
from PyQt5 import QtWidgets
from PyQt5 import QtGui

running = False
def run():
    global running
    cap = cv2.VideoCapture(0)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    label.resize(width, height)
    while running:
        ret, img = cap.read()

        if ret:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            label.setPixmap(pixmap)

        else:
            QtWidgets.QMessageBox.about(win, "Error", "Cannot read frame.")
            print("cannot read frame.")
            break

        k = cv2.waitKey(30)
        if k == 27:  # ESC
            running = False
            sys.exit()
            break


    cap.release()
    print("Thread end.")



app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()
vbox = QtWidgets.QVBoxLayout()
label = QtWidgets.QLabel()
vbox.addWidget(label)
win.setLayout(vbox)
running = True
th = threading.Thread(target=run)
th.start()
win.show()
sys.exit(app.exec_())