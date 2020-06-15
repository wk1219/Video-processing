import datetime

def create_time():
    now = datetime.datetime.today().strftime("%y%m%d_%H%M%S")
    return now

impt = []
while True:
    t = create_time()
    file_name = t + '.mp4'
    sec = int(t[11:13])
    impt_tuple = (file_name, sec)
    impt.append(impt_tuple)
    time_queue = sorted(set(impt), reverse=True)
    if sec == 20:
        break

    time_list = list(time_queue)

for i in range(0, len(time_list)):
    print("[%d] file_name : %s impt_time : %d" % (i, time_list[i][0], time_list[i][1]))


for i in range(0, len(time_list)):
    data = time_list.pop()
    print(data[0], data[1])

print(len(time_list))
