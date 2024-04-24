'''
The python file is just a function cut out of my blackjack code project.
After trying out different stuff and thinking of how to show off my understanding of redis and how to integrate it with python,
i came to the conclusion to not add values into the database and use it. Instead i will add variables and data structures into the redis
inside the python file and retrieve it aswell. 

In conclusion. i dont think my "method" of solving this was the smart neither the right way. But instead i wanted to show of
my understanding of how i understand how to interact with redis. The file does not give out the right output after compiling,
because i understood that there are certain limitation of how data structures work together in redis. 


'''

import redis

redis_host = "localhost"
redis_port = 6379

r = redis.StrictRedis(host = redis_host, port = redis_port, decode_responses=True)

# Everytime i ran the python file, it would add to the database when i pushed to list. so i created this function --
# Everytime i run the file it would first delete all of it and add new values. 
def createARedisList(list, listName):
    try:
        r.delete(listName)

        for i in list:
            r.rpush(listName, i)
    
    except:
        print("Could not create list")


def createACardStack():

    # Different attributes for cards

    color = ["red", "black"]
    pattern = ["spade","heart", "diamond", "club"]
    symbol = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    combined_list = {"color" : color, "pattern" : pattern, "symbol" : symbol}

    for i in combined_list:
        createARedisList(combined_list[i], i)

    r.set("maxCards", 52)
    maxCards = int(r.get("maxCards"))


    #Start value of the first card
    valueNumber = 2

    #Index number for each container
    colorNumber = 0
    PatternNumber = 0
    symbolNumber = 0 

    # Creating cards to add to the stack (MyCards). 
    for i in range(maxCards):

        #Creating a card with different values for their attributes
        r.hset("newCard", {"color": color[colorNumber], "pattern" : pattern[PatternNumber], "symbol": symbol[symbolNumber], "value" : valueNumber})

        #Checking if the symbol of the card has reached J, Q, K So i know that the value of the card should be 10
        if (symbol[symbolNumber] == "J" or symbol[symbolNumber] == "Q" or symbol[symbolNumber] == "K"):
            r.hset("newCard", {"color": color[colorNumber], "pattern" : pattern[PatternNumber], "symbol": symbol[symbolNumber], "value" : 10})


        
        #Checking if the symbol of the card has reached A So i know that the value of the card should be 11
        elif (symbol[symbolNumber] == "A"):
            r.hset("newCard", {"color": color[colorNumber], "pattern" : pattern[PatternNumber], "symbol": symbol[symbolNumber], "value" : 11})




        new_card_data = r.hgetall("newCard")
        r.rpush("myCards", new_card_data)



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

        return r.lrange("myCards", 0, -1)

print(createACardStack())