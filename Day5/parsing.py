from collections import defaultdict


def parseInput(instructions):

    # Parsing the input
    stackCount = 1
    stackPileMap = defaultdict(list)
    moveInstructionsIndex = 0
    firstBox = 1
    for i, eachInstruction in enumerate(instructions):
        # This line has boxes
        if '[' in eachInstruction:
            while firstBox < len(eachInstruction):
                stackPileMap[stackCount].append(eachInstruction[firstBox])
                firstBox += 4
                stackCount += 1
            stackCount = 1

        if eachInstruction == '':
            moveInstructionsIndex = i+1
            break

        firstBox = 1

    for key, value in stackPileMap.items():
        value = [i for i in value if i != ' ']
        stackPileMap[key] = value[::-1]

    moveInstructions = instructions[moveInstructionsIndex:]

    return moveInstructions, stackPileMap
