import random
from game.cards import DeckOfCards, Card

def move_card(target, destination):
    destination.append(target[0])
    target.pop(0)

class Dealer:
    
    def __init__(self):
        self.is_playing = True
        self.player_guess = None
        self.score = 300

        self.current_deck = DeckOfCards().deck
        random.shuffle(self.current_deck)
        print(len(self.current_deck))
        self.used_pile = []
        self.in_play = []
        move_card(self.current_deck, self.in_play)
        move_card(self.current_deck, self.in_play)


    def disp_card(self) -> Card:
        current_card = self.in_play[0]
        print(f"The card is: {current_card.card_value()}")
        #Move current card to the used pile
        move_card(self.in_play, self.used_pile)
        
        if(len(self.current_deck) == 0):
            print("\nShuffling deck...")
            self.current_deck = self.used_pile
            random.shuffle(self.current_deck)
            self.used_pile = []
            print("Deck shuffled.\n")

        #Move new card into in play cards
        move_card(self.current_deck, self.in_play)

        return current_card

    def prompt_player(self):
        self.player_guess = (input("Higher or Lower? [h/l] ")).lower()

    def reveal(self, last_card):
        next_card = self.in_play[0].card_value()
        next_card_value = int((next_card)[2:])
        print(f"Next card was: {next_card}")

        last_card_value = int(last_card.card_value()[2:])
        if(next_card_value > last_card_value and self.player_guess == 'h'):
            self.score += 100
        elif(next_card_value <= last_card_value and self.player_guess == 'l'):
            self.score += 100
        else:
            self.score -= 75
        print(f"your score is: {self.score}")
        
    def cont_game(self):
        if(self.score <= 0):
            self.is_playing = False
            print("You have reached 0 points...\nGame Over!")
            return
        
        incorrect_input = True
        while(incorrect_input):
            cont_play = input("Play again? [y/n] ").lower()
            print()
            if(cont_play == 'y' or cont_play == 'n'):
                incorrect_input = False
            else:
                incorrect_input = True
                print("Please enter a valid input[y/n]")


        if(cont_play == 'y'):
            return
        else:
            self.is_playing = False

    def run_game(self):
        while(self.is_playing):
           current_card = self.disp_card()     #shows current card
           self.prompt_player()                #asks if higher or lower
           self.reveal(current_card)           #Shows the next card and shows new score
           self.cont_game()                    #Asks player if they want to keep playing