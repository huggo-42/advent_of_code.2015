# length l
# width w
# height h
# formula -> 2*l*w + 2*w*h + 2*h*l + the area of the smallest side

f = open("input.txt", "r").readlines()

total_area = 0
for line in f:
    dimensions = line.split('x')
    dimensions = [float(dimensions[0]), float(dimensions[1]), float(dimensions[2])]

    l, w, h = dimensions[0], dimensions[1], dimensions[2]

    side1 = l * w
    side2 = w * h
    side3 = h * l

    smallest_side = float(min([side1, side2, side3]))

    surface_area = (2 * side1) + (2 * side2) + (2 * side3)

    total_area += surface_area + smallest_side

print('The elves should order ' + str(total_area) + ' square feet of wrapping paper.')
