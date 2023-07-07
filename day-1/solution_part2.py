f = open("input.txt", "r").read()

possibleMoves = {
    '(': 1,
    ')': -1
}

floor = 0
for idx in range(len(f)):
    floor += possibleMoves[f[idx]]
    if floor == -1:
        print('The instructions takes Santa to the basement at position: ' + str(idx + 1) + ' (part 2)')
        break
