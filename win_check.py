import tiles
#RULES.
#TO WIN A GAME, YOU MUST HAVE EXACTLY 14 MELDED TILES
#A MELD IS DEFINED AS A GROUP/COMBINATION OF TILES, 3 OR MORE
#TWO TYPES OF MELDS, GROUPS AND RUNS
#GROUPS MUST BE THE SAME NUMBER IN DIFFERENT, UNIQUE COLORS (MAX MELD SIZE OF 4)
#RUNS ARE CONSECUTIVE NUMBERS IN THE SAME COLOR

def check_win(hand, okey):
    matrix = [[0 for _ in range(13)] for _ in range(4)]
    wilds = 0
    for tile in hand:
        if tile == okey:
            wilds += 1
            continue
        elif tile == tiles.FAKE_OKEY:  # Fake okeys represent the okey tile
            matrix[tiles.tile_color(okey)][tiles.tile_number(okey) - 1] += 1
            continue
        tnum = tiles.tile_number(tile)
        tcolor = tiles.tile_color(tile)
        matrix[tcolor][tnum - 1] += 1
    print(matrix,wilds)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                print("Tile at",(i,j),sep=" ")
            else:
                continue
    return matrix


#[1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]
#[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]
#[0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1]
#[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]

hand = [0, 1, 2, 3, 9, 16, 20, 24, 29, 32, 38, 42, 47, 49] #okey is 49 ind is 48
check_win(hand,49)

