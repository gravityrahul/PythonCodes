'''
Created on Sep 11, 2013

@author: 502100330
'''
class Foo(object):
    
    @staticmethod
    def add(x,y): return x+y
    
    
###########################################################################
# Instantiate the class
###########################################################################

class Bar(object):

    @classmethod
    def add(cls, x, y):
        return x+y
    
    
class Bazz(object):
    
    def add(self, x, y):
        return x+y
        
x = Foo.add(3, 4)
print x
 
y = Bar.add(3,4)   
print y

z = Bazz().add(3,4)
print z

print Bar.add
print Foo.add
print Bazz.add
print Bazz().add
