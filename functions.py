#Functions are the backbone of a programming language

#A function is a named block of code (a block of code is a group of related statements performing something)
#Functions logically group your code
# "def" defines a function. A function is defined while a variable is declared
#some funtions are python in-built e.g. "print" function
#Customised functions; functions written by coders

num1, num2 = 10,20
print(num1 + num2)


def Add(): #Add() is the name of the function
    num1, num2 = 10,20
    print(num1 + num2) #won't print (will be ignored) until you call the code to run

Add() #This calls the code to run.

def Subtract(): #name of the function
    num3, num4 = 40,20
    print(num3 - num4) #won't print until you call the code to run

Subtract() #This calls(invokes) the code to run.

#A function can have other functions within it
def even():
    for i in range(10):
        if i % 2 == 0:
            print("--------")
            print(i)
even()

#Any variable within a function can not be accessed outside that function. The function is self-contained

def example1():
    age = 26
    
# print(age) will give an error, because the computer can't access the variable age from the function [example1()] 
#unless a special thing is done, so we have to call upon the function to access it like below

def example1():
    age = 26
    print(age)
example1()


#Functions can communicate with one another

def addition():
    num1, num2 = 30,50
    ans = num1 + num2
    return ans
    print(ans)

def division():
    num3, num4 = 90,3
    ans2 = num3 / num4
    return ans2  #this makes the function ready to share its values; the return statements makes the values accessible outside the function
    print(ans2)

#We want to combine the values from addition() with those from division()

def aggregation():
    print(addition() + division()) 

aggregation()


