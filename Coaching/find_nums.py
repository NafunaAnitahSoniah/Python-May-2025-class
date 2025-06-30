# a function to identify integers from strings within a list
def id_integers(any_list):
    integerList = []
    stringList = []
    for item in any_list:
        if type(item) == str:
            stringList.append(item)
        elif type(item) == int:
            integerList.append(item)
        else:
            print(type(item))
    result = {"integers": integerList, "strings": stringList }
    return(result)

#print(id_integers([1, 2, 3, 4, 5, "One", 4, "six", 7, "twenty"]))

print("--------")

# a function to identify prime numbers 
def primes(my_list):
    primeNumbers = set()
    odds = set()
    for item in my_list:
        if item % 2 != 0:
            odds.add(item)
        else:
            pass
    for num in odds:
        if num > 1 and num != 9:
            for i in range(2,num):
                if num % i == 0:
                    pass
                else:
                    primeNumbers.add(num)
    return(primeNumbers)
randomNumbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def isPrime(num):
    if num <= 1:
        return(False)
    if num == 2:
        return(True)
    if num % 2 == 0:
        return(False)
    import math 
    for i in range(3, int(math.sqrt(num)) + 1,2):
        if num % i == 0:
            return(False)
    return(True)

def primes2(myList2):
    primeNumbers = []
    for item in myList2:
        if isPrime(item):
            primeNumbers.append(item)
    return(primeNumbers)

print(primes(randomNumbers))

print(primes2(randomNumbers))



            
            


# a function to identify odd numbers
# a function to identify even numbers
# a function that can add numbers 