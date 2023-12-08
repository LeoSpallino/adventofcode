import re
import math


def parseInput(data: list[str]) -> tuple[str, dict[str, list[str]]]:
    moves = data[0]
    graph = {}

    for line in data[2:]:
        node, left, right = re.findall(r"([A-Z]{3})", line)
        graph[node] = [left, right]

    return (moves, graph)


def traverseGraph(startNode, endNodes: set[str], graph, moves) -> int:
    movePointer = 0
    steps = 0
    LEFT, RIGHT = 0, 1
    currentNode = startNode

    while currentNode not in endNodes:
        if movePointer == len(moves):
            movePointer = 0
        if moves[movePointer] == "L":
            currentNode = graph[currentNode][LEFT]
        if moves[movePointer] == "R":
            currentNode = graph[currentNode][RIGHT]
        movePointer += 1
        steps += 1

    return steps


def part1(data):
    moves, graph = parseInput(data)
    startNode = "AAA"
    endNode = set()
    endNode.add("ZZZ")
    steps = traverseGraph(startNode, endNode, graph, moves)

    return steps


def part2(data):
    moves, graph = parseInput(data)
    nodes = []
    endNodes = set()
    minSteps = []

    for node in graph:
        if node[-1] == "A":
            nodes.append(node)
        if node[-1] == "Z":
            endNodes.add(node)

    for node in nodes:
        minSteps.append(traverseGraph(node, endNodes, graph, moves))

    return math.lcm(*minSteps)


def solve(puzzleInput):
    solution1 = part1(puzzleInput)
    solution2 = part2(puzzleInput)

    return solution1, solution2


if __name__ == "__main__":
    file = open("testcase.in", "r")
    puzzleInput = [line.strip() for line in file.readlines()]
    solutions = solve(puzzleInput)
    print("\n".join(str(solution) for solution in solutions))
