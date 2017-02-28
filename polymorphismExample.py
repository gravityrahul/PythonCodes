'''
Created on Sep 11, 2013

@author: 502100330
'''

class Animal:
    # Base class Animal. This class doesn't have the method talk. 
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    # derived class but has implemented talk method
    def talk(self):
        return 'Meow!'

##END##

class Dog(Animal):
    # derived class but has implemented talk method but 
    # but this talk is different from that of Cat.method()
    def talk(self):
        return 'Woof! Woof!'

## Create instances of the above class
animals = [Cat('Missy'),
           Dog('Lassie'),
           Animal('Mrs. Louffe'),]

for animal in animals:
    print animal.name + ': ' + animal.talk()
