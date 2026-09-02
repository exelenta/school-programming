class Card(object):
    """A Blackjack card"""
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def value(self):
        if type(self.face) == int:
            return self.face
        elif self.face == "Ace":
            return 11
        else:
            return 10

import random
FACES = list(range(2, 11))+["Jack", "Queen", "King", "Ace"]
SUITS = ["Spades", "Diamonds", "Hearts", "Clubs"]
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for face in FACES:
                self.cards.append(Card(face, suit))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class Hand(object):
    """A hand of cards displayed on the table"""
    def __init__(self, x, y, canvas):
        self.canvas = canvas
        self.x, self.y = x, y
        self.face_up_cards = []
        self.face_down_cards = []

    def clear(self):
        self.face_up_cards.clear()
        self.face_down_cards.clear()

    def add(self, card, hidden = False):
        if hidden:
            self.face_down_cards.append(card)
        else:
            self.face_up_cards.append(card)

    def show(self):
        self.face_up_cards, self.face_down_cards = self.face_up_cards+self.face_down_cards, []

    def value(self):
        return sum(i.value() for i in self.face_up_cards)+sum(i.value() for i in self.face_down_cards)

class Table(object):
    """A graphical Blackjack table"""
    def __init__(self):
        pass

    def clear(self):
        pass

    def set_score(self):
        pass
    
def blackjack(table):
    deck = Deck()
    player = Hand(10, 100, table)
    dealer = Hand(90, 100, table)
