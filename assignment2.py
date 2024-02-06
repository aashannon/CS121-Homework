#Aaron Shannon
#CS 121
#T/TH, Wed Lab

def fib(n):
    """_Implement this method_

    Method should take as input a number
    Return None if number is negative
    Otherwise return final fib number in sequence
    Must use recursion"""
    if n < 0:
        return None

    elif n == 1:
        return 1

    elif n == 0:
        return 0

    else:
        return fib(n-1) + fib(n-2)



print(fib(9))
