'''
A class variable is one whose single value is shared by all instances of the class and, in
fact, is shared by all who have access to the class (object).

"Normal" methods are instance methods. An instance method receives the instance as its
first argument. A instance method is defined by using the def statement in the body of a
class statement.
'''
import time

class Date(object):
    """
    A static method does not receive anything special as its first argument. A static method is
    defined by defining a normal/instance method, then using the staticmethod builtin
    function.
    """
    
    def __init__(self, year, mon, day):
        self.year = year
        self.mon = mon 
        self.day = day
     
    @staticmethod    
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)
    
    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)
    
    def __str__(self):
        return "%02d-%02d-%04d" % (self.mon, self.day, self.year)
    
##################################################################################################
# Let's instantiate the class and play around
##################################################################################################

a = Date(1967, 11, 2)
b = Date.now()
c = Date.tomorrow()


class EuroDate(Date):
    #Modify the __str__ method
    def __str__(self):
        return "%02d-%02d-%04d" % (self.day, self.mon, self.year)
    

d = EuroDate(1967, 11, 1)
print a
print b
print c




##################################################################################################
# Class Methods
##################################################################################################
"""
Class methods are methods that operate on the class itself as an object. 
Defined using the @classmethod decorator

A class method receives the class as its first argument. A class method is defined by
defining a normal/instance method, then using the classmethod builtin
function.

"""
class Times(object):
    factor = 1
    @classmethod
    def multi(cls,x):
        return cls.factor * x
    
class TwoTimes(Times):
    factor = 2
 
print Times.multi(4)   
x = TwoTimes.multi(4)
print x

### END ###
 

