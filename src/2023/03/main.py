import re


def getSymbolCoordNearNum(num: tuple, symbols) -> tuple:
    line, span = num
    start, stop = span

    if (line, stop) in symbols:
        return (line, stop)
    if (line, start - 1) in symbols:
        return (line, start - 1)
    for i in range(start - 1, stop + 1):
        if (line - 1, i) in symbols:
            return (line - 1, i)
        if (line + 1, i) in symbols:
            return (line + 1, i)

    return (-1, -1)


def part1(data: list[str]):
    total = 0
    symbols = set()
    nums = set()

    for ind, line in enumerate(data):
        matches = re.finditer(r"([^\.\d])", line)
        for match in matches:
            symbols.add((ind, match.start()))
        numsMatches = re.finditer(r"(\d{1,})", line)
        for num in numsMatches:
            nums.add((ind, (num.start(), num.end())))

    for num in nums:
        symbolCoord = getSymbolCoordNearNum(num, symbols)
        if symbolCoord != (-1, -1):
            total += int(data[num[0]][num[1][0] : num[1][1]])
    return total


def part2(data):
    totalGearRatio = 0
    symbols = set()
    nums = set()
    partsTouchingSymbolsLookup = {}

    for ind, line in enumerate(data):
        matches = re.finditer(r"([^\.\d])", line)
        for match in matches:
            symbols.add((ind, match.start()))
        numsMatches = re.finditer(r"(\d{1,})", line)
        for num in numsMatches:
            nums.add((ind, (num.start(), num.end())))

    for num in nums:
        symbolCoord = getSymbolCoordNearNum(num, symbols)
        if symbolCoord != (-1, -1):
            if symbolCoord not in partsTouchingSymbolsLookup:
                partsTouchingSymbolsLookup[symbolCoord] = []
            partsTouchingSymbolsLookup[symbolCoord].append(
                int(data[num[0]][num[1][0] : num[1][1]])
            )

    for gear in partsTouchingSymbolsLookup.keys():
        if len(partsTouchingSymbolsLookup[gear]) == 2:
            gearRatio = (
                partsTouchingSymbolsLookup[gear][0]
                * partsTouchingSymbolsLookup[gear][-1]
            )
            totalGearRatio += gearRatio
    return totalGearRatio


def solve(puzzleInput):
    solution1 = part1(puzzleInput)
    solution2 = part2(puzzleInput)

    return solution1, solution2


if __name__ == "__main__":
    file = open("testcase.in", "r")
    puzzleInput = [line.strip() for line in file.readlines()]
    solutions = solve(puzzleInput)
    print("\n".join(str(solution) for solution in solutions))
