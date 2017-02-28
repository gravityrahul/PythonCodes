'''
Created on Sep 11, 2013

@author: 502100330
'''
"""
In duck typing, one is concerned with just those aspects of an object that 
are used, rather than with the type of the object itself. For example, in a 
non-duck-typed language, one can create a function that takes an object of 
type Duck and calls that object's walk and quack methods. In a duck-typed 
language, the equivalent function would take an object of any type and call 
that object's walk and quack methods. If the object does not have the methods 
that are called then the function signals a run-time error. If the object 
does have the methods, then they are executed no matter the type of the object, 
evoking the quotation and hence the name of this form of typing.
"""

class Duck:
    def quack(self):
        print("Quaaaaaack!")
    def feathers(self):
        print("The duck has white and gray feathers.")
 
class Person:
    def quack(self):
        print("The person imitates a duck.")
    def feathers(self):
        print("The person takes a feather from the ground and shows it.")
    def name(self):
        print("John Smith")
 
def in_the_forest(duck):
    duck.quack()
    duck.feathers()
 
def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)
 
game()