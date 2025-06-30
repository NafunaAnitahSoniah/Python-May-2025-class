#TYPES OF FUNCTIONS
#EXAMPLES OF FUNCTIONS
    # 1. INBUILT FUNCTIONS;
 #functions that come with the Python installation e.g print
                                                     #input
                                                     #pop (deletes what has been added to a list by the "append" function)
                                                     #append (used to add values to a list)
                                                     #delete (used to remove a values from a list)
                                                     #forward etc
                                                     #int
                                                     # sqrt() computes square root
                                                     # pow() computers the power .....input two parameters and argumnts

#A function is called by the function name followed by parentheses e.g. int()


#INPUT FUNCTION
#Helps us write interactive programs or code
#Captures strings by default
# Enables a user to initialise a value from the keyboard

"""
num1 = int(input("Please enter your range limit"))
for number in range(num1):
    if number % 2 == 0:
        print(number)
"""   #the computer ignores this! This is multi-line commenting

#int() is a typecasting function. It changes a value to an integer
#input() produces strings by default, so we type-cast it with int() function so that the input captured from the keyboard is treated as an interger value.
# remember the range() function only works on integers

#   2. USER-DEFINED FUNCTIONS
#Under user-definedfunctions we have; Static functions
                                    # Dynamic functions (parameterised function)

#STATIC FUNCTIONS
#Any function with hard coded values e.g. the function below

def Add():
    num3, num4 = 7,34
    return (num3 + num4)

Add()
print(Add())

"""
#DYNAMIC FUNCTIONS
Also known as paremeterised functions
Will always give a different value when called upon depending on how it is invoke
A dynamic function can always be called upon and used for different purposes
"""
def Multiply(num5, num6): #num5 and num6 are called parameters/ place holders. A parameter list is the number of parameters in the declaration brackets
    return(num5, num6)

print(Multiply(20, 9))
print(Multiply(100, 7))
print(Multiply(987, 3))

#However print(Multiply(20, 9, 7, 6)) will bring an error because the number of variables declared in the brackets should correspond with the number of arguments provided when invoking the function

"""
The numbers we fill into the "print" function are called arguments
Parmeters can be called formal arguments and arguments are actual parameters

The print function is an in-built dynamic function
the "input" is also an in-built dynamic function

Dynamic functions always expect an argument when being invoked

Pop function is not paremeterised, it just deletes the last element in a list

"""

#ASSIGNMENT
#Define a dynamic function that asks a user for their grosspay, deducts PAYE of 30% and returns the netpay

"""
THE BREAKDOWN
We need an input function to tell the user to key in their gross pay
multiply gross pay by 30%
subtract the new value from the gross pay
and return the result as the net pay

"""
def net_pay(gross_pay):
    tax = gross_pay * 0.3
    my_net = gross_pay - tax
    return (my_net)

gross_pay = int(input("Please input your gross pay "))
#result = net_pay(gross_pay)
print("Your net pay after payee is: ",net_pay(gross_pay))

"""
A computer only moves back amd forth in executing lines of code in a dynamic function otherwise, it usually executes from top to down

"""