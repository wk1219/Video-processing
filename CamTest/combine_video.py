import os
import glob
import cv2
import datetime

norm_path = os.getcwd() + '/video/'
impt_path = os.getcwd() + '/video/'

def create_time():
    now = datetime.datetime.today().strftime("%y%m%d_%H%M%S")
    return now

def impact():
    t = create_time()
    print("Time : %s" % t)
    video_mixing(t)

def video_mixing(t):
    print("Start")
    time = int(t[11:13])
    print(time)
    frame = 30
    file_path = glob.glob("%s*.mp4" % (norm_path))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    new_path = impt_path + 'IMPT_' + t + '.mp4'
    impt_out = cv2.VideoWriter(new_path, fourcc, 30.0, (640, 480))
    files = []
    files.append(sorted(file_path, key=os.path.getctime, reverse=True))

    if int(time) < 10:
        print("############ First ##########")
        imptFrame = time * 10
        start_time = (60 + time) - 10
        end_time = time + 10
        endFrame = end_time * frame
        print("Impt time : %d" % time)
        print("Start time : %d" % start_time)
        print("End time : %d" % end_time)
        print("End Frame : %d" % endFrame)
        startFrame = int(start_time) * int(frame)
        CurrentFrame = 0
        CurrentSecond = 0

        print("startFrame : %d" % startFrame)

        for i in range(0, 2):
            if i == 2:
                if not os.path.isfile(files[0][i]):
                    break
            print(files[0][i])

            cap = cv2.VideoCapture(files[0][1])
            amount_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            cap.set(cv2.CAP_PROP_POS_FRAMES, startFrame)
            middleFrame = amount_of_frames
            while True:
                ret, frame = cap.read()
                if (CurrentFrame > (middleFrame - imptFrame)):
                    cap = cv2.VideoCapture(files[0][0])
                    cap.set(cv2.CAP_PROP_POS_FRAMES, imptFrame)

                    while True:
                        ret, frame = cap.read()
                        if (CurrentSecond > (endFrame - 0)):
                            break
                        CurrentSecond += 1
                        impt_out.write(frame)
                    break

                CurrentFrame += 1

                impt_out.write(frame)
                cv2.waitKey(1)

            impt_out.release()
            print(amount_of_frames)
        print("Success!!")

    elif 10 <= int(time) <= 50:
        print("############ Second ##########")
        impt_time = int(time) * int(frame)
        startFrame = impt_time - frame * 10
        CurrentFrame = 0
        endFrame = impt_time + (frame * 10)
        print(impt_time)
        print(startFrame)
        print(endFrame)

        for i in range(0, 1):
            if i == 1:
                if os.path.isfile(files[0][i]) == False:
                    break
            print(files[0][i])
            cap = cv2.VideoCapture(files[0][i])
            amount_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            cap.set(cv2.CAP_PROP_POS_FRAMES, startFrame)

            while True:
                ret, frame = cap.read()
                if (CurrentFrame > (endFrame - startFrame)):
                    break
                CurrentFrame += 1

                impt_out.write(frame)
                # cv2.imshow('CAM_Window', frame)
                cv2.waitKey(1)

            impt_out.release()
            print(amount_of_frames)
        print("Success!!")


if __name__ == "__main__":
    # t = create_time()
    t = str('200609_231010')
    print(t)
    video_mixing(t)

