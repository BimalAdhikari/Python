#1 open the file 
#2 split in rijen 
#stap 3 haal data uit de r0i
#bereken totaal en presenteer 
with open('uitslagen.txt', 'r') as file:
    goal_total= 0
    for game in file:
        splitted = game.split(',')
match_goals = splitted[2], splitted[3]
goal_total += match_goals
print(f"Totaal aantal goals: {goal_total}")