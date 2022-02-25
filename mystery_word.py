
import random
print("\n\n\n***Mystery Word Game***\n\n\n")
print("You have 8 attempts to guess the word correctly. Type 'Quit' to end the game at any time. Good luck!\n\n")
words = []
underscores = []
guesses = []
end_game = False
guess_count = 0
guessed_letters = []


with open('words.txt') as file:
    strings = file.readlines()

    for string in strings:
        words.append(string)

    random_word = random.choice(words)
    random_word = random_word.replace("\n", "")

    word_length = range(len(random_word))
    for num in word_length:
        underscores.append('_ ')
    underscores = "".join(underscores)

    print(" ".join(underscores))
    user_input = input('Make a guess... ').lower()
    guessed_letters.append(user_input)
    if user_input != random_word:
        print("Guess again...")
        guess_count += 1
        print("Number of incorrect guesses made: " + (str(guess_count)))
    if user_input == 'Quit':
        end_game = True
    if guess_count >= 8:
        end_game = True

while user_input != 'Quit' and end_game == False:

    for index in range(len(random_word)):
        if random_word[index] == user_input:
            underscores = underscores[0:index] + \
                user_input + underscores[index+1:]
    print(underscores)

    if user_input in random_word:
        print("Correct! Great guess.")
        guessed_letters.append(user_input)
        user_input = input('Guess again... ')

    else:
        user_input != random_word
        user_input = input('Guess again... ')
        guess_count += 1
        print("Number of incorrect guesses made: " + (str(guess_count)))
        guessed_letters.append(user_input)
        print(guessed_letters)
        if guess_count >= 8:
            end_game = True


if user_input == 'Quit':
    end_game = True
    print(random_word)
    input('Thank you for playing!')

if guess_count >= 8:
    end_game = True
    print('The word was: ' + (str(random_word)))
    print('Thank you for playing!')
