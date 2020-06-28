import random

# Importing words as a list
word_list = list([line.rstrip('\n') for line in open("word_list.txt")])
# Creating variables 
user_guess = list()
guess_nr = 0
run_variable = True

# Loop shall run as long as run_variable is True
while run_variable == True:
    # Randomise index number
    random_index = random.randint(0,len(word_list))
    # Pick word from word_list based on randomised number
    answer = word_list[random_index]
    # Creating a new variable for the user's guess which has the length of the word and * instead of letters
    user_guess_list = list('*'*len(answer))
    active = True
    # Run the following loop when the numbers of guesses are less than 7
    while (guess_nr < 7 and (active == True)):
        # If there is still a * in the word, allow the user to input a guess
        if ('*' in user_guess_list):
            user_guess = ''.join(user_guess_list)
            # User input
            user_input = input("{} Please enter your next guess: ".format(user_guess))
            # If the letter guessed is correct, replace it in the displayed word
            if user_input in answer:
                index_list = [] 
                for i in range(0, len(answer)) : 
                    if answer[i] == user_input : 
                        user_guess_list[i] = user_input 
            # If the guess is not correct, number of guesses remaining are reduced  
            else:
                guess_nr += 1
        # If there are no * in the displayed word, the user wins the game and the game is stopped
        else:
            print("Congratulations you win")
            active = False

    # Finishing the game if user wins     
    if active == False:
        break
    # If the user guessed more than 7 times he loses
    else:
        print("You lose")
        break
    
    
        

        
    
    
    
