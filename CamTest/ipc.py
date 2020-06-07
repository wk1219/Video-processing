from multiprocessing import Process, Queue
import time

def func1(q):
    q.put(['Send','Receive'])
    key = q.get()
    print(key[1])

def func2(q):
    p2 = Process(target=func2, args=(q,))
    p2.start()
    key = q.get()
    print(key[0])
    time.sleep(1)

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=func1, args=(q,))
    p2 = Process(target=func2, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()