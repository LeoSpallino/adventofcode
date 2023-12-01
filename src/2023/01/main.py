def stringToDigits(line):
    digits = []
    for i in line:
        if ord(i) in range(ord("0"), ord("9") + 1):
            digits.append(i)

    return digits


def wordToDigits(line):
    wordLookup = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    for i in range(len(line) - 4):
        for key in wordLookup:
            if key in line[i : i + 5]:
                line = line.replace(key, wordLookup[key], 1)

    return line


def part1(data):
    total = 0
    for line in data:
        digits = stringToDigits(line)
        parsedNum = digits[0] + digits[-1]
        total += int(parsedNum)

    return total


def part2(data):
    total = 0
    for line in data:
        parsedWords = wordToDigits(line)
        digits = stringToDigits(parsedWords)
        parsedNum = digits[0] + digits[-1]
        total += int(parsedNum)
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
