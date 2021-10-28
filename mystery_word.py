#import raandom words
mystery_word = ["Dog"]

print("Welcome to Mystery Word")
print("I am thinking of a word that is " + str(len(mystery_word)) + " long.")
#triple check on concatination rules. I think Janelle used something like this earlier this week.
#show available letters.
mystery_word = ["D", "o", "g"]

#functions to put letters correctly guessed into a string
#function to put incorrect guesses into another string
#will likely need to convert words.txt into a list at the letter level, so going to need the .readline function
def random_words(file):
    with open(file) as text:
        line = text.readline()
        print(f"{len(line)} lines in the file.")
        line = line.split(" ")
        print(line)

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

""""this calls the file to run"""
file = Path(args.file)
if file.is_file():
    random_words(file)
else:
    print(f"{file} does not exist!")
    exit(1)