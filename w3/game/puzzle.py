
import csv
import random

class Puzzle:

    def __init__(self):
        self._word_list = []
        self.__word_selected = ''
        self.word_guess = []


    def _read_list(self):
        word_list_location = "./game/dict/most-common-nouns-english.csv"
        with open(word_list_location, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
              new_word = row[0]
              self._word_list.append(new_word)
        self._word_list.pop(0)

    def _pick_word(self):
        rand_word = random.choice(self._word_list)
        self._word_selected = rand_word
        for i in range(len(rand_word)):
            self.word_guess.append("_ ")

    def draw_word_guess(self):
        print()
        print(*self.word_guess)

    def process_guess(self, guess_letter):
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