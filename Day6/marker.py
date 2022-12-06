def getStartingMarker(signal, uniqueCharMarker):
    unique = set()
    for i in range(len(signal)-uniqueCharMarker-1):
        for j in range(uniqueCharMarker):
            unique.add(signal[i+j])
        if len(unique)==uniqueCharMarker:
            return i+uniqueCharMarker

        unique = set()

with open('input.txt') as f:
    lines = f.readlines()


for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

lines =  lines[0]

testcases = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
]

part1 = getStartingMarker(lines, 4)

print(part1)

part2 = getStartingMarker(lines, 14)

print(part2)
