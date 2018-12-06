#Aaron Taylor CSCE355-001 Project
#DFA Simulator
import sys

def main():
    
    numOfStates = 0
    acceptStates = []                               #Initializing
    alphabet = []
    
    dfaDesc = open('bigDFA.txt', 'r')               #TODO Change to Sys Arg

    #Total States
    currentLine = dfaDesc.readline().rstrip('\n')   #nextLine, removes \n
    numOfStates = int(currentLine[18:])             #pop Total S
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
    alphabet = splitLine
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
    
    dfaDesc.close                                 #closes file after reading data

    dfaInput = open('bigDFA-strings.txt', 'r')
    line = dfaInput.readline().rstrip('\n')
    line = dfaInput.readline().rstrip('\n')
    line = dfaInput.readline().rstrip('\n')
    print(len(line))

    

