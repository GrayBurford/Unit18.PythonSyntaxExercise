# For a list of words, print out each word on a separate line, but in all uppercase. 
# How can you change a word to uppercase? Ask Python for help on what you can do with strings!

list_of_words = ["Gray", "Tina", "Banana"]

for word in list_of_words:
    print(word.upper())

def print_upper_words (words):
    """Print each word in a list of words as upper case on separate lines.
     -words: list of strings
    """

    for word in words:
        print(word.upper())

def print_e_words_to_upper (words):
    """If word starts with "e" or "E", print each word in a list of words as upper case on a separate line
    """
    for word in words:
        # if word.startswith("e") or word.startswith("E"):
        if word[0] == "e" or word[0] == "E":
            print(word.upper())

def print_words_starts_with (words, starts_with):
    """Prints words to upper case that only start with a specific letter:
    -words: list of words
    -starts_with: list of letters
    """
    for word in words:
        for letter in starts_with:
            if word.lower().startswith(letter.lower()):
                print(word.upper())