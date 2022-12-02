def findTotalStrategyScore(strategies):

    # A Y => 8
    # B X => 1
    # C Z => 6

    roundsScore = [None] * len(strategies)

    WIN = 6
    DRAW = 3
    LOSS = 0

    scores = {
        'A': 1, 'B': 2, 'C': 3,
        'X': 1, 'Y': 2, 'Z': 3
    }

    equivalncies = {
        'A': 'X', 'B': 'Y', 'C': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C'
    }

    results = {
        # rock beats scissors
        'A': 'C', 'X': 'Z',
        # paper beats rock
        'B': 'A', 'Y': 'X',
        # scissor beats paper
        'C': 'B', 'Z': 'Y',
    }

    for i, strategy in enumerate(strategies):
        oponent, you = strategy.split(' ')
        # Loss
        if equivalncies[results[oponent]] == you:
            #print(i, "LOSS", oponent, you)
            roundsScore[i] = LOSS + scores[you]

        # Draw
        if scores[oponent] == scores[you]:
            #print(i, "DRAW", oponent, you)
            roundsScore[i] = DRAW + scores[you]

        # Win
        if equivalncies[results[you]] == oponent:
            #print(i, "WIN", oponent, you)
            roundsScore[i] = WIN + scores[you]

    return sum(roundsScore)


def findDiffStrategyScore(strategies):

    # A Y => 4
    # B X => 1
    # C Z => 7

    roundsScore = [None] * len(strategies)

    WIN = 6
    DRAW = 3
    LOSS = 0

    scores = {
        'A': 1, 'B': 2, 'C': 3,
        'X': 1, 'Y': 2, 'Z': 3
    }

    for i, strategy in enumerate(strategies):
        oponent, you = strategy.split(' ')
        # Loss
        if you == 'X':
            movePoints = (scores[oponent] - 1) % 3
            if movePoints == 0:
                movePoints = 3
            roundsScore[i] = LOSS + movePoints

        # Draw
        if you == 'Y':
            roundsScore[i] = DRAW + scores[oponent]

        # Win
        if you == 'Z':
            if oponent == 'C':
                movePoints = (scores[oponent] + 1) % 3
            else:
                movePoints = (scores[oponent] + 1)
            roundsScore[i] = WIN + movePoints

    return sum(roundsScore)


with open('input.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')


part1 = findTotalStrategyScore(lines)

print(part1)

part2 = findDiffStrategyScore(lines)

print(part2)
