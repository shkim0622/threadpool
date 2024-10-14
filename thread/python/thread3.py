import threading
import time
import random

shared_value = []
lock = threading.Lock() 

def func1(name):
    global shared_value
    for i in range(5):
        r = random.randint(1, 10) 
        lock.acquire()
        try:
            shared_value.append(r)
            print("Thread {} : {}".format(name, r))
        finally:
            lock.release()
        time.sleep(1)
        

def func2(name):
    global shared_value
    lock.acquire()
    try:
        for i in range(len(shared_value)):
            a = shared_value[i] + 1
            print("Thread {} : {}".format(name, a))
            time.sleep(1)
            
    finally:
        lock.release()

thread1 = threading.Thread(target=func1, args=("1"))
thread2 = threading.Thread(target=func2, args=("2"))

thread1.start()
thread1.join()

thread2.start()
thread2.join()

print("thread end")







