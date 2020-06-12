import datetime

def create_time():
    now = datetime.datetime.today().strftime("%y%m%d_%H%M%S")
    return now

impt_time = []

while True:
    t = create_time()
    sec = int(t[11:13])
    if sec % 2 == 1:
        impt_time.append(t)
        print(sec)
    elif sec == 20:
        break

time_queue = sorted(list(set(impt_time)), reverse=False)
queue_size = len(time_queue)

for i in range(0, queue_size):
    print("%s" % time_queue[i])