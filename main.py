from threadpool import ThreadPool
from func import myfunc

pool =  ThreadPool(func = myfunc)

for i in range(10):
    pool.put(i)
    
while(True):
    name, i, out = pool.get()
    print(f"{__name__} :: output , thread_name: {name}, Task [i] : {i}, output :{out}")
