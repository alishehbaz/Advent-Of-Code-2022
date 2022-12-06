def overlappingShifts(shifts):

    count = 0
    for i in range(len(shifts)):
        s1, s2 = shifts[i].split(',')
        startShift1, endShift1 = int(s1.split('-')[0]), int(s1.split('-')[1])
        startShift2, endShift2 = int(s2.split('-')[0]), int(s2.split('-')[1])

        # s1 contains s2

        if startShift2 >= startShift1 and endShift2 <= endShift1:
            print(i+1, "S1 contains S2", (startShift1,
                  endShift1), (startShift2, endShift2))
            count += 1

        # s2 contains s1

        elif startShift1 >= startShift2 and endShift1 <= endShift2:
            print(i+1, "S2 contains S1", (startShift1,
                  endShift1), (startShift2, endShift2))
            count += 1

        else:
            print(i+1, "NO OVERLAP", (startShift1, endShift1),
                  (startShift2, endShift2))

    return count


def noOverlap(shifts):

    notOverlapping = 0
    for i in range(len(shifts)):
        s1, s2 = shifts[i].split(',')
        startShift1, endShift1 = int(s1.split('-')[0]), int(s1.split('-')[1])
        startShift2, endShift2 = int(s2.split('-')[0]), int(s2.split('-')[1])

        if startShift2 > endShift1 or startShift1 > endShift2:
            print(i+1, "NO OVERLAP", (startShift1, endShift1),
                  (startShift2, endShift2))

            notOverlapping += 1

    return len(shifts) - notOverlapping


with open('input.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')


part1 = overlappingShifts(lines)

print(part1)


part2 = noOverlap(lines)

print(part2)
