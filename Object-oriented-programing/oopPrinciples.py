"""
PRINCIPLES OF OOP

There are four principles of OOP

Principles are theguiding rails/ foundations of OOP that we must adhere to that drives 
Building blocks of OOP i.e. Methods, properties, classes
"""

# 1 ABSTRACTION
"""
Allows you to concentrate on and define a few details/ functionalities that are most important to the user and ignore the finer back end details
More like generalisation, we look at an animal before focusing on the finer details like size, color, location, age etc
Abstract advocates for hiding complex implementation of something and just expose the most essential one  eg we only focus on the functionality of the remot and not the inner parts like its motherboard, wires etc
"""
#the class below is just defined but the properties, objects are ignored;nthis is an example of abstraction
class Animal:
    pass

#2 ENCAPSULATION
"""
In the real world, objects have a way they limit access to some things
Encapsulation is the ability to put access on control on data

We have access identifiers; Protected
                            Private
                            Controlled
                            
"""
#3 INHERITANCE
"""
Is the ability by a class to take on properties and methods of a superClass

"""
#4 POLYMORPHISM
"""
its the ability of an object to take on more than one form , or be used for more than one function
e.g under the Super class "cars" we have mercedes (under mercedes class, we have different objects like S-class, G-Class, GLE etc), toyotas etc and under toyotas, we have so many different objects under it like rav4, sienta, Prado, Corolla etc
Toyota and Mercedes ae child classes or sub classes or derived classes of the Super/ parent class "cars"

A class can have one or more sub classes and these sub classes taken on all the properties of the Super class in addition to their individual properties

"""
class Pet:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner
#line below adheres to polymorphism because it adheres to the principles of taking on more than one form e.g "+" can be used for addition and also for concatenation
    def sound(self, sound):
        return(f"{self.name} makes {sound}")

pet1 = Pet("Buddy", 3, "Hilda")
print(pet1.sound("hoof hoof"))

class Car:
    def __init__(self, model, owner, color):
        self.model = model
        self.owner = owner
        self.color = color

#below, Toyota inherits the properties of the superclass Car
class Toyota(Car):
    def engine(self, engine_type):
        return f"{self.model} has {engine_type}."
    
toyota1 = Toyota("Hilux", "Soniah", "white")
print(toyota1.engine)("inline")

#below class Truck will take on properties from car through its inheritance of Toyota
class Truck(Toyota):
    def horsePower(self, horsePower):
       return f"{self.model} has {horsePower}."