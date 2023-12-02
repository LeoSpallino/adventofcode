class Round:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def setColor(self, color, num):
        match color:
            case "red":
                self.red = num
            case "green":
                self.green = num
            case "blue":
                self.blue = num
            case _:
                pass


class Game:
    def __init__(self, id: int):
        self.id = id
        self.rounds: list[Round] = []


def parseInput(data: list[str]):
    games: list[Game] = []

    for line in data:
        meta, rounds = line.split(": ")
        game = Game(int(meta.split()[1]))
        rounds = rounds.split("; ")
        for r in rounds:
            round = Round()
            colors = r.split(", ")
            for c in colors:
                num, color = c.split()
                round.setColor(color, int(num))
            game.rounds.append(round)

        games.append(game)

    return games


def part1(data):
    redLimit = 12
    greenLimit = 13
    blueLimit = 14
    games = parseInput(data)
    validGamesTotal = 0

    for game in games:
        isValid = True
        roundPointer = 0
        while isValid and roundPointer < len(game.rounds):
            if (
                game.rounds[roundPointer].red > redLimit
                or game.rounds[roundPointer].green > greenLimit
                or game.rounds[roundPointer].blue > blueLimit
            ):
                isValid = False
                break
            roundPointer += 1
        if isValid:
            validGamesTotal += game.id

    return validGamesTotal


def part2(data):
    games = parseInput(data)
    powerTotal = 0

    for game in games:
        minRed = 0
        minGreen = 0
        minBlue = 0

        for round in game.rounds:
            if round.red > minRed:
                minRed = round.red
            if round.green > minGreen:
                minGreen = round.green
            if round.blue > minBlue:
                minBlue = round.blue

        powerTotal += minRed * minGreen * minBlue

    return powerTotal


def solve(puzzleInput):
    solution1 = part1(puzzleInput)
    solution2 = part2(puzzleInput)

    return solution1, solution2


if __name__ == "__main__":
    file = open("testcase.in", "r")
    puzzleInput = [line.strip() for line in file.readlines()]
    solutions = solve(puzzleInput)
    print("\n".join(str(solution) for solution in solutions))
