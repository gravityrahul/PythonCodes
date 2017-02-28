'''
Created on Feb 20, 2014

@author: 502100330
'''
import threading
import Queue
import time, random 

num_Workers = 2

class Worker(threading.Thread):
    '''
    classdocs
    '''
    def __init__(self, queue):
        '''
        Constructor
        '''
        self.__queue = queue
        threading.Thread.__init__(self)
        
    def run(self):
        while 1:
            item = self.__queue.get()
            if item is None:
                break # Reached the end of the queue.
            time.sleep(random.randint(10, 100)/1000.0)
            
            print "Task: %s Finished" % (item)
        
        
if __name__ == "__main__":
    
    
    queue = Queue.Queue(3)
    for i in range(num_Workers):
        Worker(queue).start()
        
    for item in range(10):
        print "push", item
        queue.put(item)
        
    for i in range(num_Workers):
        queue.put(None) #Add end of queue markers

    

