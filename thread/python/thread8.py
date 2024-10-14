import threading
import time

def func(val1=(0)):
    t1=time.time()
    print(f"received val1 : {threading.current_thread().name}, {val1}")
    time.sleep(2)
    
    val2 = int(val1) + 1
    print(f'computed val2 : {threading.current_thread().name}, {val2}')
    t2=time.time()
    
    #print(f"{threading.current_thread().name} -- time :  {t2-t1}")

threads = []
for i in range(5):   
    names = f"func{i}" 
    t1 = threading.Thread(target=func, name=names, args=(0,))
    threads.append(t1)
    t1.start()

for t in threads:
    t.join()

# v= 0
# for i in range(5):
#     v= func(v)


print("thread end")
