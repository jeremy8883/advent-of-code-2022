opponent_play_map = {
    "A": 1, # Rock
    "B": 2, # Paper
    "C": 3, # Scissors
}

# These values also happen to equal the scores.
# The winning play is also always one score higher.
you_play_map = {
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3, # Scissors
}

def get_score(opponent_play, you_play):
    opp = opponent_play_map[opponent_play]
    you = you_play_map[you_play]

    if you == opp :
        return you + 3
    elif (you % 3 + 1) == opp:
        return you + 0
    else:
        return you + 6


def part_1(data):
    rounds = data.split("\n")
    scores = list(map(lambda r: get_score(r[0], r.split(" ")[1]), rounds))
    return sum(scores)

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
