'''
Created on Sep 11, 2013

@author: 502100330
'''
import math

class Circle(object):
    
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return math.pi*self.radius**2
    
    @property
    def perimeter(self):
        return 2*math.pi*self.radius
    

C = Circle(4)
print C.area
print C.perimeter

####################################################################################################
# Note the difference how the attributes are called without the ()
# If you call them with (), you will get the TypeError
# 
# Traceback (most recent call last):
#   File "C:\Users\502100330\Python\PythonConcepts\propertyExample.py", line 23, in <module>
#     print C.area()
# TypeError: 'float' object is not callable
###################################################################################################