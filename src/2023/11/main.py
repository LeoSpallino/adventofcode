import re
import itertools

universe = open("testcase.in").read().splitlines()


def expand(universe: list[str]):
    emptyRows = []
    emptyCols = []

    for ind, row in enumerate(universe):
        if len(re.findall(r"(#)", row)) == 0:
            emptyRows.append(ind)

    cols = ["".join(col) for col in zip(*[list(row) for row in universe])]

    for ind, col in enumerate(cols):
        if len(re.findall(r"(#)", col)) == 0:
            emptyCols.append(ind)

    return emptyRows, emptyCols


def manhattanDistance(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2

    return abs(p1x - p2x) + abs(p1y - p2y)


def getExpandedGalaxies(universe, emptyRows, emptyCols, expansionFactor):
    galaxies = set()

    for r in range(len(universe)):
        for c in range(len(universe[0])):
            if universe[r][c] == "#":
                numRows = len(list(filter(lambda i: i <= r, emptyRows)))
                numCols = len(list(filter(lambda i: i <= c, emptyCols)))
                coord = (
                    r + numRows * (expansionFactor - 1),
                    c + numCols * (expansionFactor - 1),
                )
                galaxies.add(coord)

    return galaxies


def calcTotalLengths(universe, expansionFactor):
    total = 0
    emptyRows, emptyCols = expand(universe)
    universes = getExpandedGalaxies(universe, emptyRows, emptyCols, expansionFactor)

    combinations = list(itertools.combinations(universes, 2))

    for combo in combinations:
        total += manhattanDistance(combo[0], combo[1])

    return total


print("Part 1:", calcTotalLengths(universe, 2))
print("Part 2:", calcTotalLengths(universe, 1000000))
