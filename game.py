import tiles
import random

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
    return deck, playerhands, starter,indicator, okey



def main():
    deck,playerhands,starter,indicator,okey = init_game()
    for i in range(len(playerhands)):
        print("Player ",(i+1),": ",playerhands[i],sep="")
    print("\n", "OKEY:", tiles.tile_name(okey))


if __name__ == "__main__":
    main()