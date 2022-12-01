from collections import defaultdict
def findMaxCalories(data):

    calorieMap = defaultdict(int)
    elf = 1
    for eachEntry in data:
        if eachEntry == '':
            elf += 1
            continue
        calorieMap[elf] += int(eachEntry)
    
    return max(calorieMap, key=calorieMap.get)

def findTop3MaxCalories(data):
    k = 3
    calorieMap = defaultdict(int)
    elf = 1
    for eachEntry in data:
        if eachEntry == '':
            elf += 1
            continue
        calorieMap[elf] += int(eachEntry)

    s = 0
    while k:
        keyToDelete = max(calorieMap, key=calorieMap.get)
        s += calorieMap[keyToDelete]
        del calorieMap[keyToDelete]
        k -= 1

    return s
        


with open('input.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# part 1
part1 = findMaxCalories(lines)

print(part1)

# part 2
part2 = findTop3MaxCalories(lines)

print(part2)