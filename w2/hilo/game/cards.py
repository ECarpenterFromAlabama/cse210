class Card:

    def __init__(self, s, v):
        self.value = v
        self.suit = s
    
    def card_value(self):
        return f"{self.suit} {self.value}"


class DeckOfCards:

    def __init__(self):
        self.deck = []

        SUITS = ["♥️", "♦️", "♣️", "♠️"]
        
        for s in SUITS:
            for c in range(13):
                card = Card(s, (c+1))
                self.deck.append(card)