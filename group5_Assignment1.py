"""
GROUP 5 MEMBERS
1. Nafuna Anitah Soniah
2. Abigaba Hilda
3. Jonathan Aissu

"""


'''
A dynamic function called "tests" has been defined and given parameters test1 and test2 
A dynamic function is a function that gives different outputs when invoked
A function is usually self-contained but "return()" allows it to share the values called upon in the brackets().

'''


def tests(test1, test2):
	#this compares the value of test1 to the value of test2
	if test1 == test2:
		#if the value of test1 is the same as the value of test2, the function returns the value of test1
		return test1
	else:
		#but if the value of test1 is not the same as the value of test2, the function returns the value of test2
		return test2

#Below are input functions that ask the user to enter values of test1 and test2 through their keyboard
#The values entered by the user will be used as the arguments for the tests() function.
#The input function is an in-built dynamic function that enables a user to interact with the program
#The input function captures strings by default, so it has been type-casted to capture integers.
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''
A dynamic function called "courseWrk" has been defined and given a parameter cswork

'''
def courseWrk(cswork):
	#A variable "testMark" has been declared and assigned the value that is returned by the function tests().
	testsMark = tests(test1,test2)
	#this calculates the average of the values of "testsMark" and "cswork" and stores the result as "avgtestsCswork"
	avgtestsCswork = (cswork + testsMark)/2
	# this calculates the final tests coursework mark by taking 40% of the avgtestsCswork and stores the result as "fnltestsCswork"
	fnltestsCswork = avgtestsCswork * (40/100)
	#prints a line of dots. It seperates the outputs and makes them easier to be read
	print('..............................')
	#outputs the final coursework marks
	print('your final coursework marks is: ', fnltestsCswork)
	print('..............................')
#The program user will be asked to enter the value for "cswork"
cswork = int(input('Please enter your course work Marks: '))
#invokes the courseWrk() function.
courseWrk(cswork)