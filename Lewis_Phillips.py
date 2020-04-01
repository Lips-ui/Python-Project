import random

wordList = list()
wordList = [line.rstrip('\n') for line in open("word_list.txt")]
userGuess = list()
guessNr = 0
runVariable = True

while runVariable == True:
    randomIndex = random.randint(0,len(wordList))
    answer = wordList[randomIndex]
    userGuessList = list('*'*len(answer))
    active = True
    while (guessNr < 7 and (active == True)):
        if ('*' in userGuessList):
            userGuess = ''.join(userGuessList)
            userInput = input("{} Please enter your next guess: ".format(userGuess))
            if userInput in answer:
                index_list = [] 
                for i in range(0, len(answer)) : 
                    if answer[i] == userInput : 
                        userGuessList[i] = userInput 
            else:
                guessNr += 1
        else:
            print("Congratulations you win")
            active = False
            
    if active == False:
        break
    else:
        print("You lose")
        break
    
    
        

        
    
    
    