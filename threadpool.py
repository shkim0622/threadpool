from concurrent.futures import ThreadPoolExecutor
from queue import Queue 

class ThreadPool():
    def __init__(self,func):
        self.func = func
        self.queue = Queue() 
        self.pool =  ThreadPoolExecutor(max_workers=5)
           
    def put(self,i):
        future=self.pool.submit(self.func,i)
        self.queue.put(future)

    def get(self):
        future = self.queue.get()
        return future.result()
