import random

class RandBot:
    def choose_discard(self, hand):
        return random.choice(hand)

    def choose_draw(self, hand, last_discard):
        return random.choice(["deck", "discard"])