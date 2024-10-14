import threading
import time
import random

def func1():
    results = [] 
    for i in range(2):
        r = random.randint(1, 10)
        print("{} : {} ".format(threading.current_thread().name,r))
        results.append(r)  
        time.sleep(1)
    return results

def func2(values):
    for r in values:
        print("{}+1 : {} ".format(threading.current_thread().name,r+1))
        time.sleep(1)

def thread_func():
    v = func1()
    
    func2(v)

thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=thread_func)

thread1.start()
thread1.join()

thread2.start()
thread2.join()

print("thread end")
