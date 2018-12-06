#Aaron Taylor CSCE355 Project
#DFA Simulator
import sys

#Initializing
acceptStates = []                               
alphabet = []
args = sys.argv

dfaDesc = open(args[1], 'r')                    #input[1] from cmdLine = DFA.txt 

#Total States
currentLine = dfaDesc.readline().rstrip('\n')   #nextLine, removes \n
numOfStates = int(currentLine[18:])             #removes "Number of States:"
####print('Total States: ' + str(numOfStates))      

#Accepted States
currentLine = dfaDesc.readline().rstrip('\n')
acceptStates = currentLine[18:]                 #removes "Accepted States:"
acceptStates = acceptStates.split(' ')
###print('Accepted States: ' + str(acceptStates))

#Alphabet
currentLine = dfaDesc.readline().rstrip('\n')
splitLine = currentLine.split(' ') 
splitLine.pop(0)                                #removes "Alphabet: "
for i in splitLine:
    a = str(i)                                  #populates temp array with splitLine[i]
    alphabet = a                                #alphabet[] = temp[]
###print('Alphabet: ', alphabet)

#Transition Table
columnList = []                                 #List
for i in range(numOfStates):
    currentLine = dfaDesc.readline().rstrip('\n')
    splitLine = currentLine.split(' ') 
    rowList = []                                #List x List
    for j in range(len(splitLine)):
        rowList.append(int(splitLine[j]))       #Append Char
    columnList.append(rowList)

dfaDesc.close                                   #closes file after reading data



#Transitions and Output
with open(args[2], 'r') as dfaInput:             #input[2] from cmdLine = DFA-strings.txt 
    count = len(open('biggerDFA-strings.txt').readlines())
    for c in range(count):
        currentLine = dfaInput.readline().rstrip('\n')
        currentToken = ''
        currentState = 0
        tranTableRow = columnList[int(currentState)]
        inputString = currentLine
        for j in range(len(inputString)):
            currentToken = inputString[j]
            for k in range(len(alphabet)):
                if(alphabet[k] == currentToken):
                    #print('Current Token: ', str(currentToken))
                    #print('Current State: q', str(currentState))
                    #print('Transition to: q', str(tranTableRow[k]))
                    currentState = tranTableRow[k]
                    tranTableRow = columnList[currentState]
        #Final State Comparison
        for i in range(len(acceptStates)):       
            acceptInt = int(acceptStates[i])
            if(acceptInt == int(currentState)):
                printString = 'accept'
                break
            else:
                printString = 'reject'
        print(printString)        
    dfaInput.close
        
        


    
    

