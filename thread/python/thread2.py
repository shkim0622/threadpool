import threading
import time

class Mythread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name  
        
    def run(self):
        print("{} start ".format (threading.current_thread().name))
        time.sleep(3)
        print("{} end ".format (threading.current_thread().name))

def main():
    for i in range(5):
        t = Mythread("thread {}".format(i))              
        t.start()     
        
if __name__ == "__main__":
    main()                