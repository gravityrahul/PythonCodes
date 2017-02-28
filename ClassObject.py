'''
The following snippet of code helps me to understand various OOP 
concept in Python
'''
class SomeClassObject:
    
    person = None  # <------------------------------ This is a Class Variable, person is a Data Member
    def __init__(self, name):
        SomeClassObject.person=name #<-------------- <ClassObject>.person holds the value <name>
    def display(self):
        print SomeClassObject.person  # <------------ 
        
print SomeClassObject.person # <----------------  Returns the data stored by person

p = SomeClassObject("Rahul")

p.display()

# Calling a class object like a function makes a new instance object. Each time
# a class is called, it creates and returns a new instance object. Instances represent
# concrete items in your programs domain.
# #Each instance object inherits class attributes and gets its own namespace.
# Instance objects created from classes are new namespaces; they start out empty
# but inherit attributes that live in the class objects from which they were generated.
# #Assignments to attributes of self in methods make per-instance attributes.
# Inside class method functions, the first argument (called self by convention) references
# the instance object being processed; assignments to attributes of self create
# or change data in the instance, not the class.


class FirstClass(object):
    def setdata(self, value):
        self.data = value
    def display(self):
        print self.data
        

x = FirstClass()

x.setdata("Rahul Biswas")

x.display()

# # Superclasses are listed in parentheses in a class header. To inherit attributes
# from another class, just list the class in parentheses in a class statements header.
# The class that inherits is usually called a subclass, and the class that is inherited
# from is its superclass.
# # Classes inherit attributes from their superclasses. Just as instances inherit the
# attribute names defined in their classes, classes inherit all the attribute names defined
# in their superclasses; Python finds them automatically when they're accessed,
# if they don't exist in the subclasses.
# # Instances inherit attributes from all accessible classes. Each instance gets
# names from the class its generated from, as well as all of that class's superclasses.
# When looking for a name, Python checks the instance, then its class, then all
# superclasses.


class SecondClass(FirstClass):
    
    def display(self):
        print "Current item is %s" %(self.data)
        
y = SecondClass()
y.setdata("Mac")
y.display()

# Print the MRO of SecondClass
print SecondClass.mro()

# Operator overloading lets objects coded with classes intercept
# and respond to operations that work on built-in types: addition, slicing, printing,
# qualification, and so on.

#  Methods named with double underscores (__X__) are special hooks. Python
# operator overloading is implemented by providing specially named methods to
# intercept operations. The Python language defines a fixed and unchangeable mapping
# from each of these operations to a specially named method.
#  Such methods are called automatically when instances appear in built-in
# operations. For instance, if an instance object inherits an __add__ method, that
# method is called whenever the object appears in a + expression. The method's
# return value becomes the result of the corresponding expression.
#  Classes may override most built-in type operations. There are dozens of special
# operator overloading method names for intercepting and implementing nearly every
# operation available for built-in types. This includes expressions, but also basic
# operations like printing and object creation.
#  There are no defaults for operator overloading methods, and none are
# required. If a class does not define or inherit an operator overloading method, it
# just means that the corresponding operation is not supported for the class's instances.
# If there is no __add__, for example, + expressions raise exceptions.
#  Operators allow classes to integrate with Python's object model. By overloading
# type operations, user-defined objects implemented with classes can act just
# like built-ins, and so provide consistency as well as compatibility with expected
# interfaces.


class Rational(object):
    '''
    A perfect example of operator overloading
    '''
    def __init__(self, numerator=0, demoniator=1):
        self.numer = numerator
        self.denom = demoniator

    def __add__(self,rhs):  #self and rhs are Rational objects
        n1 = self.numer    #numerator of the self object
        d1 = self.denom    #denominator of the self object
        n2 = rhs.numer     #numerator of the rhs object
        d2 = rhs.denom       #denominator of the rhs object
        r = Rational(d2*n1+d1*n2,d1*d2)    #creates a new object with d2*n1+d1*n2 as the numerator, and d1*d2 as the denominator
        return r
    
    def __sub__(self,rhs):
        n1 = self.numer    #numerator of the self object
        d1 = self.denom    #denominator of the self object
        n2 = rhs.numer     #numerator of the rhs object
        d2 = rhs.denom       #denominator of the rhs object
        r = Rational(d2*n1-d1*n2,d1*d2)    #creates a new object with d2*n1-d1*n2 as the numerator, and d1*d2 as the denominator
        return r

    def __str__(self):            #rules for printing our objects
        s = "%d /% d" % (self.numer,self.denom)
        return s
    
a = Rational(2,3)
b = Rational(5,6)

print a+b
print a-b

#Another Example of operator overloading

class ThirdClass(SecondClass):
    
    def __init__(self, value):
        self.data = value
        
    def __add__(self, other):
        return ThirdClass(self.data + other)
    
    def __repr__(self):
        if isinstance(self.data, str):
            return self.data
        else:
            return str(self.data)
    
    def __mul__(self, other):
        return ThirdClass(self.data*other)
    

a = ThirdClass("abc")
print a
print a + "def"
print a * 2
b = ThirdClass(3)
print b
print b + 4
print b * 5

# Another Example of operator overloading

class Integer(object):
    
    def __init__(self, value):
        self.data = value
        
    def __sub__(self, other):
        return Integer(self.data - other)

    def __repr__(self):
        return str(self.data)
    
x = Integer(6)

print x-3

q = list()
print dir(q)

p = dict()
print dir(p)

