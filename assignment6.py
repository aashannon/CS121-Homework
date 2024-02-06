#Aaron Shannon
#CS 121 T/Th




"""
I am sure you are all used to the drill by now,
just submit your assignment6.py to autolab. Make
sure that you include the main function and any
tests that you ran.

Rubric:
20 points backupFile()
10 points addSemester()
20 points reverseLine()
20 points storeTabDelimitedFile()
10 points main() and tests
20 points style and comments 
"""


def backupFile(inputFile, outputFile):

    #Copies information from one file and saves it to another
    with open(inputFile, 'r') as origin:
        with open(outputFile + '.bak','w') as destination:
            fileContent = origin.read()
            destination.write(fileContent)
        print(fileContent)

def addSemester(inputFile, outputFile):

    #List of Fall Classes
    fall = ['121', '215', '223', '260']

    #Checks list of classes against a list, then adds 'Spring' or 'Fall'
    #to the appropriate line
    with open(inputFile,'r') as oldSemester:
        with open(outputFile, 'w') as newSemester:
            for line in oldSemester:
                line.strip()
                newList = line.split()

                if newList[1] in fall:
                    newList.append('fall\n')
                else:
                    newList.append('spring\n')

                newLine = ' '.join(newList)
                newSemester.write(newLine)
                print(newLine)

def reverseLine(inputFile, outputFile):
    
    backwardsList = []

    #Reverses the order of the words in each line
    with open(inputFile, 'r') as forward:
        with open(outputFile, 'w') as backwards:
            for line in forward:
                if line[-1] == '\n':
                    writeNewLine = True
                else:
                    writeNewLine = False
                
                line.strip()
                newList = line.split()
                backwardsList = newList[::-1]
                newLine = ' '.join(backwardsList)
                backwards.write(newLine)
                if writeNewLine == True:
                    backwards.write('\n')
                print(newLine)


def storeTabDelimitedFile(inputFile):

    matrix = []

    #Splits the lists on the Tab and adds the lists to the matrix
    with open(inputFile, 'r') as f:
        for line in f:
            newList = line.split('\t')
            matrix.append(newList)
        print(matrix)
        return matrix




def main():
    reverseLine('tabTricky.txt', 'tabTrickyOut.txt')
    backupFile('test.txt', 'backuptest.bak')
    addSemester('classes.txt', 'newClasses.txt')
    storeTabDelimitedFile('classes.txt')


if __name__ == '__main__':
    main()
