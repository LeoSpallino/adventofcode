grid = open("testcase.in").read().splitlines()

UP, DOWN, RIGHT, LEFT = (0 - 1j), (0 + 1j), (1 + 0j), (-1 + 0j)
tileLookup = {
    ".": {RIGHT: [RIGHT], LEFT: [LEFT], DOWN: [DOWN], UP: [UP]},
    "/": {RIGHT: [UP], LEFT: [DOWN], DOWN: [LEFT], UP: [RIGHT]},
    "\\": {RIGHT: [DOWN], LEFT: [UP], DOWN: [RIGHT], UP: [LEFT]},
    "-": {RIGHT: [RIGHT], LEFT: [LEFT], UP: [RIGHT, LEFT], DOWN: [RIGHT, LEFT]},
    "|": {RIGHT: [UP, DOWN], LEFT: [UP, DOWN], UP: [UP], DOWN: [DOWN]},
}


def isOutOfBounds(coord: complex):
    row, col = int(coord.imag), int(coord.real)
    return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])


def getNextBeamPos(coord: complex, dir: complex):
    row, col = int(coord.imag), int(coord.real)
    next = tileLookup[grid[row][col]][dir]
    return [(coord + n, n) for n in next]


def traverse(startPoint: tuple[int, int], startDir: complex):
    visited: dict[complex, set[complex]] = {}
    beams = [(complex(*startPoint), startDir)]

    while len(beams):
        coord, dir = beams.pop()
        if coord in visited and dir in visited[coord]:
            continue
        if isOutOfBounds(coord):
            continue
        if coord not in visited:
            visited[coord] = set()
        visited[coord].add(dir)
        for pos in getNextBeamPos(coord, dir):
            beams.append(pos)

    return len(visited)


highestEnergy = 0

for i in range(len(grid)):
    highestEnergy = max(
        highestEnergy,
        traverse((0, i), RIGHT),
        traverse((len(grid[0]) - 1, i), LEFT),
    )

for i in range(len(grid[0])):
    highestEnergy = max(
        highestEnergy, traverse((i, 0), DOWN), traverse((i, len(grid) - 1), UP)
    )

print("Part 1:", traverse((0, 0), RIGHT))
print("Part 2:", highestEnergy)
