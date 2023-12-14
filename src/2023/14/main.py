rocks = open("testcase.in").read().splitlines()

rocks = [list(row) for row in rocks]


def tiltRocks(line, dir):
    swaps = True
    if dir == "WEST" or dir == "NORTH":
        line = line[::-1]

    while swaps:
        swaps = False
        for i in range(len(line) - 1):
            if line[i] == "O" and line[i + 1] == ".":
                line[i], line[i + 1] = line[i + 1], line[i]
                swaps = True

    if dir == "WEST" or dir == "NORTH":
        return line[::-1]

    return line


def tiltCycle(rocks):
    cycle = ["NORTH", "WEST", "SOUTH", "EAST"]

    for dir in cycle:
        if dir == "NORTH" or dir == "SOUTH":
            rocks = [list(col) for col in zip(*rocks)]

        tilted = []
        for line in rocks:
            tilted.append(tiltRocks(line, dir))

        if dir == "NORTH" or dir == "SOUTH":
            tilted = [list(row) for row in zip(*tilted)]

        rocks = tilted

    return rocks


def stringifyRocks(rocks):
    return "".join(["".join(row) for row in rocks])


def runForNCycles(rocks, N):
    tilted = rocks
    cycleCount = 0
    cycleLength = 1
    hasCycle = False
    rockHist = {}
    rockHist[stringifyRocks(tilted)] = cycleCount

    while not hasCycle:
        hasCycle = True
        tilted = tiltCycle(tilted)
        cycleCount += 1
        lookup = stringifyRocks(tilted)

        if cycleCount == N:
            return tilted

        if lookup not in rockHist:
            hasCycle = False
            rockHist[lookup] = cycleCount

        cycleLength = cycleCount - rockHist[lookup]

    remainingCycles = (N - rockHist[stringifyRocks(tilted)]) % cycleLength

    for _ in range(remainingCycles):
        tilted = tiltCycle(tilted)

    return tilted


def calcTotalLoad(rocks):
    reversedCols = [list(col)[::-1] for col in zip(*rocks)]
    total = 0
    for col in reversedCols:
        for ind, char in enumerate(col):
            if char == "O":
                total += ind + 1

    return total


def solvePart1(rocks):
    tilted = []
    rocks = [list(col) for col in zip(*rocks)]

    for line in rocks:
        tilted.append(tiltRocks(line, "NORTH"))

    tilted = [list(row) for row in zip(*tilted)]

    total = calcTotalLoad(tilted)
    return total


part1 = solvePart1(rocks)
part2 = calcTotalLoad(runForNCycles(rocks, 1000000000))

print("Part 1:", part1)
print("Part 2:", part2)
