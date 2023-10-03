# A program to solve wordle puzzles using a brute force approach

alphabet = "abcdefghijklmnopqrstuvwxyz"

class Solver:
    def __init__(self):
        # Import the word list
        self.word_list = self.import_word_list()

        # Create a list of possible letters for each position
        self.possible_letters = []
        for i in range(5):
            self.possible_letters.append([letter for letter in alphabet])

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
                self.possible_letters[i] = [letter]
            # The letter is in the word, but not in the right place
            elif color_result[i] == 'y':
                # Update necessary letters to add the letter
                present = False
                for l in self.necessary_letters:
                    if letter in l.keys():
                        l[letter].remove(i)
                        present = True
                        break
                if not present:
                    self.necessary_letters.append({letter: [j for j in range(5) if j != i]})
                # Update possible letters to remove the incorrect letter
                self.possible_letters[i].remove(letter)
            # The letter is not in the word
            else:
                # Update necessary letters to remove the incorrect letter
                for l in self.necessary_letters:
                    if letter in l.keys() and len(l.values()) > 1:
                        l.pop(letter)
                # Update possible letters to remove the incorrect letter
                for i, letters in enumerate(self.possible_letters):
                    if letter in letters and len(letters) > 1:
                        self.possible_letters[i].remove(letter)

    def update_word_list(self):
        words = []
        for word in self.word_list:
            # Check if the word is possible
            possible = True
            for i, letter in enumerate(word):
                if letter not in self.possible_letters[i]:
                    possible = False
                    break
            # If the word is possible, continue to check
            if possible:
                # Check if the word has the necessary letters
                for l in self.necessary_letters:
                    letter = str(l.keys()).lstrip("dict_keys([").rstrip("])")
                    letter = letter.replace("'", "")
                    positions = l.values()
                    # Check if the letter is in the word in one of the possible positions
                    present = False
                    for position in positions:
                        for p in position:
                            if word[p] == letter:
                                present = True
                                break
                    if not present:
                        possible = False
                        break
            # Add the word if it is possible
            if possible:
                words.append(word)
        self.word_list = words
    
    def import_word_list(self):
        # Import the word list
        with open('fiveLetterWords.txt', 'r') as f:
            word_list = f.read().splitlines()
        return word_list

    def restart(self):
        # Reset the solver
        self.word_list = self.import_word_list()
        self.possible_letters = []
        for i in range(5):
            self.possible_letters.append([letter for letter in alphabet])
        self.necessary_letters = []


class UserInterface:
    def __init__(self):
        self.solver = Solver()
    
    def clear_terminal(self):
        # Clear the terminal
        print("\033c", end="")

    def get_input(self):
        # Get input from the user
        guess = input("Enter your guess: ")
        color_result = input("Enter the color result (g: green, y: yellow, n: gray): ")

        # Return the input
        return guess, color_result

    def update_solver(self, guess, color_result):
        # Update the solver
        self.solver.update_positions(guess, color_result)
        self.solver.update_word_list()
    
    def print_word_list(self):
        # Print the word list
        for word in self.solver.word_list:
            print(word)
    
    def get_input_for_restart(self):
        # Ask the user if they want to restart
        restart = input("Would you like to restart? (y/n): ").lower()
        if restart == 'y':
            return True
        else:
            return False
    
    def run(self):
        # Run the program
        while True:

            # Get input from the user
            guess, color_result = self.get_input()

            # Update the solver
            self.update_solver(guess, color_result)

            # Clear the terminal
            self.clear_terminal()

            # Print the word list
            self.print_word_list()

            # Print the length of the word list
            print("Number of words remaining:", len(self.solver.word_list))

            if len(self.solver.word_list) <= 1:
                break
    
    def restart(self):
        self.solver.restart()
        self.clear_terminal()
        

if __name__ == "__main__":
    ui = UserInterface()
    while True:
        ui.run()
        restart = ui.get_input_for_restart()
        if restart:
            ui.solver.restart()
            ui.clear_terminal()
        else:
            break
