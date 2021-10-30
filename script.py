# Query: script.py
# ContextLines: 1
import random

# import random module

#random_number = random.randrange(1,20)

random_number = 5
random_number = str(random_number)
print(random_number)
guess_count = 0
# generate random number between 1-28


# prompt user for input "Guess a number between 1 and 20




# print(type(user_input))

# input will be a value

while user_input != 'Quit':
    if guess_count == 5:
        print('You have run out of guesses!')
    # compare user input to random number
    # if user guesses correct number output "You got it right"
#  user_input = int(user_input)
    if user_input == random_number:
        print("You got it right!")


# if the user guesses incorrectly, check if the number is
# higher or lower than the random number
    if user_input != random_number:
        if user_input > random_number:
            user_input = input('Your guess was too high. Please guess again.')
            guess_count += 1
    user_input = int(user_input)

        else:
            user_input = input("Quit a number between 1-20")
# if too high need to output "Number too high"
    elif user_input < random_number:
        user_input = input('Your guess was too low! guess again:')
        guess_count += 1
        (print)
# if too low need to output "Number too low"
# limit number of guesses to 5
# show the user how many number of guesses it took to get the right number


