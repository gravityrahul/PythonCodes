'''
Created on Sep 16, 2013

@author: 502100330
'''
import thread
import time
import random 

def runOften(threadName, sleepTime):
    while 1<2:
        time.sleep(sleepTime)
        print "%s" %(threadName)
        

def runLessOften(threadName, sleepTime):
    while 1<2:
        time.sleep(sleepTime)
        print "%s" %(threadName)
        
def runFastandRandom(threadName, sleepTime):
    while 1<2:
        time.sleep(sleepTime)
        print "%s" %(threadName)
        
thread.start_new_thread(runOften,("Often Runs \n", 1))
thread.start_new_thread(runLessOften,("Often Runs Less \n", 2))
thread.start_new_thread(runFastandRandom("Runs Fast and Random \n", random.random()))