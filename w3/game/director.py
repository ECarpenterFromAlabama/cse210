from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.jumper = Jumper()
        self._is_playing = True
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()
        self.correct = True

        self._puzzle._read_list()
        self._puzzle._pick_word()
        
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        invalid = True
        while(invalid):
            letter_guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")[0:1]
            if(letter_guess.isalpha()):
                self.correct = self._puzzle.process_guess(letter_guess)
                invalid = False
            else:
                print(f"{letter_guess} is not a letter. Try again.")
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        if(not self.correct):
            self.jumper.remove_part()
            print("OOF! That letter isn't part of the word.\n")

        if("_ " not in self._puzzle.word_guess):
            print("Congratulations! You won!")
            self._is_playing = False
        elif(len(self.jumper.parachute) == 0):
            print(f"Game Over!\nThe word was {self._puzzle.word_selected}")
            self._is_playing = False
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.draw_word_guess()
        self.jumper.draw_jumper()