from enum import Enum

grid = open("testcase.in").read().splitlines()


def isOutOfBounds(coord: tuple[int, int]):
    row, col = coord
    return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])


UP, DOWN, RIGHT, LEFT = (0 - 1j), (0 + 1j), (1 + 0j), (-1 + 0j)
tileLookup = {
    ".": {RIGHT: [RIGHT], LEFT: [LEFT], DOWN: [DOWN], UP: [UP]},
    "/": {RIGHT: [UP], LEFT: [DOWN], DOWN: [LEFT], UP: [RIGHT]},
    "\\": {RIGHT: [DOWN], LEFT: [UP], DOWN: [RIGHT], UP: [LEFT]},
    "-": {RIGHT: [RIGHT], LEFT: [LEFT], UP: [RIGHT, LEFT], DOWN: [RIGHT, LEFT]},
    "|": {RIGHT: [UP, DOWN], LEFT: [UP, DOWN], UP: [UP], DOWN: [DOWN]},
}


def getNextBeamPos(coord: tuple[int, int], dir: str):
    row, col = coord
    if grid[row][col] in ".|-":
        if grid[row][col] == "|" and (dir == "RIGHT" or dir == "LEFT"):
            return [((row + 1, col), "DOWN"), ((row - 1, col), "UP")]
        if grid[row][col] == "-" and (dir == "UP" or dir == "DOWN"):
            return [((row, col - 1), "LEFT"), ((row, col + 1), "RIGHT")]
        else:
            if dir == "LEFT":
                return [((row, col - 1), "LEFT")]
            if dir == "RIGHT":
                return [((row, col + 1), "RIGHT")]
            if dir == "UP":
                return [((row - 1, col), "UP")]
            if dir == "DOWN":
                return [((row + 1, col), "DOWN")]
    if grid[row][col] == "/":
        if dir == "LEFT":
            return [((row + 1, col), "DOWN")]
        elif dir == "RIGHT":
            return [((row - 1, col), "UP")]
        elif dir == "UP":
            return [((row, col + 1), "RIGHT")]
        elif dir == "DOWN":
            return [((row, col - 1), "LEFT")]
    if grid[row][col] == "\\":
        if dir == "LEFT":
            return [((row - 1, col), "UP")]
        elif dir == "RIGHT":
            return [((row + 1, col), "DOWN")]
        elif dir == "UP":
            return [((row, col - 1), "LEFT")]
        elif dir == "DOWN":
            return [((row, col + 1), "RIGHT")]
    return []


def traverse(startPoint, startDir):
    visited: dict[tuple[int, int], set[str]] = {}
    beams = [(startPoint, startDir)]

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
        traverse((i, 0), "RIGHT"),
        traverse((i, len(grid[0]) - 1), "LEFT"),
    )

for i in range(len(grid[0])):
    highestEnergy = max(
        highestEnergy, traverse((0, i), "DOWN"), traverse((len(grid) - 1, i), "UP")
    )

print("Part 1:", traverse((0, 0), "RIGHT"))
print("Part 2:", highestEnergy)
