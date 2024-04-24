
def createACardStack():

    # Different attributes for cards
    color = ["red", "black"]
    pattern = ["spade","heart", "diamond", "club"]
    symbol = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    

    maxCards = 52
    MyCards = []

    #Start value of the first card
    valueNumber = 2

    #Index number for Color container
    colorNumber = 0

     #Index number for Pattern container
    PatternNumber = 0

     #Index number for Symbol container
    symbolNumber = 0 

    # Creating cards to add to the stack (MyCards). 
    for i in range(maxCards):

        #Creating a card with different values for their attributes
        newCard = {"Color": color[colorNumber], "Pattern": pattern[PatternNumber], "Symbol": symbol[symbolNumber], "Value": valueNumber}

        #Checking if the symbol of the card has reached J, Q, K So i know that the value of the card should be 10
        if (symbol[symbolNumber] == "J" or symbol[symbolNumber] == "Q" or symbol[symbolNumber] == "K"):
            newCard = {"Color": color[colorNumber], "Pattern": pattern[PatternNumber], "Symbol": symbol[symbolNumber], "Value": 10}
        
        #Checking if the symbol of the card has reached A So i know that the value of the card should be 11
        elif (symbol[symbolNumber] == "A"):
            newCard = {"Color": color[colorNumber], "Pattern": pattern[PatternNumber], "Symbol": symbol[symbolNumber], "Value": 11}

        MyCards.append(newCard)

        colorNumber   += 1
        PatternNumber += 1

        #Checking if each card combo has had enough of color number, each card symbol can only have 2 cards with 1 color. 
        if(colorNumber == 2):
            colorNumber = 0
        
        #Checking that the 4 of a kind cards have had one unique pattern before we move on to the next cards with different symbol. 
        if(PatternNumber == 4):
            PatternNumber = 0
            symbolNumber  += 1 
            valueNumber   += 1    

    return MyCards

print(createACardStack())