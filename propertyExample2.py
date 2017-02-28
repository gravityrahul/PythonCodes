'''
Created on Sep 11, 2013

@author: 502100330
'''
class Foo(object):
    
    def __init__(self, name):
        # pay attention to the private variable .__name
        self.__name = name
        
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string")
        else:
            self.__name = value
            
    @name.deleter
    def name(self):
        raise TypeError("Can't delete the name")
    

class SomeClass( object ):

    def getThis( self ):
        return self._hidden_variable * 2

    def setThis( self, value ):
        self._hidden_variable = float(value) / 2
    this= property( getThis, setThis )

C = Foo("Rahul")
p = C.name

print p

C.name = "Biswas"
print C.name
        
        
print dir(C)
C.__getattribute__('name')



        