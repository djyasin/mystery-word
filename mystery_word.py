# import string

mystery_word = ["Dog"]
letters_guessed = []
WORDLIST_FILE = "words.txt"

#opens and formats WORDLIST_FILE
# def word_file_opener():
# inFile = open(WORDLIST_FILE, 'r')



print("Welcome to Mystery Word")

for i in range(len(mystery_word)):
    print("I am thinking of a word that is " + (i) + " long.")
#triple check on concatination rules. I think Janelle used something like this earlier this week.
#show available letters.

#letters guessed
# import string
# alphabet = string.ascii_lowercase
# for any letters in word_guessed
# remove letter from remaining letters

# def word_guessed(mystery_word, letters_guessed):
#functions to put letters correctly guessed into a string

# def random_word(word_list):
#  return random.choice(word_list)
    

#function to put incorrect guesses into another string

#will likely need to convert words.txt into a list at the letter level, so going to need the .readline function
# random_word = random_words_generator()
# wordlist = formatted_words()
# def word_file_opener(file):
#     with open('words.txt') as text:
#         line = text.readline()
#         print(f"{len(line)} lines in the file.")
#         line = line.split(" ")
#         print(line)

# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('words.txt', help='file to read')
#     args = parser.parse_args()

# """"this calls the file to run"""
# file = Path(args.file)
# if file.is_file():
#     random_words('words.txt')
# else:
#     print(f"{file} does not exist!")
#     exit(1)