import bots, tiles
import random

def simulate(state):
    players = [bots.RandBot() for _ in range(4)]
    player = state.starter
    discards = []
    while True:
        hand = state.playerhands[player]
        
        if len(hand) == 14:##Pick up OR Discard
            if not state.deck:
                break
            last_discard = discards[-1][-1]
            choice = players[player].choose_draw(hand, last_discard)
            if choice == "discard":
                hand.append(last_discard)
            else:
                hand.append(state.deck.pop())
        
        tile = players[player].choose_discard(hand)
        hand.remove(tile)
        discards.append((player, tile))
        print(f"Player {player + 1}: {hand}")
        player = (player + 1) % 4