class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)

	def deal(self, num_hands, num_cards):
		self.num_hands = num_hands
		self.num_cards = num_cards
		if num_cards != -1:
			hand_of_cards = []
			for x in range(num_hands):
				card_list = []
				for y in range(num_cards):
					card_list.append(self.pop_card(-1))
				# for a in card_list:
				# 	print(a)
				hand = Hand(card_list)
				hand_of_cards.append(hand)
			return hand_of_cards
		else:
			hand_of_cards = []
			for x in range(num_hands):
				card_list = []
				for y in range(len(self.cards)):
					card_list.append(self.pop_card(-1))
				# for a in card_list:
				# 	print(a)
				hand = Hand(card_list)
				hand_of_cards.append(hand)
			return hand_of_cards

class Hand(object):
	init_cards = []
	def __init__(self,init_cards):
		self.init_cards = init_cards #creating a new instance variable that is part of all the instances of hand that is called init_card
		self.card_dict = {}

	def add_card(self,card):
		#self.card = card
		for x in self.init_cards:
			if x.suit == card.suit and x.rank == card.rank:
				break
		self.init_cards.append(card)

	def remove_card(self, card):
		#self.card = card #don't need this - only need it in init, but in other methods don't do this since i will end up overriding it
		for y in self.init_cards:
			if y.suit == card.suit and y.rank == card.rank:
				self.init_cards.remove(y)

	def draw(self, deck):
		self.deck = deck
		card_drawn = deck.pop_card()
		self.init_cards.append(card_drawn)

	def remove_pairs(self):
		self.card_dict = {}
		for card in self.init_cards:
			if card.rank not in self.card_dict:
				self.card_dict[card.rank] = 1
			else:
				self.card_dict[card.rank] += 1
		for card_rank in self.card_dict:
			num_cards_to_pop = 0
			if self.card_dict[card_rank] >= 2 and self.card_dict[card_rank]%2 == 0:
				num_cards_to_pop = self.card_dict[card_rank]
				for x in range(num_cards_to_pop):
					for card in self.init_cards:
						if card.rank == card_rank:
							self.remove_card(card)

if __name__ == "__main__":
	pass
