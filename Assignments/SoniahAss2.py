
#below is a string variable assigned a name "some_string"
some_string = 'Python is fun' 

#the statement below declares and assigns variables a, b, c
a, b, c = 5, 3.2, 'Hello'

print(a)  # prints the value assigned to a
print(b)  # prints the value assigned to b
print(c)  # prints the value assigned to c which is string.

#the statement below declares and assigns variable num1
num1 = 5

#returns the data type of num1 in a sentence as indicated below
print(num1, 'is of type', type(num1))

#the statement below declares and assigns variable num2
num2 = 2.0

#returns the data type of num2 in a sentence as indicated below
print(num2, 'is of type', type(num2))

#the statement below declares and assigns variable num3
num3 = 1+2j

#returns the data type of num3 in a sentence as indicated below
print(num3, 'is of type', type(num3))

#below is a list assigned to a variable name "languages". A list is a mutable, ordered group of elements defined by square brackets.
languages = ["Swift", "Java", "Python"]

#prints the element in position index 0 
print(languages[0])   # the element in position index 2 Swift

# prints the element in position index 2
print(languages[2])   # the element in position index 2 is Python

#Below is a tuple containing both strings and integers, assigned to a variable name "product". A tuple is an ordered list of elements defined by parentheses(), whose elements can not be modified after creation 
product = ('Microsoft', 'Xbox', 499.99)

# prints the element in position index 0
print(product[0])   # Microsoft is the element in position index 0

# prints the element in position index 1
print(product[1])   # Xbox is the element in position index 1 

#Below is a dictionary assigned to a variable name "capital_city". A dictionary is a collection of values, each stored in a key.
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
#prints each key in the dictionary with its value
print(capital_city)


#below is a set assigned to a variable name "student_id". A set is an unordered collection of unique elements defined by curly brackets{}.
student_id = {112, 114, 116, 118, 115}

# prints the set
print(student_id)

# prints the data type of the variable "student_id", which is a set
print(type(student_id))

# a list assigned to the variable name, fruits. A list is a mutable, ordered group of elements defined by square brackets.
fruits = ["apple", "mango", "orange"] 
#prints the list
print(fruits)

#a tuple of integers. A tuple is an ordered list of elements defined by parentheses(), whose elements can not be modified after creation.
numbers = (1, 2, 3) 
#prints the tuple
print(numbers)

#Below is a dictionary. A dictionary is a collection of values, each stored in a key. 
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
#Prints the keys in the dictionary together with their values
print(alphabets)

#below is a set assigned to a variable name "vowels". A set is an unordered collection of unique elements defined by curly brackets{}.
vowels = {'a', 'e', 'i' , 'o', 'u'} 
# prints the set
# And each time this function is run, the elements are printed in a different order because the elements in a set are unordered
print(vowels) 

# below is a set assigned to a variable name "student_id". A set is an unordered collection of unique elements defined by curly brackets{}.
student_id = {112, 114, 116, 118, 115,114,116}

# prints the set
# but since each element in a set must be unique, 116 is printed once.
# And each time this function is run, the elements are printed in a different order because the elements in a set are unordered
print(student_id)

# display the data type of student_id 
print(type(student_id)) 

#Below is a tuple containing both strings and integers. A tuple is an ordered list of elements defined by parentheses(), whose elements can not be modified after creation.
product = ('Microsoft', 'Xbox', 499.99)

#prints the element in index position 0
print(product[0])   # the element in index position 0 is 'Micrososft'

# prints the element in index position 1
print(product[1])   # Xbox is the element in position index 1

#below are declared variables a and b
a = 7
b = 2

# Adds a and b
print ('Sum: ', a + b)  

# subtracts b from a
print ('Subtraction: ', a - b)   

# multiplies a by b
print ('Multiplication: ', a * b)  

# divides a by b
print ('Division: ', a / b) 

# divides a by b and only returns the whole number
print ('Floor Division: ', a // b)

# divides a by b and returns the remainder
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b)   

# a variable declared and assigned a value, 10
a = 10

#a variable declared and assigned a value, 5
b = 5 

# additional assignment statement
a += b      #this statement is the same as, a = a + b
print(a) # Output:15, prints the new value of a after adding b to it

# below is a logical statement that checks if a is the same as b, and returns a value "False" since they are not the same.
print('a == b =', a == b)

#below is a logical statement that checks if a is not the same as b, and returns a value "True" since they are not the same.
print('a != b =', a != b)

