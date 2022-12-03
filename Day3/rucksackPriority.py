def sumOfPriorities(rucksackData):

    eachRucksackData = [None] * len(rucksackData)

    alphabets = {chr(i+97): i+1 for i in range(26)}

    for i, entry in enumerate(rucksackData):
        p1, p2 = entry[:len(entry)//2],  entry[len(entry)//2:]
        commonLetter = ''.join(set(p1).intersection(p2))
        if commonLetter.islower():
            score = alphabets[commonLetter]
        else:
            commonLetter = commonLetter.lower()
            score = alphabets[commonLetter] + 26
        eachRucksackData[i] = score

    return sum(eachRucksackData)


def priorityWindow(rucksackData):

    eachRucksackData = [None] * (len(rucksackData)//3)

    alphabets = {chr(i+97): i+1 for i in range(26)}

    for i, j in enumerate(range(0, len(rucksackData)-2, 3)):
        e1, e2, e3 = set(rucksackData[j]), set(
            rucksackData[j+1]), set(rucksackData[j+2])
        commonLetter = ''.join(set.intersection(e1, e2, e3))
        if commonLetter.islower():
            score = alphabets[commonLetter]
        else:
            commonLetter = commonLetter.lower()
            score = alphabets[commonLetter] + 26
        eachRucksackData[i] = score

    return sum(eachRucksackData)


with open('input.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

part1 = sumOfPriorities(lines)

print(part1)

part2 = priorityWindow(lines)

print(part2)
