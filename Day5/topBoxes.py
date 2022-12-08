from parsing import parseInput


def getTopStacks(instructions, crateMoverType):

    moveInstructions, stackPileMap = parseInput(instructions)

    for instruction in moveInstructions:

        instruction = instruction.split(' ')
        boxesToMove, fromStack, toStack = int(instruction[1]), int(
            instruction[3]), int(instruction[5])

        boxesToMove = getBoxesToBeMoved(stackPileMap, fromStack, boxesToMove)
        addBoxesToStack(stackPileMap, toStack, boxesToMove, crateMoverType)

    return getTopElements(stackPileMap)


def getBoxesToBeMoved(stackPileMap, fromStack, k):
    popped = []
    while k:
        box = stackPileMap[fromStack].pop()
        popped.append(box)
        k -= 1

    return popped


def addBoxesToStack(stackPileMap, toStack, toAdd, crateMoverType):
    if crateMoverType == 'CrateMover 9000':
        stackPileMap[toStack].extend(toAdd)
    if crateMoverType == 'CrateMover 90001':
        stackPileMap[toStack].extend(toAdd[::-1])


def getTopElements(stackPileMap):

    topBoxesString = ''

    for key, value in stackPileMap.items():
        topBoxesString += value[-1]

    return topBoxesString


with open('input.txt') as f:
    lines = f.readlines()


for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

part1 = getTopStacks(lines, 'CrateMover 9000')
print(part1)

part2 = getTopStacks(lines, 'CrateMover 90001')
print(part2)
