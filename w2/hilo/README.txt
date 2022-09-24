W2 Developer: HILO
Easterling Carpenter
easterling.carpenter@gmail.com

Required Software: Python 3.X

The project adheres to the following rules and requirements
in order to play the game HILO:

***RULES***
The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.

***REQUIREMENTS***
The program must include a README file.
The program must include class and method comments.
The program must have at least two classes.
The program must remain true to game play described in the overview.

-------------------------------------------------------------

Structure:
__main__.py
.\game
-> cards.py
    -> Card class
    -> DeckOfCards class
-> dealer.py
    -> Dealer class
        -> contains several methods that allow the dealer
           to:
           generate a deck of cards
           show the current Card
           prompt user to continue playing or select higher/lower
           keep the player's score


