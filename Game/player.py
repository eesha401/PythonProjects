import random


class Player:

    def __init__(self, name, dealer):
        self.name = name
        self.dealer = dealer
        self.win = 0
        self.tie = 0
        self.loss = 0
        self.hand = []
        return


    def decide_hit(self):
        return random.choice([True, True, False])


    def deal_to(self, card_value):

        self.hand.append(card_value)
        return


    @property
    def card_sum(self):

        count = 0
        for i in self.hand:
            count += i
        return count


    def play_round(self):
        while self.decide_hit() == True and self.card_sum < 21:
            self.dealer.signal_hit(self)
        return


    def discard_hand(self):

        self.hand.clear()
        return


    @property
    def wins(self):
        return self.win


    @property
    def ties(self):
        return self.tie


    @property
    def losses(self):
        return self.loss


    def record_win(self):

        self.win += 1
        return


    def record_loss(self):

        self.loss += 1
        return


    def record_tie(self):

        self.tie += 1
        return


    def reset_stats(self):

        self.win = 0
        self.tie = 0
        self.loss = 0
        return

    def __repr__(self):

        return "{}: {} {}/{}/{}".format(self.name, self.hand, self.wins, self.ties, self.losses)


