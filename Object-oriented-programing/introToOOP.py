
"""
Object Oriented programming is a software paradigm that advocates creating programs based on real life problems
This is the art of writing code that solves real life problems

We have however been dealing with Structured functional paradigms where we step by step 

The building blocks of OOP are
 1. A class #This is the top layer, the overall. 
 By definition, a class is a blue print of an object

 2. An Object
 An object is an instance, an example of a class
 objects belong to classes

How to identify a class where an oblect belongs
A class is identified like this; "is a...."

Classes are defined in singular
A class is also a block

"""
class Person: #class name has to start with a capital letter.
    name = "Soniah"  # "name" is a feature of our object "Soniah"
    age = 23            # the attributes/variables "age", "name", etc they are the properties of a class person.
    location = "Mukono" #the values/operands "Soniah", "23" ; a collection of the values is what we call an object.
    occupation = "Civil Engineer"
    Contact =  "nafunasoniah@gmail.com"
    #Creating a method(function) of a class person
    def Sing(): # the word "Self" is used for individual objects 
        return("This person sings nicely") #this is called a behaviour; its under a method "Sing" which falls under class "Person"
print(Person.Sing()) 

#In OOP; a function is a collection of descriptions of the things an object does to itself or other objects. Its also known as a method
# A behaviour describes how an object does something to itself or to other objects.
# we can have several objects to one definition of a class

class Animal:
    animal_name = "cat"
    a_color = "black"
    a_size = "medium"
    a_skin_texture = "hairy"
    a_owner = "Ange"
    a_location = "Kampala"
    def Sound():
        return("This animal meows") 

print(Person.name) #we use "." operator to access properties of an object in a class
print("The name of an object of an Animal is: ",Animal.animal_name)
print(Animal.Sound())

#create another object that belongs to the class Person
Person2 = Person()
Person2.name = "Joanna"
Person2.age = "18"
Person2.Contact = "joanna12@gmail.com"
Person2.location = "Kampala"
Person2.occupation = "Nurse"


print(Person2.name)

#remember to ask if each object in the class can have seperate methods/ functions