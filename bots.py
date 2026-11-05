import random
#RULES.
#TO WIN A GAME, YOU MUST HAVE EXACTLY 14 MELDED TILES
#A MELD IS DEFINED AS A GROUP/COMBINATION OF TILES, 3 OR MORE
#TWO TYPES OF MELDS, GROUPS AND RUNS
#GROUPS MUST BE THE SAME NUMBER IN DIFFERENT, UNIQUE COLORS (MAX MELD SIZE OF 4)
#RUNS ARE CONSECUTIVE NUMBERS IN THE SAME COLOR
class RandBot:
    def choose_discard(self, hand):
        return random.choice(hand)

    def choose_draw(self, hand, last_discard):
        return random.choice(["deck", "discard"])
    

class SmartBot:
    def organizeStart(self, hand, okey):
        return