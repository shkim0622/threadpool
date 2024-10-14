import threading
import time
import random

def func1():
    for i in range(3):
        r = random.randint(1, 10)
        print("Thread : {}".format(r))
        time.sleep(1)
            
t1 = threading.Thread(target=func1)    
t1.start()
t1.join()
print("Thread end ")



