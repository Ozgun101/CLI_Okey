import game
import tiles
#RULES.
#TO WIN A GAME, YOU MUST HAVE EXACTLY 14 MELDED TILES
#A MELD IS DEFINED AS A GROUP/COMBINATION OF TILES, 3 OR MORE
#TWO TYPES OF MELDS, GROUPS AND RUNS
#GROUPS MUST BE THE SAME NUMBER IN DIFFERENT, UNIQUE COLORS (MAX MELD SIZE OF 4)
#RUNS ARE CONSECUTIVE NUMBERS IN THE SAME COLOR

def check_win(hand,okey): #TO CHECK WINS, WE DEFINE A 2D MATRIX OF THE PLAYERS HAND, FOR EACH ROW AND COLUMN COMBINATION, THE MELD IS SEPERATED
    matrix = [[0 for _ in range(13)] for _ in range(4)]
    for tile in hand:
        if tile == tiles.FAKE_OKEY:
            wilds += 1
            continue
        tnum = tiles.tile_number(tile)
        tcolor = tiles.tile_color(tile)
        matrix[tcolor][tnum - 1] += 1
    return(matrix)



hand = [10, 35, 34, 45, 29, 33, 37, 49, 3, 33, 28, 42, 16, 10, 17]
print(check_win(hand,1))

