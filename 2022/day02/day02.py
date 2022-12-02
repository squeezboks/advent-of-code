sol1_dict = {
    'A X': ['opp: rock, you: rock, result: draw', 1, 3], 'A Y': ['opp: rock, you: papr, result: win!', 2, 6], 'A Z': ['opp: rock, you: scsr, result: lose', 3, 0],
    'B X': ['opp: papr, you: rock, result: lose', 1, 0], 'B Y': ['opp: papr, you: papr, result: draw', 2, 3], 'B Z': ['opp: papr, you: scsr, result: win!', 3, 6],
    'C X': ['opp: scsr, you: rock, result: win!', 1, 6], 'C Y': ['opp: scsr, you: papr, result: lose', 2, 0], 'C Z': ['opp: scsr, you: scsr, result: draw', 3, 3]
}

sol2_dict = {
    'A X': ['opp: rock, you: scsr, result: lose', 3, 0], 'A Y': ['opp: rock, you: rock, result: draw', 1, 3], 'A Z': ['opp: rock, you: papr, result: win!', 2, 6],
    'B X': ['opp: papr, you: rock, result: lose', 1, 0], 'B Y': ['opp: papr, you: papr, result: draw', 2, 3], 'B Z': ['opp: papr, you: scsr, result: win!', 3, 6],
    'C X': ['opp: scsr, you: papr, result: lose', 2, 0], 'C Y': ['opp: scsr, you: scsr, result: draw', 3, 3], 'C Z': ['opp: scsr, you: rock, result: win!', 1, 6]
}

with open("day02_data.txt") as f:
    lines = f.readlines()
    games_sol1 = []
    games_sol2 = []
    for line in lines:
        line = line.strip()
        games_sol1.append(sol1_dict[line][1]+sol1_dict[line][2])
        games_sol2.append(sol2_dict[line][1]+sol2_dict[line][2])
        
print(f"Score using misinterpreted strategy guide: {sum(games_sol1)}")
print(f"Score using correctly interpreted strategy guide: {sum(games_sol2)}")