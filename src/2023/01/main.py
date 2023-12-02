def stringToDigits(line):
    leftDigit = ""
    rightDigit = ""
    reversedLine = line[::-1]

    for i in range(len(line)):
        if leftDigit == "" and ord(line[i]) in range(ord("0"), ord("9") + 1):
            leftDigit = line[i]

        if rightDigit == "" and ord(reversedLine[i]) in range(ord("0"), ord("9") + 1):
            rightDigit = reversedLine[i]

        if leftDigit != "" and rightDigit != "":
            break

    return int(leftDigit + rightDigit)


def wordAndNumsToDigits(line):
    wordLookup = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    reversedLine = line[::-1]
    leftDigit = ""
    rightDigit = ""
    leftPointer = 0
    rightPointer = 0

    while leftDigit == "" or rightDigit == "" or leftPointer < len(line):
        if leftDigit == "" and ord(line[leftPointer]) in range(ord("0"), ord("9") + 1):
            leftDigit = line[leftPointer]
        if rightDigit == "" and ord(reversedLine[leftPointer]) in range(
            ord("0"), ord("9") + 1
        ):
            rightDigit = reversedLine[leftPointer]

        while (
            leftDigit == ""
            and rightPointer < len(line)
            and rightPointer < leftPointer + 6
        ):
            if line[leftPointer:rightPointer] in wordLookup:
                leftDigit = wordLookup[line[leftPointer:rightPointer]]
                break
            rightPointer += 1

        rightPointer = leftPointer

        while (
            rightDigit == ""
            and rightPointer < len(reversedLine)
            and rightPointer < leftPointer + 6
        ):
            if reversedLine[leftPointer:rightPointer][::-1] in wordLookup:
                rightDigit = wordLookup[reversedLine[leftPointer:rightPointer][::-1]]
                break
            rightPointer += 1

        leftPointer += 1
        rightPointer = leftPointer

    return int(leftDigit + rightDigit)


def part1(data):
    total = 0
    for line in data:
        total += stringToDigits(line)

    return total


def part2(data):
    total = 0
    for line in data:
        total += wordAndNumsToDigits(line)
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
