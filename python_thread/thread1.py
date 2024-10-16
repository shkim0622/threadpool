import threading
import time

def func(name):
    for i in range(3):
        print("Thread {}: {}".format(name,i))
        time.sleep(1)

def func2(name):
    for i in range(3):
        print("Thread {}: {}".format(name,i))
        time.sleep(1)
    
    
thread1 = threading.Thread(target=func, args=("1"))
thread2 = threading.Thread(target=func2, args=("2"))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("thread end")
