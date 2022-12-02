# adventofcode 2022-02
import itertools

#data = "C X\nC X\nA Y\nC X\nB Y\nA X\nA Z\nB Y\nC Z\nC Z\nB X\nC Z\nB Y\nC Z\nB Y\nA Z\nB Y\nC X\nC X\nC X\nB X\nC Z\nC X\n"
data = open('/tmp/test', 'r').readlines()

# Points for outcome
WIN = 6
LOSE = 0
DRAW = 3
# Additional poins for hand played
SHAPE_SCORES = {'R': 1, 'P': 2, 'S': 3}

ITEMS = ('R', 'P', 'S')
LOOKUP = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'}

def win_or_lose(p1, p2):
    # Return player2 result by shifting the items for the first lookup.
    if p1 == p2: return DRAW
    elif (ITEMS*2)[1:].index(p1) == (ITEMS*2).index(p2):
        return LOSE
    return WIN

# Create a lookup for total points scored per play
results = dict()
for prod in itertools.product(ITEMS, repeat=2):
    results[prod] = win_or_lose(*prod) + SHAPE_SCORES[prod[1]]

# Get the scores
scores = list()
for line in data:
    p1, p2 = line.strip().split(' ')
    scores.append(results[(LOOKUP[p1], LOOKUP[p2])])

sum(scores)

# Part 2 (X Lose, Y Draw, Z Win)

def get_play(oponent, target_result):
    # Return the play required by p2 to either win, lsoe or draw
    lookup = {'X': LOSE, 'Y': DRAW, 'Z': WIN}
    res = lookup[target_result]
    for key, val in game_scores.ITEMS():
        if val == res and key[0] == oponent:
            return key[1]

scores.clear()
for line in data:
    p1, p2 = line.strip().split(' ')
    p2 = get_play(LOOKUP[p1], p2)
    scores.append(results[(LOOKUP[p1], p2)])
