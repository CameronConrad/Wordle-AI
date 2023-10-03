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

def add_words(*words: str):
    # Add words to the word list
    with open('fiveLetterWords.txt', 'a') as f:
        for word in words:
            f.write(word + '\n')
    # Sort the words
    sort_words()

def format_words(*words: str):
    # Format the words to be added to the word list
    formatted_words = []
    for word in words:
        formatted_words.append(word.lower())
    return formatted_words

def main():
    pass