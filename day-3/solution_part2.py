# north(^), south(v), east( >), or west( <).

moves = open("input.txt", "r").read()

xSanta = ySanta = xRoboSanta = yRoboSanta = 0

gridPosSanta = {
    'x': xSanta,
    'y': ySanta
}

gridPosRoboSanta = {
    'x': xRoboSanta,
    'y': yRoboSanta
}

alreadyReceived = [gridPosSanta]

atLeastOnePresent = 1

for idx in range(len(moves)):
    if idx % 2 == 0:
        isSanta = True
    else:
        isSanta = False

    x = y = 0
    match moves[idx]:
        case '^':
            y += 1
        case 'v':
            y -= 1
        case '>':
            x += 1
        case '<':
            x -= 1

    if isSanta:
        xSanta += x
        ySanta += y
        gridPosSanta = {
            'x': xSanta,
            'y': ySanta
        }
        if gridPosSanta not in alreadyReceived:
            alreadyReceived.append(gridPosSanta)
            atLeastOnePresent += 1
    else:
        xRoboSanta += x
        yRoboSanta += y
        gridPosRoboSanta = {
            'x': xRoboSanta,
            'y': yRoboSanta
        }
        if gridPosRoboSanta not in alreadyReceived:
            alreadyReceived.append(gridPosRoboSanta)
            atLeastOnePresent += 1

print(str(atLeastOnePresent) + ' houses received at least one present with Santa and RoboSanta giving presents together.' + ' (part 2)')
