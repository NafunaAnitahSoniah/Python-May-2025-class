# Below are the different data types we have in Python
#NUMERIC DATA TYPES; Integers (int), Floating(float) numbers and Complex numbers (complex)
#STRING; which is represented by "str"
#SEQUENCE; Here we have list, tuple, range
#MAPPING; dictionary {dict}
#BOOLEAN; (bool)
#SET and FROZEN SET

#INTEGER VALUES
#These are whole number values
num = 50
print(num, "is of a type", type(num))

#FLOAT VALUES
#These are values with decimal points/ floating points
num2 = 50.5
print(num2, "is of a type", type(num2)) #floats are decimal fractions

#COMPLEX NUMBERS
num6 = 1 + 2j
print(num6, "is of a type", type(num6))

#STRINGS
#values in quotes are treated as strings
name = "Soniah"
print(name, "is of a type", type(name))
num3 ="10000" #in this case 10000 will be treated as a string
print(num3, "is of a type", type(num3))

#TYPE CASTING
#The process of transforming a value from one data type to another
num4 = int(num3) #the computer will the store it as an interger
print(num4, "is of a type", type(num4))
num5 = float(num3) #the computer will the store it as an float
print(num5, "is of a type", type(num5))
#however, the name "Soniah" can not be converted into a float or an integer

#LIST []
#these are variables that store more than one value
#A group of values accessed from one memory location
#Other languages may call it an array
#Lists are identified by square brackets []
languages = ["Luganda", "Lusoga", "Lugwere", "Lugisu", "Lunyankole"]
languages2 = ["Python", "JavaScript", "C++", "PHP", "Jango"] #all these values will be accessed from the same memory location.
print(languages, "is of a type", type(languages))
#to print something from a list
#this can be done by indexing, so the first string in the list, 
# "Luganda" is in index 0 if we are moving from left to right (this is called 'positive indexing')
# "Luganda" is also in index -5 when moving from right to left(this is called 'negative indexing')
print(languages[0])
print(languages[-5])
print(languages2[3])

lang3 = [] #memory stores spaces for variables to be added
#you can have an empty list but you can't have an empty variable e.g. var2 =  (can't leave it blank, it will be an error)

my_stuff = [10, 20, "20", "Dennis"]
print(my_stuff[0])
#the list below is a three dimensional list
#Dimensions are the number of square brackets in a list
all_languages = ["luganda", "lugwere", "lugisu", ["python", "javascript", "jango", ["binary","assembly"]], "Stephen"]
print(all_languages[-1][-2])
print(all_languages[3][1])
print(all_languages[3][-1][0])
all_languages.append("Soniah") #A list is mutable like we have just done here
print(all_languages)
#other operations we can do on list are; pop, delete
all_languages.pop() #removes the last element in a list
print(all_languages)


#Tuples, lists and dictionaries all stores multiple data
#Tuples and lists uses indices but dictionaries don't

#TUPLE ()
#Tuples are identified by parentheses (We use oval brackets)
cars = ("benz", "mazda", "subaru", "Vitz", "probox", "allex")
print("------")
print(cars[-1]) #a tuple is immutable, this line would indeed give an error
#but if one of the elements in the tuple is a list, we can manipulate only the values, in the list.
cars = ("benz", "mazda", "subaru", "Vitz", "probox", "allex", ["Cadillac", "limousine", "bughatti"])


#DIFFERENCES BETWEEN LIST AND TUPLE
#List uses square brackets[] but tuple uses parentheses()
#In tuples, you can't programmatically manipulate or update the values in the list but a list can be programmatically manipulated
# i.e. Data in a tuple is read-only (immutable) and a list is mutable

#DICTIONARY DATA TYPE
#Identified by braces {} also known as moustache brackets
#Dictionaries have an arrangement of a key paired with its value. 
# A dictionary stores more than one value but each value is given a customed key. To call that value, use the key name 
# The values are stored in memory locations named by the keys you give e.g. "name"
#In dictionaries we use keys instead of indices
# The key is seperated from a value by a colon ':'
person = {"name" : "Soniah", "age" : 25 , "gender" : "female", "origin" : "Butebo"} 
print(person["name"])

#SET data type
#Is also identified by braces {}
#a set is an unordered collection of unique items
fruits = {"mangoes", "oranges", "grapes", "apples", "oranges", "watermelon", "apples", "pineapple"}
print(fruits) #each time you print, the order of the values will change and no duplicates will be presented

#read about python boolean data type
#what is the difference between null and empty 

#BOOLEAN data type
# One of the value, 'True' or 'False'
# Case sensitive, must be written with a capital 'T' for True and capital 'F' for False
#Boolean values are the result of a comparison statement whose logic either emits 'True' or 'False'