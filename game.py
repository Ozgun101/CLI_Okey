import tiles, random, simulate
from dataclasses import dataclass

@dataclass
class GameState:
    deck: list
    playerhands: list
    starter: int
    indicator: int
    okey: int

def init_game():
    deck = tiles.create_tiles()
    random.shuffle(deck)
    playerhands = [deck[0:14],deck[14:28],deck[28:42],deck[42:56]]
    starter = random.randint(0,3)
    playerhands[starter].append(deck[56])
    del deck[:57]
    indicatorindex = random.randint(0,48)
    while tiles.is_fake_okey(deck[indicatorindex]):
        indicatorindex = random.randint(0,48)
    indicator = deck.pop(indicatorindex)
    okey = tiles.get_okey_tile(indicator)
    return GameState(deck, playerhands, starter, indicator, okey)




def main():
    state = init_game()
    for i in range(len(state.playerhands)):
        deconstructed_hand = []
        for num in state.playerhands[i]:
            deconstructed_hand.append(tiles.tile_name(num))
        deconstructed_hand.insert((len(deconstructed_hand)//2),"\n")
        print(state.starter)
        print("                         PLAYER",(i+1) if (i+1) != state.starter else ("~~")) ##p. if (i) == state.starter "~~" else: 1)
        output = ""
        for i in deconstructed_hand:
            if i == "\n":
                output += "\n"
            else:
                output+=i + " "
        print(output,"\n")
    print("\n", "OKEY:", tiles.tile_name(state.okey))


    simulate.simulate(state)


if __name__ == "__main__":
    main()