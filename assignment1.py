#Aaron Shannon
#CS 121



import time

def milesToKilo(miles):
    """_Implement this method_

    Write a function that will convert miles to kilometers and return the result"""
    return miles * 1.609344

def milesToKiloTest(value, test):
    """_Implement this method_

    Write a function that will comapre the milesToKilo() function result with
    the parameter test. If they are the same, then return true. Otherwise, false"""
    if milesToKilo(value) == test:
        return True
    else:
        return False

def builtIn1(x):
    """_Implement this method_

    Calculate x to the power of 3"""
    return pow(x,3)

def builtIn2(x):
    """_Implement this method_

    Convert x to an integer by truncating"""
    return int(x)

def builtIn3(x):
    """_Implement this method_

    Convert x to an integer by rounding"""
    return round(x)

def builtIn4(x):
    """_Implement this method_

    Take the absolute value of x and convert it to a floating point number."""
    return float(abs(x))


#print(milesToKilo(20))
#print(builtIn1(2))
#print(builtIn2(3.14))
#print(builtIn3(3.678))
#print(builtIn4(-2))