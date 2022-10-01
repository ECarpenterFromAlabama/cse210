
import csv
import random

class Puzzle:
    """A word puzzle to be solved. 
    
    The responsibility of a puzzle is to choose a word to be solved
    and show correct guesses.

    Attributes:
        word_list (list): List of words to choose from.
        word_selected(string): The word selected the word_list for the puzzle.
        word_guess(list): list of underscores(representing letters in word_selected)
        and letters correctly guessed.
    """
    def __init__(self):
        """Constructs a new Puzzle.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        self._word_list = []
        self._word_selected = ''
        self.word_guess = []

    def _read_list(self):
        """Reads a csv dictionary into the _word_list.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        word_list_location = "./game/dict/most-common-nouns-english.csv"
        with open(word_list_location, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
              new_word = row[0]
              self._word_list.append(new_word)
        self._word_list.pop(0)

    def _pick_word(self):
        """Picks a word from the _word_list to be the puzzle word.
        Also generates a series of underscores dependent on how many 
        letters are in the puzzle word.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        rand_word = random.choice(self._word_list)
        self._word_selected = rand_word
        for i in range(len(rand_word)):
            self.word_guess.append("_ ")

    def draw_word_guess(self):
        """Prints out the puzzle word in underscores and
        correctly guessed letters.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        print()
        print(*self.word_guess)

    def process_guess(self, guess_letter):
        """Takes the player's guess and checks to see if the
        letter is in the selected word. It then changes all
        relevant underscores in the guess word to the guessed 
        letter if correct. 
        
        Returns correct_answer(boolean): Whether the guess was
        present in the selected word or not..
        
        Args:
            self (Puzzle): an instance of Puzzle.
            guess_letter(string): the player's guessed letter
        """
        more_letters = True
        pos = 0
        correct_answer = False
        while(more_letters):
            letter_pos = self._word_selected.find(guess_letter, pos)
            if(letter_pos != -1):
                self.word_guess[letter_pos] = guess_letter
                pos += 1
                correct_answer = True
            else:
                more_letters = False
        return correct_answer