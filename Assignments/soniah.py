#Using Python comments explain the following terms to an average Ugandan (senior 4/6 educated person) ;

#Programming: 
#This is the art and science of writing computer instructions that a computer can understand and follow. 
#Instructions are orders that tell a computer what to do and how to do it.

#Variable: 
#This is like a storage container that holds data or values such as numbers, texts which can be manipulated within a program.
#Its a named unit of memeory 
# Its given by a software engineer to values when writing a program
age = 18 #in this example, 'age' is the variable that stores the number 18.

#Partitioning
#This is the division of computer storage into different smaller parts.
#You can divide your phone or computer storage to have one part for music, another for photos, another for your class files or documents.

#Memory address:
#This is a location where a value is stored inside the computer memory. 
#Its a unique numerical identifier created by the computer operating system. The OS is responsible for partitioning your memory and naming the partitions
#The computer assigns a unique address to each value it stores so that it can access it easily.(like a house address)

#Assignment:
#This is when we give a variable a value using the equals(=) sign
age = 18, #we have assigned the variable "age" a value "18".

#Declaring:
#The process of creating variables. We tell the computer that a variable exists 
age = 18, #from this example, we have told the computer that a variable "age" exists and also gone ahead and assigned it a value "18" 

# Comment:
# A comment is a note written within code to explain the code or show other users what you have done
#The computer ignores the comments. They are only for humans to read and understand
#For example in python, the comments start with a "#" symbol

#An operator:
#An operator is special a character or symbol that tells a computer what to do with a certain value. 
#for example to add "+", to subtract "-", multiply "*", to divide "/"

#An operand:
#These are values that an operator works with.
5 + 3; #in this example, 5 and 3 are the operands.  

#Type cast:
#This means changing a value from one data type to another.
"7", #here, the computer reads "7" as a string(word/ text).
#to change "7" to an integer, we do this; 
int("7"); # and now the computer will read 7 as a number.

#Statement
# This is a single line of instructions telling the computer to do something.
print("Soniah is a girl") #this tells the computer to show "Soniah is a girl" on the screen.

#Code:
#A group of two or more statements telling a computer what to do.
#Think of it like a recipe that tells someone how to prepare a dish. But in programming the recipe(code) tells the computer how to perform a task.
 
#Syntax:
# These are like the grammar rules of a programming language.
#They dictate how instructions should be written so that a computer can easily understand and perform yopur desired task.
print("Soniah is a girl"), #python understands this
# print"Soniah is a girl" ;however python will not understand this, hence the error

#Semantics:
#This is refers to the meaning of the code or what we expect a certain code to produce when a program is run.
#For example; we expect 5+3 to give 8.
#We have to write the code rightly so as to get the meaning we desire.
#A code can have the right syntax but wrong semantics


#List any 4 examples of computer memories you know.
#RAM (Random Access Memory)
#HDD (Hard Drive Disk) memory
#Cache memory
#ROM (Read-Only Memory)

#Discuss the relationship between HDD, Ram and CPU in the context of a software engineer.
#The HDD is a long-term memory where the software engineer stores/ saves their code, files and documents.
#The RAM is where the code and data that is actively being used by a computer is stored. The RAM is like a temporary woeking space.
#When the engineer runs a program, the code required to run it is loaded from the HDD(long-term memory) into the RAM
#The active code is temporarily stored in the RAM because the computer accesses the RAM faster than the HDD hence enabling faster execution of a required task.
#The CPU is the brain of the computer that executes the program.
#The CPU fetches the code and data from the RAM and executes the instructions step by step (line by line).
#The CPU can only access data directly from the RAM and not the HDD.
#If anything is changed while running the program, the data is transferred from the RAM to the HDD so that it can be stored permanently.

#If we are to compare this to a cook, the HDD is the store where the cook keeps the food and recipes while the  RAM is the kitchen table where the
#cook puts everything and works from while cooking and the CPU is the cook. The cook only picks things directly from the kitchen table when he starts
#cooking.
#Understanding the relationship between the HDD, RAM and CPU enables a sodtware engineer to write efficient programs. It also helps in debugging, 
#checking performance and optimising programs.

#Using code/statements, demonstrate the use of different Python Operators (the most commonly used, please use comments to discribe the meaning of the operators demonstrated)

#We have six types of operators, namely;
	#Arithmetic operators
	#Assignment operators
	#Logical operators
	#Comparison operators
	#Bitwise operators
	#Special operators

#But the most commonly used ones are;
    #Arithmetic operators
	#Assignment operators
	#Comparison operators
    #Logical operators

#lets use the variables below
var1, var2 = 10,5
 
#ARITHMETIC OPERATORS 
#These include;
	#Addition, +
print(var1 + var2) #this gives 15
	#Subtraction, -,
print(var1 - var2) #this gives 5
	#Multiplication, *
print(var1 * var2) #this gives 50
	#Division, /
print(var1 / var2) #this gives 2.0

#Other operators include;
#	Floor division (//) 
#Here, it gives you only the whole number after the division, truncates the decimal fractions from the answer after division has taken place. 
# E.g. 1//2 = 0, 30//14 = 2
print(var1 // var2) #this gives 2

#	Modular (%) 
#This gives the remainder. It’s an operator that gives you the remainder after a division has taken place. 30//14 = 2
print(var1 % var2) #this gives 0
#When you divide a smaller value by a bigger value, the modular answer is the smaller number i.e. the answer here, 1&2 is 1.
print(var2 % var1) #this gives 5

#	Exponential (**)
#num1 ** num2; value of num1 to the power value of num2
print(var1 ** var2) #this gives 100000

#ASSIGNMENT OPERATORS 
#These tell the computer to put things somewhere
	# (=),
	# +=, additional assignment
	# -= subtraction assignment
	# **= exponential assignment
	# *= multiplication assignment
	# = modular assignment
#For example, with additional assignment,
var = 7, # "=" sign assigns a value 7 to the variable "var"
#When we have var1 += var2; this statement is the same as, var1 = var1 + var2 (i.e the new value of that variable is that variable plus another value)
var1 += var2 #this assigns var1 a new value 15
print(var1 - var2) #the computer will now use the new value of var1 as 15 hence giving 10 as the answer.

#COMPARISON OPERATORS: ==, <, >, >=, <=, !=
#If we have, var3 = 5 and var4 = 2
# == (equal to)
# Var3 == var4, checks if the value is equal to the other

# < (less than)
#var3 < var4, Checks whether var3 is less than var4

# > (greater than)
#var3 > var4, Checks whether var3 is greater than var4

# >= (greater than or equal to)
#var3 > var4, Checks whether var3 is greater than or equal to var4

#<= (less than or equal to)
#var3 > var4, Checks whether var3 is less than or equal to var4" 

# != (not equal to)
# var3 !=  var4, Checks whether var3 is the same as var4
#The computer will check any of the conditions above and either give a ‘false’ or ‘true’ response accordingly.

#LOGICAL OPERATORS: and, or, not
#E.g. when we have 
var5, var6 = 5,6
#and; this operator will only give a ‘true’ response if both conditions are true
print((var5 > 2) and (var6 >=6))
print((var5 ==2) and (var6 >=6)) #if one condition is false, it will return false
print((var5 ==2) and (var6 >=7)) #if both conditions are false, it will return false

#or; this operator will give a true value as long as one of the statements is true.
print((var5 > 2) or (var6 >=6)) 
print((var5 ==2) or (var6 >=6)) #if one conditions is true, it will return true
print((var5 ==2) or (var6 >=7)) #if none of the conditions are true, it will return false

