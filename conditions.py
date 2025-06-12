#CONDITIONS IN PYTHON
numbers = [1, 2, 4, 18, 13, 21]

first_name = "Soniah"
second_name = "Nafuna"
if first_name == second_name: 
    print("Your names are similar")
#the computer will just print nothing if the condition is not satisfied; there is no error

if first_name != second_name:  #can also use 'is not' instead of '!='
   print("Your names are not similar")

#a group of statements related to one another performing something is called a "BLOCK"
#line 6 and 7 are related.
#if condition is a block 
# a block of code is identified by a colon ':' at the end e.g. in line 6 and 10
# after a colon

#you can have more than one condition, giving you an alternative when something is false
# in this case, we use 'if' and 'else'
if first_name == second_name:
    print("Names are similar")
else:
    print("Your names are not similar")

if "x" not in first_name: #recall the use of membership operators like 'in', 'not in'
    print("Your name is for a Ugandan")
else:
    print("You are a normal Ugandan")

#if elif ; used when you have multiple conditions
number = -5 
if number > 0:
    print("positive number")
elif number < 0: #used to add more conditions to your block
    print("negative number")
else:        #closes the block
    print("its a zero")

#ASSIGNMENT
# Read about; switch, case, break, and continue, pass



