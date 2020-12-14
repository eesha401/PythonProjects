import random


class CardDeck:
    class Card:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __repr__(self):
            return "{}".format(self.value)

    def __init__(self):
        self.top = None

    def shuffle(self):
        card_list = 4 * [x for x in range(2, 12)] + 12 * [10]
        random.shuffle(card_list)

        self.top = None

        for card in card_list:
            new_card = self.Card(card)
            new_card.next = self.top
            self.top = new_card

    def __repr__(self):
        curr = self.top
        out = ""
        card_list = []
        while curr is not None:
            card_list.append(str(curr.value))
            curr = curr.next

        return " ".join(card_list)

    def draw(self):
        top_card = self.top
        if self.top == None:
            return
        elif self.top.next == None:
            self.top == None
        else:
            self.top = self.top.next
        return top_card.value

