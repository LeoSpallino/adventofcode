import re
import itertools

galaxy = open("testcase.in").read().splitlines()


def expand(galaxy: list[str]):
    emptyRows = []
    emptyCols = []

    for ind, row in enumerate(galaxy):
        if len(re.findall(r"(#)", row)) == 0:
            emptyRows.append(ind)

    cols = ["".join(col) for col in zip(*[list(row) for row in galaxy])]

    for ind, col in enumerate(cols):
        if len(re.findall(r"(#)", col)) == 0:
            emptyCols.append(ind)

    return emptyRows, emptyCols


def manhattanDistance(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2

    return abs(p1x - p2x) + abs(p1y - p2y)


def getExpandedUniverses(galaxy, emptyRows, emptyCols, expansionFactor):
    universes = set()

    for r in range(len(galaxy)):
        for c in range(len(galaxy[0])):
            if galaxy[r][c] == "#":
                numRows = len(list(filter(lambda i: i <= r, emptyRows)))
                numCols = len(list(filter(lambda i: i <= c, emptyCols)))
                coord = (
                    r + numRows * (expansionFactor - 1),
                    c + numCols * (expansionFactor - 1),
                )
                universes.add(coord)

    return universes


def calcTotalLengths(galaxy, expansionFactor):
    total = 0
    emptyRows, emptyCols = expand(galaxy)
    universes = getExpandedUniverses(galaxy, emptyRows, emptyCols, expansionFactor)

    combinations = list(itertools.combinations(universes, 2))

    for combo in combinations:
        total += manhattanDistance(combo[0], combo[1])

    return total


print("Part 1:", calcTotalLengths(galaxy, 2))
print("Part 2:", calcTotalLengths(galaxy, 1000000))
