from player import Player
from card_deck import CardDeck


class Dealer(Player):

    def __init__(self):
        self.deck = CardDeck()
        super().__init__('Dealer', self)

        return

    def shuffle_deck(self):

        self.deck.shuffle()
        return

    def signal_hit(self, player):

        player.deal_to(self.deck.draw())
        return

    def play_round(self):

        while self.card_sum < 17:
            self.deal_to(self.deck.draw())
        return


