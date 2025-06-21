"""
Functions grow bigger and bigger
Its important to seperate code into different files called modules basing on their functionality; makes it easy to read.
Its easier to read shorter lines of code
 A module is a logical seperation of functions into files according to their functionality
"""
#
# After creating functions, it is important to seperate the code based on their functionality to avoid long code.
# Modules are python files that have reusable code or functions. 
# A python Script/file is a module
# A Module helps access a value returned from a function from one file into another file.
# It's only able to share if the file has a dynamic function.

def Add(num1, num2):
    Ans = num1 + num2
    return(Ans)

def Sub(num3,num4):
    Answer = num4 - num3
    return(Answer)

def Multiply(num1, num2):
    Answer = num1 * num2
    return(Answer)

def Div(num3, num4):
    Ans = num3 / num4
    return(Ans)