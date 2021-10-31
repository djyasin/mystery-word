# select random word from words.txt
# import random module **
# open txt file using with syntax **
# put words from txt file into list of strings **
# select one word from list to use for testing **

# show mystery word as underscores to user **
# ask for user guess (upper or lowercase does not matter)**
# validate user input if user enters more than one letter
# show user error: "You can only guess letter a a time. Guess again: "

# Show user if guess is part of word **
# replace underscore with letter **
# Show letters that have not been guessed


# limit number of user guesses to 8
# keep track of user guess count
# show user how many guesses are left
# user only loses guess if guess is incorrect*
# display mystery word if user runs out of guesses
# show user error if they guess same letter twice. Do not count as a guess in this case.

# Prompt user to play again when the game ends
# Add levels of difficulty based on random word length


print("\n\n\n***Mystery Word Game***\n\n\n")
print("You have 8 attempts to guess the word correctly. Type 'Quit' to end the game at any time. Good luck!\n\n")
import random
words = []
underscores = []
guesses = []
end_game = False
guess_count = 0
guessed_letters = []
#letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
#        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#print(letter)

#this isn't working.
# while user_input != 'Quit':
#     if guess_count == 8:
#         print('You have run out of guesses!')

with open('words.txt') as file:
    strings = file.readlines()

    for string in strings:
        words.append(string)
    # actually get a random word from words.txt
    random_word = words[7].lower()
    random_word = random_word.replace("\n", "")
    # print(random_word)

    word_length = range(len(random_word))
    for num in word_length:
        underscores.append('_')
    underscores = "".join(underscores)

    print(" ".join(underscores))
    user_input = input('Make a guess... ').lower()
    guessed_letters.append(user_input)
    if user_input != random_word:
        guess_count += 1
    if user_input == 'Quit':
        end_game = True
    if guess_count >= 8:
        end_game =True
    
while user_input != 'Quit' and end_game == False:

    for index in range(len(random_word)):
        if random_word[index] == user_input:
            underscores = underscores[0:index] + \
                user_input + underscores[index+1:]
    print(underscores)
    #this isn't working
    if user_input == random_word:
        print("Correct! Great guess.")
        

    else: 
        user_input != random_word
        user_input = input('Guess again... ')
        guess_count += 1
        print("Number of guesses made: " + (str(guess_count)))
        guessed_letters.append(user_input)
        print(guessed_letters)
        if guess_count >= 8:
            end_game =True
        


if user_input == 'Quit':
    end_game = True

if guess_count >= 8:
    end_game =True