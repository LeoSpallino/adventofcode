strings = open("testcase.in").read().split(",")


def hashString(string):
    curr = 0
    for char in list(string):
        curr += ord(char)
        curr *= 17
        curr %= 256
    return curr


part1 = sum(map(hashString, strings))

print("Part 1:", part1)

boxes = [[set(), []] for _ in range(256)]

for string in strings:
    if "-" in string:
        label = string.split("-")[0]
        boxNum = hashString(label)
        lookup, contents = boxes[boxNum]
        if label not in lookup:
            continue
        for ind, lbl in enumerate(contents):
            if lbl.startswith(label):
                del contents[ind]
                lookup.remove(label)
        boxes[boxNum] = [lookup, contents]
    if "=" in string:
        label, num = string.split("=")
        boxNum = hashString(label)
        lookup, contents = boxes[boxNum]
        if label in lookup:
            for ind, lbl in enumerate(contents):
                if lbl.startswith(label):
                    contents[ind] = " ".join(string.split("="))
        else:
            lookup.add(label)
            contents.append(" ".join(string.split("=")))
        boxes[boxNum] = [lookup, contents]


totalPower = 0
for boxInd, box in enumerate(boxes):
    for slotInd, slot in enumerate(box[1]):
        totalPower += (boxInd + 1) * (slotInd + 1) * int(slot.split(" ")[1])

print("Part 2:", totalPower)
