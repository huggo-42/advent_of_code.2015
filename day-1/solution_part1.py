f = open("input.txt", "r").read()

# possible moves are ( and )
# ( = up 1 floor
# ) = down 1 floor

possibleMoves = {
    '(': 1,
    ')': -1
}

floor = 0
for c in f:
    floor += possibleMoves[c]

print('The instructions takes Santa to floor: ' + str(floor) + ' (part 1)')
