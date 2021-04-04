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

    def card_info(self):  # -> str:
        return f"{self.__value}{self.__suit}"  # 4♥
        # return self.__value, self.__suit


class DeckCards:
    def __init__(self) -> None:
        self.__deck_cards = [Card(a, b) for b in ("♣", "♥", "♠", "♦") for a in
                             ("A", "2", "3", "4", "5", "6", "7", "8", "9", "В", "Д", "К", "Т")]

        random.shuffle(self.__deck_cards)

    def get_carf_from_deck(self) -> Card:  # Card("5", "♣")
        return self.__deck_cards.pop()

    # def show_deck(self):
    #     for card in self.__deck_cards:
    #         print(card.card_info())


class Player:
    def __init__(self, name):
        self.__name = name
        self._hand = []
        self.score = 0
        self.money = 100

    def info(self):
        return f'{self.__name} hand: {self._hand} - Score {self.score}'

    def hand(self, karta):
        self._hand.append(karta.card_info())
        self.score += karta.cost_card()

    def show_hand(self):
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
            self.hand(koloda.get_carf_from_deck())


class Game:
    def __init__(self):
        self.igrok = Player(name='Player')
        self.dealer = Dealer(name="Dealer")
        self.koloda = DeckCards()

    def check(self):
        if self.igrok.score > 21:
            print(f'\nВы проиграли:\n{self.igrok.info()}\n{self.dealer.info()}')
        elif self.dealer.score > 21 and self.igrok.score <= 21:
            print(f'\nВы победили.\n{self.igrok.info()}\n{self.dealer.info()}')
        elif self.dealer.score == self.igrok.score:
            print(f'\nНичья.\n{self.igrok.info()}\n{self.dealer.info()}')
        elif self.dealer.score > self.igrok.score:
            print(f'\nВы проиграли.\n{self.igrok.info()}\n{self.dealer.info()}')
        elif self.dealer.score < self.igrok.score:
            print(f'\nВы победили.\n{self.igrok.info()}\n{self.dealer.info()}')

    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.igrok.hand(self.koloda.get_carf_from_deck())
        self.igrok.hand(self.koloda.get_carf_from_deck())

        self.dealer.hand(self.koloda.get_carf_from_deck())
        self.dealer.hand(self.koloda.get_carf_from_deck())

        self.igrok.new_show_hand()
        # self.dealer.new_show_hand()
        # print(self.igrok.show_hand())  # ['5♥', '2♠'] score:7

        while self.igrok.score < 21:
            answer = input("Ещё карту? y/n ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if answer == "y":
                self.igrok.hand(self.koloda.get_carf_from_deck())
                self.igrok.new_show_hand()
            elif answer == "n":
                self.igrok.new_show_hand()
                self.dealer.get_cards(self.koloda)
                break

        self.check()


def main():
    game = Game()
    game.start()


if __name__ == '__main__':
    main()
