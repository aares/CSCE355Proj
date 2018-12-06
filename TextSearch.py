#Aaron Taylor CSCE355 Project
#Text Searcher
import sys

def main():
    #Initializing
    alphabet = 'abcdefghijklmnopqrstuvwxyz'         #set alphabet
    args = sys.argv                                 #receive args input
    inputStringFile = open('str1.txt', 'r')         #input[1] from cmdLine = strX.txt
    inputString = inputStringFile.readline().rstrip('\n')#inputString = firstLine of strX
    strLen = len(inputString)                       #Length for iterator and print

    #Transition Table
    columnList = []                                 #List
    for i in range(strLen):                         #iterate thru inputString length
        rowList = []
        repeatArray = []
        repeatIterator = 0
        currentToken = inputString[i]               #get currentToken from inputString
        
        for j in range(len(alphabet)):              #iterate thru alphabet length
            rowList.append(0)                       #populate blank row [0,0,,,,0], where len rowList = alphabet

        for j in range(len(alphabet)):              #iterate thru alphabet tranTable[j]
            if (alphabet[j] == currentToken):       #if currentToken == value on tranTable[j]
                rowList[j] = i+1                    #set tranTableRow[j] to i+1 (value of the state)
        columnList.append(rowList)

    #appends final row of Transition Table   
    finalRowList = []   
    for k in range(len(alphabet)):
       finalRowList.append(strLen)
    columnList.append(finalRowList)

    #Print Output
    print("Number of states: " + str(strLen+1))
    print("Accepting states: " + str(strLen))
    print("Alphabet: " + alphabet)
    for i in range(len(columnList)):
        print(columnList[i])

    
