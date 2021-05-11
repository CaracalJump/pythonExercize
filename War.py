from random import shuffle

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """suit and value are integer"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
            # if self.suit < c2.suit:
            #     return True
            # else:
            #     return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
            # if self.suit > c2.suit:
            #     return True
            # else:
            #     return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v


class Deck:

    def __init__(self):
        self.cards = []
        self.add_cards()

    def add_cards(self):
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
            shuffle(self.cards)

    # def rm_card(self):
    def draw(self):
        if len(self.cards) == 0:
            self.add_cards()
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.winssum = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("Name of Player1: ")
        name2 = input("Name of Player2: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        w = "This round, winner is {}."
        # w = w.format(winner)
        # print(w)
        print(w.format(winner.name))

    def print_draw(self, p1, p2):
        d = "{} is {}, {} is {}."
        # d = d.format(p1n, p1c, p2n, p2c)
        # print(d)
        print(d.format(p1.name, p1.card, p2.name, p2.card))

    def play_game(self):
        cards = self.deck.cards
        print("Let's start a game!")
        while len(cards) >= 2:
            m = "q to quit, play to other keys: "
            response = input(m)
            if response == "q":
                    break
            n = input("What time will you war?: ")
            for j in range(0, int(n)-1):
                for i in range(0, 26):
                    self.p1.card = self.deck.draw()
                    self.p2.card = self.deck.draw()
                    self.print_draw(self.p1, self.p2)
                    if self.p1.card > self.p2.card:
                        self.p1.wins += 1
                        # self.wins(self.p1.name)
                        self.print_winner(self.p1)
                    else:
                        self.p2.wins += 2
                        self.print_winner(self.p2)

            win = self.winner(self.p1, self.p2)
            print("Game Over! {} is winner!".format(win))
            self.p1.winssum += self.p1.wins
            self.p2.winssum += self.p2.wins
            print("{} won {} times, and {} won {} times".format(self.p1.name, self.p1.wins, self.p2.name, self.p2.wins))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Draw!"


game = Game()
game.play_game()


    




    
