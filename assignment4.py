def squareOdds(x):
    """_Implement this method_

    Return a list containing all odd numbers squared. 
    For example if x=[1,2,3,4], then squareOdds(x) 
    would return [1,9]."""

    return [i*i for i in x if i % 2 !=0]

def spaces(x):
    """_Implement this method_

    Using list comprehension, return a list containing only the 
    spaces in the function. For example, if x='how are you today?', 
    spaces(x) would return [' ', ' ', ' ']."""

    return [i for i in x if i == ' ']

def specialChars(x):
    """_Implement this method_

    Return a list containing the index of all the special characters 
    $, !, @, &. The format should be a string such that 'xy' where 
    x is the position of the string and y is the position of the 
    character in that string. For example, if x = ['he!!o', 'w@rld'], 
    then specialChars(x) would return ['02', '03', '11']"""
    
    specialList = ['$', '!', '@', '&']
    newList = []

    for i in range(0, len(x)):
        for j in range(0,len(x[i])):
            for k in specialList:
                if x[i][j] == k:
                    newList.append(str(i)+str(j))
    return newList

def evenIndex(x):
    """_Implement this method_

    Return a list containing the index of every even number at an even 
    index. For example, if x = [2, 4, 3, 3, 4, 5], then evenIndex(x) 
    would return [0, 4]."""
    
    newIndex = []

    for i in range(0, len(x)):
        if i % 2 == 0 and x[i] % 2 == 0:
            newIndex.append(i)
    return newIndex


def main():

    print(squareOdds([1,2,3,4,5]))
    print(spaces('There are things you do not know'))
    print(specialChars(['he!!0', 'w@rld']))
    print(evenIndex([2, 4, 3, 3, 4, 5, 6, 8, 9, 8, 8]))


if __name__ == '__main__':
    main()