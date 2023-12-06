import math
import re


def parseInput(data: list[str]):
    parsed = []
    for line in data:
        match = re.findall(r"(\d+)", line.split(":")[1].strip())
        parsed.append(match)
    return parsed


def part1(data):
    parsed = parseInput(data)
    times, distances = [int(time) for time in parsed[0]], [
        int(distance) for distance in parsed[1]
    ]
    marginOfError = 1

    for i in range(len(times)):
        winCount = 0
        time = times[i]
        targetDistance = distances[i]
        for j in range(time + 1):
            distance = j * (time - j)
            if distance > targetDistance:
                winCount += 1

        marginOfError *= winCount

    return marginOfError


def part2(data):
    parsed = parseInput(data)
    time, distance = int("".join(parsed[0])), int("".join(parsed[1]))

    leftBound = math.ceil(
        (-time + math.sqrt(time**2 + (-4) * (-1) * (-distance))) / 2 * -1
    )
    rightBound = math.ceil(
        (-time - math.sqrt(time**2 + (-4) * (-1) * (-distance))) / 2 * -1
    )

    return rightBound - leftBound


def solve(puzzleInput):
    solution1 = part1(puzzleInput)
    solution2 = part2(puzzleInput)

    return solution1, solution2


if __name__ == "__main__":
    file = open("testcase.in", "r")
    puzzleInput = [line.strip() for line in file.readlines()]
    solutions = solve(puzzleInput)
    print("\n".join(str(solution) for solution in solutions))
