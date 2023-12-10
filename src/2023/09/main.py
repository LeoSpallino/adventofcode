import re


def parseInput(data: list[str]) -> list[list[int]]:
    parsedData = []

    for line in data:
        nums = [int(num) for num in re.findall(r"(-?\d+)", line)]
        parsedData.append(nums)

    return parsedData


def decomposeNums(nums) -> list[list[int]]:
    decomp = [nums]
    decompPointer = 0

    allZero = False
    while allZero is False:
        allZero = True
        step = []
        for i in range(len(decomp[decompPointer]) - 1):
            diff = decomp[decompPointer][i + 1] - decomp[decompPointer][i]
            step.append(diff)
            if diff != 0:
                allZero = False
        decomp.append(step)
        decompPointer += 1

    return decomp


def predictLastNum(nums) -> int:
    decomp = decomposeNums(nums)
    decomp[len(decomp) - 1].append(0)

    for i in range(len(decomp) - 2, -1, -1):
        missing = decomp[i + 1][-1] + decomp[i][-1]
        decomp[i].append(missing)

    return decomp[0][-1]


def predictFirstNum(nums) -> int:
    decomp = decomposeNums(nums)
    decomp[len(decomp) - 1].insert(0, 0)

    for i in range(len(decomp) - 2, -1, -1):
        missing = decomp[i][0] - decomp[i + 1][0]
        decomp[i].insert(0, missing)

    return decomp[0][0]


def part1(data):
    histories = parseInput(data)
    total = 0

    for history in histories:
        total += predictLastNum(history)

    return total


def part2(data):
    histories = parseInput(data)
    total = 0

    for history in histories:
        total += predictFirstNum(history)

    return total


def solve(puzzleInput):
    solution1 = part1(puzzleInput)
    solution2 = part2(puzzleInput)

    return solution1, solution2


if __name__ == "__main__":
    file = open("testcase.in", "r")
    puzzleInput = [line.strip() for line in file.readlines()]
    solutions = solve(puzzleInput)
    print("\n".join(str(solution) for solution in solutions))
