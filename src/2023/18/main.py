steps = open("testcase.in").read().splitlines()


RIGHT, LEFT, UP, DOWN = (0, 1), (0, -1), (-1, 0), (1, 0)
opLookup = {"R": RIGHT, "L": LEFT, "U": UP, "D": DOWN}


def shoelace(bounds):
    total = 0
    for i in range(len(bounds) - 1):
        y1, x1 = bounds[i]
        y2, x2 = bounds[i + 1]
        total += x1 * y2 - x2 * y1

    yn, xn = bounds[-1]
    y1, x1 = bounds[0]
    total += xn * y1 - x1 * yn

    return abs(total) / 2


def calcPerim(bounds):
    total = 0
    for i in range(len(bounds) - 1):
        y1, x1 = bounds[i]
        y2, x2 = bounds[i + 1]
        total += max(abs(y2 - y1), abs(x2 - x1))

    y1, x1 = bounds[-1]
    y2, x2 = bounds[0]
    total += max(abs(y2 - y1), abs(x2 - x1))
    return total


def calcArea(bounds):
    innerArea = shoelace(bounds[::-1])
    perim = calcPerim(bounds)
    area = perim / 2 + innerArea + 1
    return int(area)


def part1(steps):
    currLoc = [0, 0]
    bounds = []
    global opLookup

    parseStep = lambda step: [
        step.split(" ")[0],
        int(step.split(" ")[1]),
        step.split(" ")[2],
    ]
    steps = [parseStep(step) for step in steps]

    for step in steps:
        dir, length, color = step
        op = opLookup[dir]
        currLoc = [currLoc[0] + op[0] * length, currLoc[1] + op[1] * length]
        bounds.append(tuple(currLoc))

    return calcArea(bounds)


def part2(steps):
    currLoc = [0, 0]
    bounds = []
    global opLookup
    dirLookup = {0: "R", 1: "D", 2: "L", 3: "U"}

    parsedSteps = []
    for step in steps:
        _, _, color = step.split(" ")
        length, dir = color[2:7], color[7:8]
        parsedSteps.append([dirLookup[int(dir)], int(length, 16)])

    for step in parsedSteps:
        dir, length = step
        op = opLookup[dir]
        currLoc = [currLoc[0] + op[0] * length, currLoc[1] + op[1] * length]
        bounds.append(tuple(currLoc))

    return calcArea(bounds)


print("Part 1:", part1(steps))
print("Part 2:", part2(steps))
