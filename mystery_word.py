# select random word from words.txt **
# import random module **
# open text file with syntax **
# select one word from list to use for testing **


# show mystery word as underscores to use*
# ask for user guess (upper or lowercase does not matter)*
# validate user input if user enters more than one letter*
    # show user error: "Only guess one letter at a time"

# show user if guess is part of word*
    # replace underscore with letter*
    # show letters that have not been guessed
    # put user guessed letters in a list

# limit number of user guesses to 8
    # keep track of usere guess count
    # remind user how many guesses are left
    # user only loses guess if guess is incorrect
    # display mystery word if user runs out of guesses
    # show error  message if they guess the same letter twice
        # do not count as a guess

# prompt user to play again when the game ends

# empty list for words
import random
words = []
underscores = []
guesses = []
end_game = False

with open('words.txt') as file:
    strings = file.readlines()

    for string in strings:
        words.append(string)
    random_word = words[7].lower()
    random_word = random_word.replace("\n", "")

    word_length = range(len(random_word))
    for num in word_length:
        underscores.append('_')
# joins strings into one sting "" means no spaces
    underscores = "".join(underscores)
    print(underscores)
    user_input = input('Make a guess..').lower()

# [idx for idx, item in enumerate(random-word_list) if item in a[:idx]]
    while user_input != 'Quit!' and end_game == False:
        print(underscores)
        user_input
    for index in range(len(random_word)):
        if random_word[index] == user_input:
            underscores = underscores[0:index] + \
                user_input + underscores[index+1:]
    print(underscores)
    user_input = input('Guess again..')

        if user_input == 'Quit':
            end_game = True
