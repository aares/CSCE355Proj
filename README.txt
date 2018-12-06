Aaron Taylor CSCE355 Project:
Contains the following:
  DFA Simulator:
    Reads DFA description from text file, as well as input strings to check if they pass the DFA
  Text Searcher:
    Constructs standard output of an exclusive acceptance DFA based on one input string
    Attempted to create a 2ndary comparison array, where if(compare[i] != inputString[0...n]), breaks loop and replaces char in the  
    transition table (if the loop iterates 2 times, goes to the appropriate index in the table, and replaces 0 with a 2 so that the 
    machine skips to state 2). Couldn't figure out specifics unfortunately. Happens
