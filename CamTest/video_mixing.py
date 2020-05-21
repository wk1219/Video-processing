import os
import glob
import cv2

folder = r"path"
file_path = glob.glob("%s/*.mp4" % (folder))

files = []
files.append(sorted(file_path, key=os.path.getctime, reverse=True))

# Input impact  (Modify)
# if y_scale > threshold:
#   time = "Time"
#   startFrame = time - 250     10 seconds before impact
#   endFrame = Time + 250       10 seconds after impact

startFrame = 10
CurrentFrame = 0
endFrame = 22

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
npath = folder + '\\output.mp4'
impt_out = cv2.VideoWriter(npath, fourcc, 25.0, (640, 480))

for i in range(0, 2):
    print(files[0][i])
    cap = cv2.VideoCapture(files[0][i])
    fps = cap.get(cv2.CAP_PROP_FPS)
    current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
    amount_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    cap.set(cv2.CAP_PROP_POS_FRAMES, startFrame)

    while True:
        ret, frame = cap.read()
        if (CurrentFrame > (endFrame - startFrame)):
            break
        CurrentFrame += 1

        impt_out.write(frame)
        cv2.imshow("image", frame)
        cv2.waitKey(1)

    impt_out.release()
    print(amount_of_frames)


