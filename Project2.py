import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return ("{} of {}".format(self.rank, self.suit))

class Deck(Card):
    
    def __init__(self):
        self.deck = []  # start with an empty list
        self.deck = [ Card( suit, rank ) for rank in ranks for suit in suits ]
   
    
    def __str__(self):
            return '\n'.join([str(card) for card in self.deck])

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
            single_card = self.deck.pop()
            return single_card

class Hand(Card):
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value = self.value + values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        if self.value > 21 and self.aces > 0:
                self.value = self.value - 10
                self.aces = self.aces + 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total = self.total + self.bet
    
    def lose_bet(self):
         self.total = self.total - self.bet

def take_bet(chips):
    while True:
	    try:
	        chips.bet = int(input("Enter your bet as an integer: "))
	    except ValueError:
	        print ("Please enter an integer value")
	    else:
	        if chips.total >= chips.bet:
	            break
	        else:
	            print ("Your bet should not exceed {}". format(chips.total))

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        h_or_s = input("Enter Hit (h) or Stand(s): ")
        #To account for cases where the player enters ss or hh
        #Take only the 1st letter
        if h_or_s[0].lower() == 'h':
            hit(deck,hand)
        elif h_or_s[0].lower() == 's':
            playing = False
        else:
            print("You have not entered the correct value. Please enter 'h' or 's'")
            continue
        break

def show_some(player,dealer):
    print ("Player's cards")
    for card in player.cards:
        print (card)
    print("\n")
    print ("Dealer's card")
    print("Hidden card")
    print (dealer.cards[1])
    
    
    
def show_all(player,dealer):
    print ("Player's cards")
    for card in player.cards:
        print (card)
    print ("Player's hand value is:{}".format(player.value))
    print("\n")
    print ("Dealer's cards")
    for card in dealer.cards:
        print (card)
    print ("Dealer's hand value is:{}".format(dealer.value))

def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push():
    print("It's a push! Tie between player and dealer")

while True:
    # Print an opening statement
    print("Let's play BlackJack")
    
# Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    # Set up the Player's chips
    player_chips = Chips()
    
# Prompt the Player for their bet
    take_bet(player_chips)   
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        #if player takes a stand this loop is exited and the dealer keeps taking a hit
        hit_or_stand(deck, player_hand)
    
    # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    # Player has taken a stand
    if player_hand.value <= 21:
        while (dealer_hand.value < 17):
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)
        # Run different winning scenarios
      
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            #Tie situation
            push()
    
    # Inform Player of their chips total 
    print("Player chips total: {}".format(player_chips.total))
    
    # Ask to play again
    y_or_n = input("Do you want to play again? y or n ")
    if y_or_n[0].lower() == 'y':
        playing = True
    else:
        playing = False
        print("Game has ended")
        break
        
    