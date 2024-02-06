#Aaron Shannon
#CS 121



import time

def primeBattle(low, high):
    """_Implement this method_

    Write a function which will find all such numbers which are divisible by 7
    but are not a multiple of 5, between low and high (both included).The
    numbers obtained should be stored in a list. The function returns said list."""
    myList = []

    for i in range(low, high + 1):
        if i % 7 == 0 and i % 5 != 0 and i >= 1:
            myList.append(i)
    return myList

#Factorial as covered in class
def facRec(n):
    if n <= 1:
        return 1
    else:
        return n*facRec(n-1)

def facForLoop(n):
    """_Implement this method_

    Write a function which will use a FOR loop to compute the factorial of n"""
    
    facNum = 1
    for i in range(1, n+1):
        facNum = facNum * i
    return facNum

def facWhileLoop(n):
    """_Implement this method_

    Write a function which will use a WHILE loop to compute the factorial of n"""
    facNum = 1
    counter = 1
    while counter <= n:
        facNum = facNum * counter
        counter += 1
    return facNum

def testFactorialTimes():
    """
    This is a handy function which will print the output and times of each method.
    Feel free to use this to test your methods and compare how long they take.
    Which one is the fastest? 
    """
    n = 5
    print('Testing Recursion...')
    start = time.time()
    results = facRec(n)
    end = time.time()
    print('Total Time: ', end-start, 'Results: ', results)

    print('Testing While Loop...')
    start = time.time()
    results = facWhileLoop(n)
    end = time.time()
    print('Total Time: ', end-start, 'Results: ', results)

    print('Testing For Loop...')
    start = time.time()
    results = facForLoop(n)
    end = time.time()
    print('Total Time: ', end-start, 'Results: ', results)



def coolMatrix(x, y):
    """_Implement this method_

    Write a function which takes 2 digits, x,y as input and generates a 2-dimensional
    list. The element value in the i-th row and j-th column of the array should be i - j.
    Note: i=0,1, ..., x-1; j=0,1, ..., y-1. Suppose the following inputs are given to 
    the program: x=3, y=5. Then, the output of the program should be:
    [[0, -1, -2, -3, -4], [1, 0, -1, -2, -3], [2, 1, 0, -1, -2]]"""
    
    matrix = []

    if x <=2 and y <= 2:
        return []

    else:
        for i in range(x):
            col = []
            for j in range(y):
                cell = i-j
                col.append(cell)
            matrix.append(col)
        return matrix


# print(primeBattle(-50,50))
# print(facForLoop(5))
# print(facWhileLoop(5))
# print(coolMatrix(3,5))