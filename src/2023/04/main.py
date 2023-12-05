from collections import deque
import re


class Card:
    def __init__(self, id):
        self.id: int = id
        self.winningNums = set()
        self.nums: list[int] = []

    def addWinningNum(self, num: int):
        self.winningNums.add(num)

    def addNum(self, num: int):
        self.nums.append(num)


def parseInput(data: list[str]) -> list[Card]:
    cards = []

    for line in data:
        match = re.findall(r"^Card\s+(\d+):\s+([\d\s]+)\s*\|\s*([\d\s]+)$", line)
        card = Card(int(match[0][0]))
        for winningNum in re.findall(r"(\d+)", match[0][1]):
            card.addWinningNum(int(winningNum))
        for num in re.findall(r"(\d+)", match[0][2]):
            card.addNum(int(num))

        cards.append(card)

    return cards


def processCard(card: Card) -> int:
    wins = 0

    for num in card.nums:
        if num in card.winningNums:
            wins += 1

    return wins


def part1(data: list[str]):
    totalPoints = 0
    cards = parseInput(data)

    for card in cards:
        wins = processCard(card)
        if wins > 0:
            totalPoints += 2 ** (wins - 1)

    return totalPoints


def part2(data: list[str]):
    cards = parseInput(data)
    cardsProcessed = 0
    processingQueue = deque(range(len(cards)))

    while len(processingQueue) > 0:
        cardNum = processingQueue.popleft()
        card = cards[cardNum]
        wins = processCard(card)
        if wins > 0:
            processingQueue.extend([i for i in range(cardNum + 1, cardNum + 1 + wins)])
        cardsProcessed += 1

    return cardsProcessed


def solve(puzzleInput):
    solution1 = part1(puzzleInput)
    solution2 = part2(puzzleInput)

    return solution1, solution2


if __name__ == "__main__":
    file = open("testcase.in", "r")
    puzzleInput = [line.strip() for line in file.readlines()]
    solutions = solve(puzzleInput)
    print("\n".join(str(solution) for solution in solutions))
