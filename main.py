# A program to solve wordle puzzles using a brute force approach

alphabet = "abcdefghijklmnopqrstuvwxyz"

class Solver:
    def __init__(self):
        # Import the word list
        self.word_list = self.import_word_list()

        # Create a list of possible letters for each position
        self.possible_letters = [
            [[alphabet for i in range(5)] for j in range(5)],
        ]

        # Create a list of necessary letters for the word
        # Each item in the list is a dictionary with the letter as the key and possible positions as the value
        self.necessary_letters = []

    def update_positions(self, guess, color_result):
        for i, letter in enumerate(guess):
            # The letter is correct
            if color_result[i] == 'g':
                # Add it to the necessary letters list if it isn't already there
                present = False
                for l in self.necessary_letters:
                    if letter in l.keys():
                        l[letter] = [i]
                        present = True
                        break
                if not present:
                    self.necessary_letters.append({letter: [i]})
                # Set possible letters to only the correct letter
                for l in self.possible_letters:
                    l[i] = [letter]
            # The letter is in the word, but not correct
            elif color_result[i] == 'y':
                # Update necessary letters to remove the incorrect letter
                for l in self.necessary_letters:
                    if letter in l.keys() and len(l.values()) > 1:
                        l[letter].remove(i)
                        break
                # Update possible letters to remove the incorrect letter
                self.possible_letters[0][i].remove(letter)
            # The letter is not in the word
            else:
                # Update necessary letters to remove the incorrect letter
                for l in self.necessary_letters:
                    if letter in l.keys() and len(l.values()) > 1:
                        l.pop(letter)
                        break
                # Update possible letters to remove the incorrect letter
                self.possible_letters[0][i].remove(letter)
            
    def update_word_list(self):
        for word in self.word_list:
            # Check if the word is possible
            possible = True
            for i, letter in enumerate(word):
                if letter not in self.possible_letters[0][i]:
                    possible = False
                    break
            # Remove the word if it is not possible
            if not possible:
                self.word_list.remove(word)
    
    def import_word_list(self):
        # Import the word list
        with open('five-letter-words.txt', 'r') as f:
            word_list = f.read().splitlines()
        return word_list