import threading
import time, random

class Counter(object):
    
    def __init__(self):
        self.lock=threading.Lock()
        self.value = 0
        
    def increment(self):
        self.lock.acquire()
        self.value = self.value + 1
        self.lock.release()
        return self.value



class Worker(threading.Thread):
    global counter
    def run(self):
        for i in range(10):
            #pretend we're are doing something that takes 10-100 ms.
            value = counter.increment()
            time.sleep(random.randint(10,100)/1000.0)
            print self.getName(), "--task",i, "finished", value
            
            

if __name__ == "__main__":
    counter = Counter()
    for i in range(10):
        Worker().start()