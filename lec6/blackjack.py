# Mini-project #6 - Blackjack
# -*- coding:utf-8 -*-


import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self, whoami):
        self.card_list = []
        self.whoami = whoami

    def __str__(self):
        return "Hand contains " + " ".join(  map( str,self.card_list) )

    def add_card(self, card):
        self.card_list.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        ace = 0
        ace = len( filter( lambda x:x.rank == "A", self.card_list ) )
        total =  sum( map( lambda x: VALUES[x.rank],  self.card_list) )
        return total if ace == 0 or total + 10 > 21 else total + 10
   
    def draw(self, canvas):
        if self.whoami == "p":
            pos_y = 200
        elif self.whoami == "d":
            pos_y = 300
        for ( i, card) in enumerate( self.card_list):
            card.draw(canvas, [ 20 + 100 * ( i + 1), pos_y ] )

    def __gt__(self, other):
        return self.get_value() > other.get_value()
 
    def __lt__(self, other):
        return self.get_value() < other.get_value()

    def __le__(self, other):
        return self.get_value() <= other.get_value()

    def __ge__(self, other):
        return self.get_value() >= other.get_value()


        
# define deck class 
class Deck:
    def __init__(self):
        self.card_list = []
        for s in SUITS:
            for r in RANKS:
                self.card_list.append( Card(s, r))

    def shuffle(self):
        random.shuffle(self.card_list)

    def deal_card(self):
        return self.card_list.pop( len( self.card_list ) - 1 )
    
    def __str__(self):
        return "Deck contains " + " ".join( map( str, self.card_list))


deck = Deck()
player_hand = Hand("p")
dealer_hand = Hand("d")

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck

    # your code goes here
    deck = Deck()
    deck.shuffle()
    player_hand = Hand("p")
    dealer_hand = Hand("d")
    player_hand.add_card( deck.deal_card() )
    player_hand.add_card( deck.deal_card() )
    dealer_hand.add_card( deck.deal_card() )
    dealer_hand.add_card( deck.deal_card() )
    
    in_play = True

    print "Player's Hand " + str(player_hand)
    print "Dealer's Hand " + str(dealer_hand)

def hit():
    global in_play, player_hand, score, deck
    if in_play:
        # if the hand is in play, hit the player
        if player_hand.get_value() <= 21 :
            player_hand.add_card( deck.deal_card() )
            print player_hand
            print player_hand.get_value()
        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21 :
            print "You have busted."
            in_play = False
            score = 0

       
def stand():
    global in_play, dealer_hand, player_hand, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card( deck.deal_card() )
            print dealer_hand
            print dealer_hand.get_value()
        if dealer_hand.get_value() > 21:
            print "Player wins!"
            in_play = False
            score = 0
            return
        if dealer_hand >= player_hand:
            print "Dealer wins!"
            in_play = False
            score = 0
        else :
            print "Player wins!"
            in_play = False
            score = 0



    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    dealer_hand.draw(canvas)
    player_hand.draw(canvas)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
