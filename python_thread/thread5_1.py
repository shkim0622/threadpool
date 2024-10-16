import threading
import time
import random

def run():
    for i in range(3):
        r = random.randint(1, 10)
        print("thread1 : {}".format(r))
        time.sleep(1)
        print("thread2: {}".format( r+1))
        time.sleep(1)
    return r

t1 = threading.Thread(target=run) # sub thread
t1.start()





    


