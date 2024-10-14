import threading
import time
import random

def mythread (a,c):
    for i in range(a):
        r1=random.randint(1,10)
        print("{}님에게 {}번쨰 일을 완료하다".format(c,r1))
        time.sleep(1)
        print("{}님에게 {}번쨰 일을 완료하다".format(c,r1+1))    

   

thread1=threading.Thread(target=mythread ,args=(3,"Thread1   "))

thread1.start()
thread1.join()
mythread(3,"Thread2_main   ")
