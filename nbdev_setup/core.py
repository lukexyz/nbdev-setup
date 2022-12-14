# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'hello_player', 'Card', 'Deck']

# %% ../00_core.ipynb 2
from fastcore.utils import *

# %% ../00_core.ipynb 4
def hello_player(to):
    "Say hello to a player"
    return f'Hello {to}! From 00_core.ipynb'

# %% ../00_core.ipynb 7
# ["♣️","🔶","❤️","♠️", "🃏"]
suits = "♠ ♣ ♦ ♥ 🃏".split()
ranks = [None] + [x for x in range(2,11)] + "J Q K A".split()

# %% ../00_core.ipynb 9
class Card:
    """A playing card."""
    def __init__(self, 
                 rank:int, 
                 suit:int):
        self.rank = rank
        self.suit = suit
    def __str__(self): 
        if self.suit==4: return f"{suits[self.suit]}"
        else: return f"{ranks[self.rank]}{suits[self.suit]}"
    __repr__=__str__
    def __eq__(self, a): return self.rank == a.rank
    def __gt__(self, a): return self.rank > a.rank
    def __st__(self, a): return self.rank < a.rank
    

# %% ../00_core.ipynb 18
import random

class Deck:
    "A deck of 54 cards, including two jokers."
    def __init__(self, jokers=True):
        self.cards = [Card(suit=s, rank=r) for s in range(4) for r in range(1,14)]
        if jokers:
            self.cards.append(Card(suit=4, rank=None))
            self.cards.append(Card(suit=4, rank=None))
            
    def __str__(self):
        ret = f"Deck ({len(self.cards)})\n"
        cardlist = "".join([f"{card}; " for card in self.cards])
        return ret + cardlist
    __repr__ = __str__
    
    def __len__(self):
        return len(self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def take_card(self):
        return self.cards.pop()
    
    def draw_n(self, n:int):
        hand = []
        for card in range(n):
            hand.append(self.take_card())
        return hand

