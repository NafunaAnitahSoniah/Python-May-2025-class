"""
DIFFERENT FORMATS OF CREATING CLASSES AND OBJECTS

"""

class Animal:
    #__innit__ function is a special python method that helps us initialise an instanciated object
    # 'self' is very important as a parameter, it is used as a bridge between the properties of the class and the individual values of the objects
    def __init__(self, name, color, owner, skin_texture, size): 
        self.name = name
        self.color = color
        self.owner = owner
        self.skin_texture = skin_texture
        self.size = size
    def Sound(self, sound):
        #return(self.name, "makes sharp scary ", sound)
        # "f" stands for format
        return f"{self.name} makes sharp scary {sound}"

animal1 = Animal("dog", "black", "Soniah", "Hairy", "medium") 
print(animal1.Sound("hoof-hoof"))


class Person:
    def __init__(self, name, age, location, occupation, contact):
        self.name = name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.contact = contact

Person1 = Person("Hilda", "25", "Luweero", "Doctor", "hilda.abigaba@gmail.com")      

