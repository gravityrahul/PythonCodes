'''
Created on Sep 10, 2013

@author: 502100330
'''
class Pet(object):
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def getName(self):
        return self.name
    
    def getSpecies(self):
        return self.species
    
    def __str__(self):
        # This is a private method
        return "%s is a %s" %(self.name, self.species)


# This is a derived class which will inherit from the base class

class Dog(Pet):
    
    def __init__(self, name, chases_cat):
        # The init of this class has two parameters
        # name and chases_cat which will be a boolean
        Pet.__init__(self, name, "Dog")
        self.chases_cat = chases_cat
        
    def cat_chaser(self):
        return self.chases_cat    
    
    
# Inheritance using super
class Fish(Pet):
    
    def __init__(self, name, swim):
        super(Fish, self).__init__(name, "Fish")
        self.name = name
        self.swim = swim
        
    def can_swim(self):
        if self.swim:
            return True
    
    def __str__(self):
        # You are overriding the method in Pet
        if self.can_swim():
            return "%s is a Fish which can swim" %(self.name)
        else:
            return "%s is a Fish but can't swim" %(self.name)
        
   
    
    
    
    
mister_pet = Pet("spencer", "Dog")

# Instantiating the Pet class

print mister_pet.getName()
print mister_pet.getSpecies()

# Instantiating the Dog class

mr_doggy = Dog("Bronzo", True)
print mr_doggy.getName()
print mr_doggy.getSpecies()
print mr_doggy.cat_chaser()

print mr_doggy

mr_boggy = Dog("Gronzo", False)
print mr_boggy

# Instantiating a fish class

mr_fishy = Fish("Nemo", True)

print mr_fishy.getName()
print mr_fishy.getSpecies()
print mr_fishy

