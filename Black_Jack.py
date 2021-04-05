"""Black_Jack"""
import random
import os


class Card:
    def __init__(self, value: str, suit: str):
        self.__value = value
        self.__suit = suit

    def cost_card(self) -> int:
        if self.__value in ("", "A", "2", "3", "4", "5", "6", "7", "8", "9"):
            return ("", "A", "2", "3", "4", "5", "6", "7", "8", "9").index(self.__value)
        elif self.__value in ("В", "Д", "К"):
            return 10
        elif self.__value == "Т":
            return 11

    def card_info(self):
        return f"{self.__value}{self.__suit}"


class DeckCards:
    def __init__(self) -> None:
        self.__deck_cards = [Card(a, b) for b in ("♣", "♥", "♠", "♦") for a in
                             ("A", "2", "3", "4", "5", "6", "7", "8", "9", "В", "Д", "К", "Т")]

        random.shuffle(self.__deck_cards)

    def get_card_from_deck(self) -> Card:  # Card("5", "♣")
        return self.__deck_cards.pop()

    def show_deck(self):
        for card in self.__deck_cards:
            print(card.card_info())


class Player:
    def __init__(self, name):
        self.__name = name
        self._hand = []
        self.score = 0
        self.money = 100

    def info(self):
        return f'{self.__name} hand: {self._hand} - Score {self.score}     |money = {self.money}|'

    def hand(self, karta):
        self._hand.append(karta.card_info())
        self.score += karta.cost_card()

    def show_hand(self):  # old
        return f"{self._hand} score:{self.score}"

    def new_show_hand(self):
        [print(f"┌────────┐", end=" ") for a in self._hand]
        print()
        [print(f'│      {a}│', end=' ') for a in self._hand]
        print()
        [print(f'│        │', end=' ') for a in self._hand]
        print()
        [print(f'│        │', end=' ') for a in self._hand]
        print()
        [print(f'│        │', end=' ') for a in self._hand]
        print()
        [print(f'│{a}      │', end=' ') for a in self._hand]
        print()
        [print(f'└────────┘', end=' ') for a in self._hand]
        print()


class Dealer(Player):
    def get_cards(self, koloda):
        while self.score <= 16:
            self.hand(koloda.get_card_from_deck())


class Game:
    def __init__(self):
        self.igrok = Player(name='Player')
        self.dealer = Dealer(name="Dealer")
        self.koloda = DeckCards()
        self.rate = 0

    def rates(self):
        if self.igrok.money == 0:
            print("GameOver! You Lose!\n")
            pass

        elif self.dealer.money == 0:
            print("GameOver! You Win!\n")
        self.rate = int(input(f'Igrok.money = {self.igrok.money}\nDealer.money = {self.dealer.money}\nRates: '))
        while self.rate > self.igrok.money or self.rate > self.dealer.money:
            print("not enough money, try again ")
            self.rate = int(input('Ваша ставка: '))

        self.igrok.money -= self.rate
        self.dealer.money -= self.rate

    def check(self):
        if self.igrok.score > 21:
            self.dealer.money += self.rate * 2
            print(f'\nВы проиграли:\n{self.igrok.info()}\n{self.dealer.info()}')

        elif self.dealer.score > 21 and self.igrok.score <= 21:
            self.igrok.money += self.rate * 2
            print(f'\nВы победили.\n{self.igrok.info()}\n{self.dealer.info()}')

        elif self.dealer.score == self.igrok.score:
            self.igrok.money += self.rate
            self.dealer.money += self.rate
            print(f'\nНичья.\n{self.igrok.info()}\n{self.dealer.info()}')

        elif self.dealer.score > self.igrok.score:
            self.dealer.money += self.rate * 2
            print(f'\nВы проиграли.\n{self.igrok.info()}\n{self.dealer.info()}')

        elif self.dealer.score < self.igrok.score:
            self.igrok.money += self.rate * 2
            print(f'\nВы победили.\n{self.igrok.info()}\n{self.dealer.info()}')

    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.rates()
        os.system('cls' if os.name == 'nt' else 'clear')

        self.igrok.hand(self.koloda.get_card_from_deck())
        self.igrok.hand(self.koloda.get_card_from_deck())

        self.dealer.hand(self.koloda.get_card_from_deck())
        self.dealer.hand(self.koloda.get_card_from_deck())

        self.igrok.new_show_hand()

        while self.igrok.score < 21:
            answer = input("Ещё карту? y/n ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if answer == "y":
                self.igrok.hand(self.koloda.get_card_from_deck())
                self.igrok.new_show_hand()
            elif answer == "n":
                self.igrok.new_show_hand()
                self.dealer.get_cards(self.koloda)
                break

        self.check()
        self.igrok._hand = []
        self.dealer._hand = []
        self.igrok.score = 0
        self.dealer.score = 0
        input("\nPUSH A BUTTON TO GO THE NEXT ROUND")


def main():
    game = Game()
    while True:
        game.start()


if __name__ == '__main__':
    main()