#below is a logical statement that checks if a greater than b, and returns a value "True" since a is numerically greater than b 
print('a > b =', a > b)

# below is a logical statement that checks if a less than b, and returns a value "False" since a is numerically greater than b 
print('a < b =', a < b)

# below is a logical statement that checks if a greater than or equal to b, and returns a value "True" since a is numerically greater than b 
print('a >= b =', a >= b)

# below is a logical statement that checks if a less than or equal to b, and returns a value "False" since a is numerically greater than b 
print('a <= b =', a <= b)

#below is a logical statement that checks if a greater than b, and if b is greater than 6
#returns a value "False" since one of the statements b >= 6 is false.
# the logical operator "and" will give a "True" value only and only if all conditions are true  
print((a > 2) and (b >= 6)) 

# Logical 'and'. Returns a "True" value only and only if both statements are true
print(True and True)     # both statements are true hence the computer returns the value "True"
print(True and False)    # returns the value "False" because one condition is false

# logical OR
print(True or False)     #returns a value "True" if atleast one of the conditions is true

# prints a boolean value
print(not True)   #when something is not true, its false, hence the function returns a value "False" 

#below are declared variables
x1 = 5 
y1 = 5
x2 = 'Hello' #a string
y2 = 'Hello' #a string
x3 = [1,2,3] #a list
y3 = [1,2,3] #a list


#below is a function with an identity operator "is not" which returns a value "True" or "False" basing on the condition
print(x1 is not y1)  # checks if the variable x1 is not the same as variable y1, returns a value "False" because the value assigned to x1 is the same as that assigned to y1

#below is a function with an identity operator "is" which returns a value "True" or "False" basing on the condition
print(x2 is y2)  # checks if variable x2 is the same as variable y2; returns the value "True" because the value assigned to variable x2 is the same as that assigned to y2.

#below is a function with an identity operator "is" which returns a value "True" or "False" basing on the conditio
print(x3 is y3)  #checks if the variable x3 is the same as variable y3; the list assigned to variable x3 is exactly the same as that assigned to variable y3
#However the function returns the value "False" because the "is" operator deals with values not objects.

#below is a declared variable, "message" 
message = 'Hello world'

#Below is a dictionary. A dictionary is a collection of values, each stored in a key.
dict1 = {1:'a', 2:'b'}

#below is a membership operator 'in' nested in a print function which returns a boolean value, True or False after checking the specified condition  
print('H' in message)  # checks if the string "Hello World" has a character "H" and if its there, returns a value "True"

#below is a membership operator "not in" nested in a print function which returns a boolean value, True or False after checking the specified condition  
print('hello' not in message)  # checks if the string "Hello World" does not have "hello" in it, and it not being there; returns a value "True". Python is character sensitive.

# below is a membership operator 'in' nested in a print function which returns a boolean value, True or False after checking the specified condition  
print(1 in dict1)  #checks if the key "1" in the dictionary "dict1" above exists, and its there, returns a value "True". 

# below is a membership operator 'in' nested in a print function which returns a boolean value, True or False after checking the specified condition  
print('a' in dict1)  #checks for the key "a" in the dictionary "dict1" above; since its not there, returns a value "False". To call a value from a dictionary, you use the key, not the value itself


# Below is a set assigned to a variable name "animals". A set is an unordered collection of unique elements defined by curly brackets{}.
animals = {'goat','cows', 'cat','zebra','cow','cows'}

#the variable 'animal' used below hasn't been defined, the right variable is 'animals'
print(animals) #I have corrected the variable name to 'animals' and also removed the square brackets. The elements in a set are unordered hence have no indices assigned.
#Since a set doesn't allow repetition, the computer will print the elements in the list with the repeated element "cows" appearing once


#Before correcting the syntax of the block of code above, the computer was not running the following code. When python meets an error, it stops running at that point.

#Below is a tuple of integers. A tuple is an ordered list of elements defined by parentheses(), whose elements can not be modified after creation.
integr_id = (112, 114, 116, 118, 115,114,116)

print(integr_id[0] + integr_id[-1]) #The print function is used to show the answer on the computer screen after adding the integer in index 0 to the integer in index -1
# The positive indices are used when reading from left to right and negative indices are used when reading from right to left
#The integer in index [0] is 112 and the integer in index [-1] is 116
#The computer adds them and displays the answer, 228.





























