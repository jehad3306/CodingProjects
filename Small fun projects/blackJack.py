import random

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

def printAllCards(card_stack):
    for card in card_stack:
        print(f"{card['Color']} | {card['Pattern']} | {card['Symbol']} | {card['Value']}  ")

def betOutcome(Outcome, Chips, handValue):
    maxHandValuePossible = 21

    if (Outcome == "Player Wins"):

        if(handValue > maxHandValuePossible):
            print("Dealer got bustet")
        return Chips 
    
    elif(Outcome == "Dealer Wins"):

        if(handValue > maxHandValuePossible):
            print("You got bustet")
        return -Chips
    
    elif(Outcome == "No wins"):
        return 0
    
    elif(Outcome == "Blackjack"):
        return Chips * 2

def dealOutCards(card_stack):
    amountOfCards = len(card_stack)
    card = card_stack[amountOfCards - 1]
    cardStack.pop(amountOfCards-1)

    return card

def cardValues(Hand):
    totalCardValue = 0

    for cardValue in Hand:
        totalCardValue += cardValue["Value"]
   
    return totalCardValue

def betIteration(betLessThanOwnedChips, bettingChips):

    while not betLessThanOwnedChips:
        bettingChipsInput = int(input("-----How much would you like to bet this round: "))
        if(bettingChipsInput <= PlayerChips):
            betLessThanOwnedChips = True
            bettingChips = bettingChipsInput
            return betLessThanOwnedChips, bettingChips
        else:
            print(f"You have to bet the amount you have or lower. the amount you have is {PlayerChips}")
    
    return True, bettingChips

def playersTurn(stand, PlayerChips, bettingChips, periodFinished, playerHandValue):

    printCardsOnTheTable(playerHand, dealerHand)

    if not stand:
        playerHandValue = cardValues(playerHand)

        if(playerHandValue > 21):

            isThereAceInTheHand = changeAceValue(playerHand)

            if(isThereAceInTheHand == False ):
                PlayerChips += betOutcome("Dealer Wins", bettingChips, playerHandValue)
                periodFinished = True
                return periodFinished, stand, PlayerChips

        elif(playerHandValue == 21):
            PlayerChips += betOutcome("Blackjack", bettingChips, playerHandValue)
            periodFinished = True
            return periodFinished, stand, PlayerChips

        elif(playerHandValue < 21):
            while not stand:
                print(playerHandValue)
                nextMove = input("Hit & Stand? ")
                if(nextMove.lower() == "hit"):
                    playerHand.append(dealOutCards(cardStack))
                    playerHandValue = cardValues(playerHand)
                    printCardsOnTheTable(playerHand, dealerHand)
                    if(playerHandValue >= 21):
                        break
                elif(nextMove.lower() == "stand"):
                    stand = True
                    return periodFinished, stand, PlayerChips
        
    return periodFinished, stand, PlayerChips

def dealersTurn(stand, PlayerChips, bettingChips, periodFinished, dealerHandValue, playerHandValue):

    if(stand == True):
        printCardsOnTheTable(playerHand, dealerHand)
        
        #print("It is dealers turn now")
        if(dealerHandValue < 18):
            dealerHand.append(dealOutCards(cardStack))

        elif(dealerHandValue > 21):

            isThereAceInTheHand = changeAceValue(dealerHand)

            if(isThereAceInTheHand == False):
                periodFinished = True
                PlayerChips += betOutcome("Player Wins", bettingChips, dealerHandValue)
                return periodFinished, PlayerChips

        elif(dealerHandValue > 17 and dealerHandValue < 22 ):
            print(f"Comparing Player and dealers hands | Player:{playerHandValue} | Dealer:{dealerHandValue}")
            
            if(playerHandValue > dealerHandValue):
                periodFinished = True
                PlayerChips += betOutcome("Player Wins", bettingChips, dealerHandValue)
                return periodFinished, PlayerChips


            elif(playerHandValue < dealerHandValue):
                periodFinished = True
                PlayerChips += betOutcome("Dealer Wins", bettingChips, dealerHandValue)
                return periodFinished, PlayerChips


            elif(playerHandValue == dealerHandValue):
                PlayerChips += betOutcome("No wins", bettingChips, dealerHandValue)
                periodFinished = True
                return periodFinished, PlayerChips
    
    return periodFinished, PlayerChips

def printCardsOnTheTable(pHand, dHand):

    print("Players hand:", end=" ")

    for cards in pHand:
        print(f"[{cards['Symbol']}]", end=" ")

    print("\nDealersHand: ", end=" ")

    if  stand == False:
        for index, cards in enumerate(dHand):
            if index == 0:
                print(f"[X]", end=" ")
            else:
                print(f"[{cards['Symbol']}]", end=" ")
        print("\n")

    else:
        for cards in dHand:
                print(f"[{cards['Symbol']}]", end=" ")
        print("\n")

def changeAceValue(cardHands):
    isThereAceInTheHand = False
    
    for cards in cardHands:

        if((cards["Symbol"] == "A") and (cards["Value"] != 1)):

            isThereAceInTheHand = True
            cards["Value"] = 1

            return isThereAceInTheHand
        
    return isThereAceInTheHand


cardStack = createACardStack()
random.shuffle(cardStack)
#printAllCards(cardStack)
#print(len(cardStack))

playerHand = []
dealerHand = []
hit = False
stand = False
quit = False
roundFinished = False
BetLessThanOwnedChips = False
isItPlayersTurn = True
bettingChips = 0

nextMove = ""
BigHandValue = False


cardStack = createACardStack()
random.shuffle(cardStack)

playerHand.append(dealOutCards(cardStack))
playerHand.append(dealOutCards(cardStack))
dealerHand.append(dealOutCards(cardStack))
dealerHand.append(dealOutCards(cardStack))



print("------------------------ Welcome to BlackJack Heavan -------------------------------")
PlayerChips = int(input("How many chips would you like to play with? "))

print("\n--------------------------- Now the game will begin  -------------------------------\n")


while (quit != True):

    playerHandValue = cardValues(playerHand)
    dealerHandValue = cardValues(dealerHand)

    #Bet chips each round
    bet = betIteration(BetLessThanOwnedChips, bettingChips)
    BetLessThanOwnedChips = bet[0]
    bettingChips = bet[1]

    

    playersTurnOutcome = playersTurn(stand, PlayerChips, bettingChips, roundFinished, playerHandValue)
    roundFinished = playersTurnOutcome[0]
    stand = playersTurnOutcome[1]
    PlayerChips = playersTurnOutcome[2]

    dealersTurnOutcome = dealersTurn(stand, PlayerChips, bettingChips, roundFinished, dealerHandValue, playerHandValue)
    roundFinished  = dealersTurnOutcome[0]
    PlayerChips = dealersTurnOutcome[1]

    if(roundFinished == True):
        playerHand = []
        dealerHand = []
        playerHandValue = 0
        dealerHandValue = 0

        playerHand.append(dealOutCards(cardStack))
        playerHand.append(dealOutCards(cardStack))
        dealerHand.append(dealOutCards(cardStack))
        dealerHand.append(dealOutCards(cardStack))

        BetLessThanOwnedChips = False
        roundFinished = False
        isItPlayersTurn = True
        stand = False

        cardStack = createACardStack()
        random.shuffle(cardStack)
    
        if(PlayerChips == 0):
            print("-------------------- Thank you for playing at Blackjack Heavan --------------------")
            quit = True
   
    

        print(f"Player Chips:{PlayerChips}")


