# north(^), south(v), east( >), or west( <).

moves = open("input.txt", "r").read()

x = y = 0

gridPos = {
    'x': x,
    'y': y
}

alreadyReceived = [gridPos]

atLeastOnePresent = 1

for move in moves:
    match move:
        case '^':
            y += 1
        case 'v':
            y -= 1
        case '>':
            x += 1
        case '<':
            x -= 1

    gridPos = {
        'x': x,
        'y': y
    }

    if gridPos not in alreadyReceived:
        alreadyReceived.append(gridPos)
        atLeastOnePresent += 1

print(str(atLeastOnePresent) + ' houses received at least one present.' + ' (part 1)')
