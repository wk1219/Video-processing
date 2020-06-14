import datetime

def create_time():
    now = datetime.datetime.today().strftime("%y%m%d_%H%M%S")
    return now

impt = []
while True:
    t = create_time()
    file_name = t + '.mp4'
    sec = int(t[11:13])
    impt.append((file_name, sec))
    time_queue = sorted(set(impt), reverse=False)
    if sec == 40:
        break

keys = list(dict(time_queue).keys())        # Video file name list
values = list(dict(time_queue).values())    # Impact time (sec) list

for i in range(0, len(time_queue)):
    print("[%d] file_name : %s, impt_time : %d" % (i, keys[i], values[i]))
    # print("[%d] file_name : %s" % (i, time_queue[i]))
