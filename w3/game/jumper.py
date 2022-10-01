class Jumper:
    """A jumper that represents the number of chances a player
    has to guess the word incorrectly. 
    
    The responsibility of the jumper is to act as a visual representation as to
    how many guesses the player has left.

    Attributes:
        parachute (list): List of characters that form a parachute-like image.
        person (list): List of characters that form a person-like image. 
    """
    def __init__(self):
        """Constructs a new Jumper.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self.parachute = [" ___ ", \
                          "/___\\", \
                          "\   /", \
                          " \ / "
                          ]
        self.person = ["  O  ", \
                       " /|\ ", \
                       " / \ ", \
                       "     ", \
                       "^^^^^"
                       ]

    def draw_jumper(self):
        """Prints out the complete jumper(parachute and person).
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        for i in self.parachute:
            print(i)
        for i in self.person:
            print(i)

    def remove_part(self):
        """Removes element in parachute list at index 0 every time
        a player guesses incorrectly. Also changes person's head(index 0)
        to an "x"
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        if(len(self.parachute) != 0):
            self.parachute.pop(0)
        if(len(self.parachute) == 0 ):
            self.person[0] = "  X  "