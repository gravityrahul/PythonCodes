'''
Python attribute tutorial based on Sulabh Chaturvedi's online tutorial
www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html
#method-resolution-order
'''

class C(object):
    '''
    This example illustrates Attribute concepts
    '''
    classattribute="a class attribute"

    def f(self):
        return "function f"
    

cobj = C()

print cobj.f

# if Python finds an object with a __get__() method inside the
# class's __dict__,
# instead of returning the object, it calls the __get__() method and returns
# the result. Note that the __get__() method is called with the instance and the class as the
# first and second arguments respectively.

print C.__dict__['f'].__get__(cobj, C)

# It is only the presence of the __get__() method that transforms an ordinary function into a bound
# method. There is nothing really special about a function object. Anyone can put objects with a
# __get__() method inside the class __dict__ and get away with it. 


# An example of descriptor

class Descriptor(object):
    "A class demonstrating descriptor protocol"
    
    def __get__(self, obj, cls=None): #cls is optional class argument
        pass
    
    def __set__(self, obj, val):
        pass
    
    def __delete_(self, obj):
        pass
    

class C2(object):
    '''
    A class with single descriptor
    '''
    d = Descriptor()
    
    
cobj2=C2()
cobj2.d = "setting a value"
cobj2.__dict__['d']="Try to force a value"
x = cobj2.d

C2.d = "Setting a value on class"
print C2.d

d = Descriptor()
d.__set__(cobj, "setting a value")
print x

#Non-data descriptors

class NonDataDescriptor(object):
    "A class demonstrating descriptor protocol"
    
    def __get__(self, obj, cls=None): #cls is optional class argument
        pass


class C3(object):
    '''
    A class with single descriptor
    '''
    d = NonDataDescriptor()
    
cobj3 = C3()
cobj3.d = "Setting a value for nondata"

print cobj3.d
print cobj3.__dict__

d = NonDataDescriptor()
d.__get__(cobj3, C3)
print d.__dict__