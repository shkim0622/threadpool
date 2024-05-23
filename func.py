import time
import random
import threading

def myfunc(i):
    thread_name = threading.current_thread().name
    random_val = round(random.uniform(2,10),1)
    
    print(f"{thread_name} , {__name__}::[{i}] input : {i} , {random_val}s")
    time.sleep(random_val)
    print(f"{thread_name} , {__name__}::[{i}] time_sleep (input {i} ) : {random_val}s")
    out=random_val+i
    print(f"{thread_name} , {__name__}::[{i}] output : {out}" )
    return thread_name, i, out
