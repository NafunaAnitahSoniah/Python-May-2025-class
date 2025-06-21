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

