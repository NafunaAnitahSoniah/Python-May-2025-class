#We use loops to order a computer to do something/ iterate through a given task until a certain condition is false
#the false condition gives the computer a stoppage point otherwise the computer memory maybe overwhelmed

#FOR LOOP
for item in range(10):  #range is a function
    print(item) #computer will print from 0 to 9

for item in range(1,10):
   print(item)

for item in range(1,10,2): #the last figure '2' gives what the computer should increment the value '1' by when printing
    print(item)

name = "Soniah" #a string is a group of characters
for item in name: #the function 'item' iterates each individual letter in the string 'Soniah'
    print(item) #the computer will then print one by one character 

for letter in name: #the function 'letter' iterates each individual letter in the string 'Soniah'
    print(letter) #the computer will then print one by one character 

for character in name: #the function 'character' iterates each individual letter in the string 'Soniah'
    print(character) #the computer will then print one by one character 

numbers = [2, 3, 67, 90, 600, 10]

countries = ["Uganda", "Kenya", "Hungary", "Germany", "Poland", "Sweden"]

cities = ["Kampala", "Cairo", "Nairobi", "Frankfurt", "Paris", "London"]

for country in countries:
    print(country)
# "Country" is a swap space; it is a temporary memory
# sort of a counter where everything is first received before it goes somewhere.
#the computer accesses the value individually, one by one
#same appliesin the for loop below, but in this case our items are cities
for city in cities: 
    print(city)

#to print Uganda and Kenya from the countries list
for country in countries:
    if country == "Uganda":
        print("************")
        print(country)
    elif country == "Kenya":
        print("************")
        print(country)
    else:
        pass #means ignore the rest; tells the computer to stop printing when the condition is met

#to print Frankfurt and Paris
for city in cities:
    if city == "Frankfurt":
        print("************")
        print(city)
    elif city == "Paris":
        print("*********")
        print(city)
        print("***********") #used to demarcate output and make the code readable
    else:
        pass

for number in numbers:
    if number % 2 == 0:
        print(number)


for number in numbers:
    if number % 2 != 0:
        print(number)

#Using a for loop and if statement, print out even numbers between 1 and 100
for number in range(1,100): #prints even numbers; where it finds an odd number, it prints the else condition
    if number % 2 == 0:
        print("*******")
        print(number)
    else:
        print("All numbers are odd")

for number in range(1,100): #prints even numbers only
    if number % 2 == 0:
        print("*******")
        print(number)
  

for number in range(1,100,2): #to print odd numbers only
    if number % 2 != 0:
        print("*******")
        print(number)
  
for number in range(1,100): #prints odd numbers, where it finds an even number, it prints the else condition
    if number % 2 != 0:
        print("*******")
        print(number)
    else:
        print("All numbers are even")

for number in range(1,100,2): #to print odd numbers only
    if number % 2 != 0:
        print("*******")
        print(number)
    else:
        pass


#WHILE LOOP
#one of the least used loops because as it iterates into the values, it checks the conditions atleast once
#usaually evaluates to "True" so it won't close
var1 = 1
while var1 <= 3:
    print("=======")
    print(var1)
    var1 += 1

#try to avoid loops if possible 




