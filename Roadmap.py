#select random word from words.txt
#import random module
#open text file with syntax
#select one word from list to use for testing


#show mystery word as underscores to use
#ask for user guess (upper or lowercase does not matter)
#validate user input if user enters more than one letter
    #show user error: "Only guess one letter at a time"

#show user if guess is part of word
    #replace underscore with letter
    # show letters that have not been guessed
    #put user guessed letters in a list 

#limit number of user guesses to 8
    #keep track of usere guess count
    #remind user how many guesses are left
    #user only loses guess if guess is incorrect
    #display mystery word if user runs out of guesses
    #show error  message if they guess the same letter twice
        #do not count as a guess

#prompt user to play again when the game ends

#empty list for words
words =[]

with open('words.txt') as file:
    strings = file.readlines()

    for string in strings:
        words.append(string)
        print(words)