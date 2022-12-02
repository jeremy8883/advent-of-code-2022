opponent_play_map = {
    "A": 1, # Rock
    "B": 2, # Paper
    "C": 3, # Scissors
}

def get_score(opp, you):
    if you == opp :
        return you + 3
    elif (you % 3 + 1) == opp:
        return you + 0
    else:
        return you + 6

def get_score_by_target_play(opponent_play, you_play):
    # These values also happen to equal the scores.
    # The winning play is also always one score higher.
    you_play_map = {
        "X": 1,  # Rock
        "Y": 2,  # Paper
        "Z": 3,  # Scissors
    }

    opp = opponent_play_map[opponent_play]
    you = you_play_map[you_play]

    return get_score(opp, you)

def part_1(data):
    rounds = data.split("\n")
    scores = list(map(lambda r: get_score_by_target_play(r[0], r.split(" ")[1]), rounds))
    return sum(scores)

def get_score_by_desired_outcome(opponent_play, desired_outcome):
    opp = opponent_play_map[opponent_play]

    if desired_outcome == "X": # Lose
        you = (opp - 2) % 3 + 1
    elif desired_outcome == "Y": # Draw
        you = opp
    else: # Win
        you = opp % 3 + 1

    return get_score(opp, you)

def part_2(data):
    rounds = data.split("\n")
    scores = list(map(lambda r: get_score_by_desired_outcome(r[0], r.split(" ")[1]), rounds))
    return sum(scores)

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
    print(part_2(data))
