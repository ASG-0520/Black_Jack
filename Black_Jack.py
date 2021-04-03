"""Black_Jack"""
import random


class Card:
    def __init__(self, value: str, suit: str):
        self.__value = value
        self.__suit = suit

    def cost_card(self) -> int:
        if self.__value in ("", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
            return ("", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10").index(self.__value)
        elif self.__value in ("Валет", "Дама", "Король"):
            return 10
        elif self.__value == "Туз":
            return 11

    def card_info(self) -> str:
        return f"{self.__value}{self.__suit}"  # 4♥


class DeckCards:
    def __init__(self) -> None:
        self.__deck_cards = [Card(a, b) for b in ("♣", "♥", "♠", "♦") for a in
                             ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз")]

        random.shuffle(self.__deck_cards)

    def get_carf_from_deck(self) -> Card:  # Card("5", "♣")
        return self.__deck_cards.pop()

    # def show_deck(self):
    #     for card in self.deck_cards:
    #         print(card.card_info())


class Player:
    def __init__(self, name):
        self.__name = name
        self._hand = []
        self.score = 0
        self.money = 100

    def info(self):
        return f'{self.__name}\nHand: {self._hand}'

    def hand(self, karta):
        self._hand.append(karta.card_info())
        self.score += karta.cost_card()

    def show_hand(self):
        return f"{self._hand}"  # score:{self.score}


class Dealer(Player):
    def get_cards(self, karta):
        while self.score <= 16:
            self.hand(karta)


class Game:
    def __init__(self):
        self.igrok = Player(name='Player')
        self.dealer = Dealer(name="Dealer")
        self.koloda = DeckCards()

    def check(self):
        if self.igrok.score > 21:
            print(f'\nВы проиграли.\n{self.igrok.info()}\n{self.dealer.info()}')
        elif self.dealer.score > 21 and self.igrok.score <= 21:
            print(f'\nВы победили.\n{self.igrok.info()}\n{self.dealer.info()}')
        elif self.dealer.score == self.igrok.score:
            print(f'\nНичья.\n{self.igrok.info()}\n{self.dealer.info()}')
        elif self.dealer.score > self.igrok.score:
            print(f'\nВы проиграли.\n{self.igrok.info()}\n{self.dealer.info()}')
        elif self.dealer.score < self.igrok.score:
            print(f'\nВы победили.\n{self.igrok.info()}\n{self.dealer.info()}')

    def start(self):

        self.igrok.hand(self.koloda.get_carf_from_deck())
        self.igrok.hand(self.koloda.get_carf_from_deck())

        self.dealer.hand(self.koloda.get_carf_from_deck())
        self.dealer.hand(self.koloda.get_carf_from_deck())

        print(self.igrok.show_hand())

        while self.igrok.score < 21:
            answer = input("Ещё карту? y/n ")
            if answer == "y":
                self.igrok.hand(self.koloda.get_carf_from_deck())
                print(self.igrok.show_hand())
            elif answer == "n":
                print(self.igrok.show_hand())
                self.dealer.get_cards(self.koloda.get_carf_from_deck())
                break

        self.check()


def main():
    game = Game()
    game.start()


if __name__ == '__main__':
    main()
