import datetime

def create_time():
    now = datetime.datetime.today().strftime("%y%m%d_%H%M%S")
    return now

class ListQueue:
    def __init__(self):
        self.my_list = list()

    def put(self, element):
        self.my_list.append(element)
        self.my_list = sorted(set(self.my_list), reverse=True)

    def get(self):
        return self.my_list.pop(0)

    def qsize(self):
        return len(self.my_list)

    def remove(self, obj):
        self.my_list.pop(obj)

time_queue = ListQueue()
while True:
    t = create_time()
    file_name = t + '.mp4'
    sec = int(t[11:13])
    impt_tuple = (file_name, sec)
    if impt_tuple[1] > 50:
        time_queue.put(impt_tuple)

    if sec == 00:
        break

for i in range(0, time_queue.qsize()):
    value = time_queue.get()
    print("[%d] file_name : %s impt_time : %d" % (i, value[0], value[1]))
print(time_queue.qsize())

