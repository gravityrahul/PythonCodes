'''
Created on Feb 18, 2014

@author: 502100330

This example shows the difference of using the super vs non super in 
class inheritance. Consider a class as BaseClass which will implement
certain methods. This base class will be used to generate certain derived class. 

Super is useful in case of multiple inheritance and helps in mro. Incase of single 
inheritance, we can safely do away with following

class BaseClass(object):
    
    def __init__(self, params):
        print "This is an old style inheritance"
        

class DerivedClass(BaseClass):
    
    def __init__(self, param, kwparams):
        Baseclass.__init__(self, param)
        pass

'''


class BaseClass(object):
    
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
            
    def printName(self):
        print "I am called from BaseClass"
        print self.name
        
    def setName(self, givenName):
        print "I am called from BaseClass"
        self.name=givenName
        
    def CalledFromThirdGen(self):
        print "I am called from BaseClass and invoked from Third Generation Derived Class"

class FirstGenDerived(BaseClass):
    
    def __init__(self, *args, **kwargs):
        #BaseClass.__init__(self, *args, **kwargs)
        super(FirstGenDerived, self).__init__(*args, **kwargs)
        self.name = kwargs.get('name')
        self.FamilyName = kwargs.get('FamilyName')
        
    def printFullName(self):
        print "I am called from FirstDerivedClass"
        print self.name + ' ' + self.FamilyName
        
    def printName(self):
        print "I am called from FirstDerivedClass, although I was present in BaseClass"
        print "His Highness " + self.name + ' ' + self.FamilyName
        
    
class SecondGenDerived(BaseClass):
    
    def __init__(self, *args, **kwargs):
        #BaseClass.__init__(self, *args, **kwargs)
        super(SecondGenDerived, self).__init__(*args, **kwargs)
        self.name = kwargs.get('name')
        self.middleName = kwargs.get('middleName')
        self.FamilyName = kwargs.get('FamilyName')
        
        
    def printWholeName(self):
        print "I am called from SecondDerivedClass"
        print self.name + ' ' + self.middleName + ' ' + self.FamilyName
        
    def printName(self):
        print "I am called from SecondDerivedClass, although I was present in BaseClass"
        print "Sir " + self.name + ' ' + self.middleName + ' ' + self.FamilyName
        

class ThirdGenDerived(FirstGenDerived, SecondGenDerived):
    
    def __init__(self, *args, **kwargs):
        super(ThirdGenDerived, self).__init__(*args, **kwargs)
    
    

if __name__ == "__main__":
    
    print "Executing BaseClass"
    BaseClass(name='Robin').printName()
        
    print "Executing Instance of BaseClass with SetName \n"
    Instance = BaseClass()
    Instance.setName("Little John")
    Instance.printName()
    print "################################################\n"
    
    
    print "Executing FirstGenDerived with printName and printFullName\n"
    FirstGenDerived(name='Robin', FamilyName='Hood').printFullName()
    FirstGenDerived(name='Robin', FamilyName='Hood').printName()
    print "################################################\n"
    
    
    print "Executing FirstGenderived with instance\n"
    Instance2 = FirstGenDerived(name=None, FamilyName="Hood")
    Instance2.setName("Edwards")
    Instance2.printFullName()
    print "################################################\n"
    
    print "Executing SecondGenDerived with printName and printWholeName\n"
    SecondGenDerived(name='Robin', FamilyName='Hood', middleName='Williams').printWholeName()
    SecondGenDerived(name='Robin', FamilyName='Hood', middleName='Williams').printName()
    print SecondGenDerived.__mro__
    print "################################################\n"
    
    print "Executing ThirdGenDerived\n"
    ThirdGenDerived(name='Robin', FamilyName='Hood', middleName='Williams').CalledFromThirdGen()
    ThirdGenDerived(name='Robin', FamilyName='Hood', middleName='Williams').printName()
    print ThirdGenDerived.__mro__
    print "################################################\n"
