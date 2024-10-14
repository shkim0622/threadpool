import threading
import time
import random

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
  
    def run(self):
        for i in range(3):
            r = random.randint(1, 10)
            print("Thread : {}".format( r))
            time.sleep(1)
            print("Thread +1 : {}".format( r + 1))
            time.sleep(1)

def main(): 
    t1 = MyThread() 
    t1.start()
    t1.join()
    print("threads end.")
    
if __name__ == "__main__":
    main()

