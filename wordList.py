# Functions to modify fiveLetterWords.txt

def import_word_list():
    # Import the word list
    with open('fiveLetterWords.txt', 'r') as f:
        word_list = f.read().splitlines()
    return word_list

def sort_words():
    # Sort the words by length
    word_list = import_word_list()
    word_list.sort(key=len)
    # Write the sorted word list to a file
    with open('fiveLetterWords.txt', 'w') as f:
        for word in word_list:
            f.write(word + '\n')

def add_words(words: list):
    # Add words to the word list
    with open('fiveLetterWords.txt', 'a') as f:
        for word in words:
            f.write(word + '\n')
    # Sort the words
    sort_words()

def main():
    pass