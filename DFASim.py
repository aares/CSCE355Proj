#Aaron Taylor CSCE355 Project
#DFA Simulator
import sys

def main():

    #Initializing
    currentState = 0
    numOfStates = 0
    acceptStates = []                               
    alphabet = []
    currentToken = ''
    
    dfaDesc = open('bigDFA.txt', 'r')               #TODO Change to Sys Arg

    #Total States
    currentLine = dfaDesc.readline().rstrip('\n')   #nextLine, removes \n
    numOfStates = int(currentLine[18:])             #removes "Number of States:"
    ####print('Total States: ' + str(numOfStates))      
    
    #Accepted States
    currentLine = dfaDesc.readline().rstrip('\n')
    splitLine = currentLine.split(' ')
    splitLine.pop(0)                                #pop "Accepting"
    splitLine.pop(0)                                #pop "States: "

    for i in splitLine:                             #iterate thru line to append
        a = int(i)                                  #temp for int conversion
        acceptStates.append(a)                      #appends ints to acceptList
    ###print('Accepted States: ' + str(acceptStates))

    #Alphabet
    currentLine = dfaDesc.readline().rstrip('\n')
    splitLine = currentLine.split(' ') 
    splitLine.pop(0)                                #pop "Alphabet: "
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



    #Transitionns
    with open('bigDFA-strings.txt', 'r') as dfaInput:#TODO argv

        #while document hasn't finished read
        #lineCount = len(open('bigDFA-strings.txt').readlines())
        currentLine = dfaInput.readline().rstrip('\n')
        if(len(currentLine) == 0):
            currentLine = dfaInput.readline().rstrip('\n')
        if(len(currentLine) != 0):
            for c in range(len(currentLine)):
                inputString = currentLine
                tranTableRow = columnList[int(currentState)]
                for j in range(len(inputString)):
                    currentToken = inputString[j]
                    for k in range(len(alphabet)):
                        if(str(alphabet[k]) == str(currentToken)):
                            print('Current Token: ', str(currentToken))
                            print('Current State: q', str(currentState))
                            print('Transition to: q', str(tranTableRow[k]))
                            currentState = str(tranTableRow[k])
                            tranTableRow = columnList[int(currentState)]
                #Final State Comparison
                """
                for m in range(len(acceptStates)):
                    if(acceptStates[m] != currentState):
                        print('reject')
                    if(acceptStates[m] == currentState):
                       print('accept')
                        break
                """
                
                if any(currentState in acceptStates for i in acceptStates):
                    print('accept')
                else:
                    print('reject')

        dfaInput.close
        
        


    
    

