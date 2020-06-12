import datetime

def create_time():
    now = datetime.datetime.today().strftime("%y%m%d_%H%M%S")
    return now

impt_time = []

while True:
    data = int(input())
    if data == 2:
        impt_time.append(create_time())
        continue
    elif data == 0:
        break

for i in range(0, len(impt_time)):
    print("%s" % impt_time[i])