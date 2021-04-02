"""Black_Jack"""
import random


class Card:
    def __init__(self, value: str, suit: str):
        self.__value = value
        self.__suit = suit

    def card_info(self) -> str:
        return f"{self.__value} {self.__suit}"

    def cost_card(self) -> int:
        if self.__value in " А23456789":
            return " А23456789".index(self.__value)
        elif self.__value in ("Валет", "Дама", "Король"):
            return 10
        elif self.__value == "Т":
            return 11


class DeckCards:
    def __init__(self):
        self.deck_cards = [Card(a, b) for b in ("♣", "♥", "♠", "♦") for a in
                           ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз")]

    def show_deck(self):
        for card in self.deck_cards:
            print(card.card_info())


class Player:
    def __init__(self, name):
        self.__name = name
        self._hand = []
        self.score = 0
        self.money = 100

    def info(self):
        print(f'Player: {self.__name}\nMoney: {self.money}\nHand: {self._hand}')

    def hand(self, karta):
        self._hand.append(karta.card_info())

    def show_hand(self):
        return self._hand


class Dealer(Player):

    @staticmethod
    def shuffle_the_cards(DeckCards):
        random.shuffle(DeckCards.deck_cards)

    @staticmethod
    def get_carf_from_deck(DeckCards):
        DeckCards.deck_cards.pop()
        return DeckCards.deck_cards.pop()


class Game:
    def __init__(self):
        self.player = Player(name='Player1')
        self.dealer = Dealer(name="Dealer")
        self.stopka = DeckCards()
        self.card = self.dealer.get_carf_from_deck(self.stopka)

    def rules(self):
        if self.player.score > 21:
            print(f'\nВы проиграли.\n{self.player.info()}\n{self.dealer.info()}')
        elif self.dealer.score > 21 and self.player.score <= 21:
            print(f'\nВы победили.\n{self.player.info()}\n{self.dealer.info()}')
        elif self.dealer.score == self.player.score:
            print(f'\nНичья.\n{self.player.info()}\n{self.dealer.info()}')
        elif self.dealer.score > self.player.score:
            print(f'\nВы проиграли.\n{self.player.info()}\n{self.dealer.info()}')
        elif self.dealer.score < self.player.score:
            print(f'\nВы победили.\n{self.player.info()}\n{self.dealer.info()}')

    def start(self):
        self.dealer.shuffle_the_cards(self.stopka)

        self.player.hand(self.card)
        self.player.hand(self.card)

        self.dealer.hand(self.card)
        self.dealer.hand(self.card)

        print(self.player.show_hand())

        while self.player.score < 21:
            answer = input("Ещё карту? y/n")
            if answer == "y":
                self.player.hand(self.card)
                print(self.player.show_hand())
        #     elif answer == "n":
        #
        # print(self.rules())

        # self.player.info()


def main():
    game = Game()
    game.start()


if __name__ == '__main__':
    main()
