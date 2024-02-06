#Aaron Shannon
#CS 121 T/Th


def logMessage(logFile, message):
    #will open and add a line to the end of the document with a new line

    with open (logFile, 'a') as f:
        f.write(message + '\n')


def getLine(inputFile, lineNumber):
    #Returns specified line content in inputFile or returns None

    counter = 1
    with open (inputFile,'r') as f:
        for line in f:
            if counter == lineNumber:
                return str(line)
            counter += 1

    #edge case for if document is empty or not enough lines
    if lineNumber > counter or lineNumber <1:
        return None


def writeCSV(outputFile, data):
    #Writes data as a string to a new file with data seperated by a comma

    with open (outputFile, 'w') as f:
        for i in data:
            lines = []
            for j in i:
                lines.append(str(j))
            f.write(','.join(lines)+'\n')




def main():
    data = [['cs',121],['cs', 122], ['cs', 223]]
    #Put your tests here!
    #Remember to test as you go!
    logMessage('newClasses.txt', 'Gap')
    getLine('newClasses.txt', 2)
    writeCSV('csvText.txt', data)


if __name__ == '__main__':
    main()