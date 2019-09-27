
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two__', 'Three', 'Four_', 'Five_', 'Six__', 'Seven',
         'Eight', 'Nine_', 'Ten__', 'Jack_', 'Queen', 'King_', 'Ace__')
values = {'Two___Hearts': 2, 'Three_Hearts': 3, 'Four__Hearts': 4, 'Five__Hearts': 5, 'Six___Hearts': 6,
          'Seven_Hearts': 7, 'Eight_Hearts': 8, 'Nine__Hearts': 9, 'Ten___Hearts': 10, 'Jack__Hearts': 10,
          'Queen_Hearts': 10, 'King__Hearts': 10, 'Ace___Hearts': 11, 'Two___Diamonds': 2, 'Three_Diamonds': 3,
          'Four__Diamonds': 4, 'Five__Diamonds': 5, 'Six___Diamonds': 6, 'Seven_Diamonds': 7, 'Eight_Diamonds': 8,
          'Nine__Diamonds': 9, 'Ten___Diamonds': 10, 'Jack__Diamonds': 10, 'Queen_Diamonds': 10, 'King__Diamonds': 10,
          'Ace___Diamonds': 11, 'Two___Spades': 2, 'Three_Spades': 3, 'Four__Spades': 4, 'Five__Spades': 5, 'Six___Spades': 6,
          'Seven_Spades': 7, 'Eight_Spades': 8, 'Nine__Spades': 9, 'Ten___Spades': 10, 'Jack__Spades': 10, 'Queen_Spades': 10,
          'King__Spades': 10, 'Ace___Spades': 11, 'Two___Clubs': 2, 'Three_Clubs': 3, 'Four__Clubs': 4, 'Five__Clubs': 5, 'Six___Clubs': 6,
          'Seven_Clubs': 7, 'Eight_Clubs': 8, 'Nine__Clubs': 9, 'Ten___Clubs': 10, 'Jack__Clubs': 10, 'Queen_Clubs': 10, 'King__Clubs': 10, 'Ace___Clubs': 11}
cards = []
results = []
dealer_result = []
dealer_hand = ['hit', 'stay']


def result_sum(results):
    i = 0
    sums = 0
    while i < len(results):
        sums = sums+results[i]
        i = i+1
    print("result sum is :", sums)
    if sums > 21:
        print("sum of cards exceed 21")
        print(" lost the game")
        print("other player won the game since you had bursted")
        #feelings = str(input("do you want to play again say yes or no:"))
        # if feelings == 'yes':
        #    Game(Player_hand)
        # else:
        exit()
    if sums == 21:
        print(" Hurrah you won the game")


class Deck:
    def __init__(self):
        self.cards = cards

    def get_deck(self):
        for i in suits:
            for j in ranks:
                cards.append((j + '_' + i))
        return cards


class Dealer(Deck):
    def d_hit(self):
        Dealer.get_deck(self)
        random.shuffle(cards)
        hand = random.sample(cards, k=2)
        dealer_result.append(values[hand[0]])
        dealer_result.append(values[hand[1]])
        initial = True
        while initial:
            single_card = random.sample(cards, k=1)
            hand.append(single_card)
            dealer_result.append(values[single_card[0]])
            print(hand)
            result_sum(dealer_result)
            play = random.sample(dealer_hand, k=1)
            print(play)
            if play[0] == 'stay':
                print("dealer wants to stay")
                initial = False
        print("dealer's cards are :", hand)


class Player_Hand(Deck):
    def __init__(self, balance):
        self.balance = balance

    def hit(self):
        money = int(input("enter the bet amount:"))
        if self.balance < money:
            print("You Don't have enough balance")
        else:
            print(" Bet taken balance amount is :", self.balance - money)
            print("You are ready to play the game")
            option = str(input("Are you ready for your cards:"))
            if option == 'yes':
                Player_Hand.get_deck(self)
                random.shuffle(cards)
                hand = random.sample(cards, k=2)
                print(hand)
                results.append(values[hand[0]])
                results.append(values[hand[1]])
                print("card sum is :", results[0]+results[1])
                if results[0]+results[1] > 21:
                    print("your card sum exceed 21 you are busted")
                else:
                    h_s = input("do you want to hit or stay:")
                    while h_s == 'hit':
                        single_card = (random.sample(cards, k=1))
                        hand.append(single_card)
                        print(hand)
                        #we can also use extend method in lists will use it later
                        results.append(values[single_card[0]])
                        result_sum(results)
                        h_s = str(input("do you want to hit again:"))
                        if h_s == 'stay':
                            break
                    if h_s == 'stay':
                        print(" it is dealers turn")
                        Dealer.d_hit(self)

            else:
                print(" take your own time")


#deck = Deck()
# print(deck.get_deck())
pavan = Player_Hand(2000)
print(pavan.hit())
# using random.shuffle and random.sample
#dealer = Dealer()
# print(dealer.D_hit())
