COLORS = ("Red", "Yellow", "Blue", "Black")
NUM_COLORS = len(COLORS)
NUM_NUMBERS = 13
FAKE_OKEY = 52 #Reserved ID for joker
NUM_TILE_TYPES = 53


def make_tile(color, number):
    """Convert a color index (0-3) and number (1-13) to a tile ID."""
    if not 0 <= color < NUM_COLORS:
        raise ValueError(f"Invalid color: {color}")
    if not 1 <= number <= NUM_NUMBERS:
        raise ValueError(f"Invalid number: {number}")
    return color * NUM_NUMBERS + (number - 1)


def is_fake_okey(tile):
    return tile == FAKE_OKEY


def tile_color(tile):
    """Return a tile's color index."""
    if is_fake_okey(tile):
        raise ValueError("The fake okey has no fixed color")
    return tile // NUM_NUMBERS

def get_okey_tile(indicator):
    color = tile_color(indicator)
    number = tile_number(indicator) % NUM_NUMBERS + 1
    return make_tile(color, number)

def tile_number(tile):
    """Return a tile's number from 1 to 13."""
    if is_fake_okey(tile):
        raise ValueError("The fake okey has no fixed number")
    return tile % NUM_NUMBERS + 1


def tile_name(tile):
    """Return a readable name, such as 'Red 7'."""
    if is_fake_okey(tile):
        return "Fake Okey"
    return f"{COLORS[tile_color(tile)]} {tile_number(tile)}"


def create_tiles():
    """Return all 106 tiles: two of each numbered tile and two fake okeys."""
    return list(range(FAKE_OKEY)) * 2 + [FAKE_OKEY] * 2


def hand_to_counts(hand):
    """Convert a hand to a list of 53 tile counts."""
    counts = [0] * NUM_TILE_TYPES
    for tile in hand:
        counts[tile] += 1
    return counts