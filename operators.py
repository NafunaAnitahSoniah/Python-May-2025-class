#An operator is special a character or symbol that tells a computer what to do with a certain Value or an operand eg the '=' below
#'age' is the variable
#A statement which is an instruction contains a variable, an operator and a value(an operand) e.g the one below
age = 25 

#We have six types of operators, namely;
#1 Arithmetic operators
#2 Assignment operators
#3 Logical operators
#4 Comparison operators
#5 Bitwise operators; the ampersand "&" (logically means 'and') and the pipe "|" (which means 'or') these are rarely used in python anyway
#6 Special operators

#ARITHMETIC OPERATORS +, -,* (multiplication), / (division)
num1,num2 = 14,30
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)

#other operators include;
#1. floor division (//) here, it gives you only the whole number after the division, truncstes the decimal fractions!
print(num1 // num2)
print(num2 // num1)
#2. Modular (%) (This gives the remainder, its an operator that gives you the remainder after a division has taken place)
print(1%2) #when you divide a smaller value by a bigger value, the modular answer is the smaller number i.e the answer here is 1.
print(num2 % num1)
print(1000000 % 3)
#3. Exponential (**)
print(num1 ** num2) #value of num1 to the power value of num2


#ASSIGNMENT OPERATORS 
# eg (=), (+=, additional assignment),(-= subtraction assignment), (**= exponential assignment), (*= multiplication assignment), (%= modular assignment)
# these tell the computer to put things somewhere
var1 = 10
var2 = 5
#  +=, additional assignment
var1 += var2 # this statement is the same as, var1 = var1 + var2 (i.e the new value of that variable is that variable plus another value)
print(var1)
var1 += 10
print(var1)
#  -= subtraction assignment
var1 -= var2
print(var1)
#  *= multiplication assignment
var1 *= var2
print(var1)
#  **= exponential assignment
var1 += var2
print(var1)
#%= modular assignment
var1 += var2
print(var1)

# COMPARISON OPERATORS: ==, < , >, >=, <=, !=
var3 = 5
var4 = 2
# == (checks if the value is equal to the other)
print("Checking whether var3 is the same as var4", var3 == var4)
# < (less than)
print("Checking whether var3 is less than var4", var3 < var4)
# > (greater than)
print("Checking whether var3 is greater than var4", var3 > var4)
# >= (greater than or equal to)
print("Checking whether var3 is greater than or equal to var4", var3 > var4)
# <= (less than or equal to)
print("Checking whether var3 is less than or equal to var4", var3 > var4)
# != (not equal to)
print("Checking whether var3 is the same as var4", var3 != var4)

#LOGICAL OPERATORS: and, or, not
var5 = 5
var6 = 6
# and (this operator will work if all conditions are true)
print((var5 > 2) and (var6 >=6)) 
print((var5 ==2) and (var6 >=6)) #if one condition is false, it will return false
print((var5 ==2) and (var6 >=7)) #if both conditions are false, it will return false

print(True and True)
print(True and False)
print(True or False)
print(True or True)
print(False or False)
print(not True)
print(not False)

#WEEKEND ASSIGNMENT
#In not more than two pages briefly discuss your learning take aways so far, in your own understanding, from week one of learning Python with Ozzy

#SPECIAL OPERATORS IN PYTHON
#1. Identity operators
#2. Membership operators

#Idebtity Operators
# 'is' and 'is not'
x = 5
y = 5
x2 = "Hello"
y2 = "Hello"
print(x2 is y2) # 'is' is similar to ,'=='
print(x2 == y2)
print(x2 is not y2) #is the same as '!='

#Membership Operators
# 'in' and 'not in'
message = "Hello Ivan the Great!"
print("Hello" in message)
print("Anitah" in message)

#BITWISE OPERATORS 
# 1. the ampersand "&" (logically means 'and') 
# 2. the pipe "|" (which logically means 'or') 
# these are rarely used in python anyway