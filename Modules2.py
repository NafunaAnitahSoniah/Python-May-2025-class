# When we want to access a function from one file, we use a key word "import" then put the name of the file.


import Modules

#After calling the module, we can now access the functions in the module as follows
print(Modules.Add(6, 9))
print(Modules.Sub(7, 9))
print(Modules.Div(9, 3))
print(Modules.Multiply(4, 8))

# One or more modules in a folder with a special file named with "__init__.py" qualifies the folder to be called a package.
#The "__init__.py" file is usually empty
