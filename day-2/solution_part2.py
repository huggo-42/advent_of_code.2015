f = open("input.txt", "r").readlines()

total_ribbon = 0

for line in f:
    dimensions = line.split('x')
    dimensions = [float(dimensions[0]), float(dimensions[1]), float(dimensions[2])]

    wrap = 0
    bow = 1
    crossedMaxDimension = False

    for dimension in dimensions:
        if dimension != max(dimensions) or crossedMaxDimension == True:
            wrap += 2 * dimension
        else:
            crossedMaxDimension = True
        bow *= dimension

    total_ribbon += wrap + bow

print('The elves should order ' + str(total_ribbon) + ' square feet of wrapping paper.')
