import re
import json

file = open('games_teste.log', 'r')

lines = file.readlines()

games = []
kills_by_means = []

def newGame():
    games.append({
            'total_kills': 0,
            'players': [],
            'kills': {},
        })

def substring(string, init, end):
    return string[init:end]

gamesCount = -1
for line in lines:
    if "InitGame:" in line: 
        newGame()
        gamesCount = gamesCount + 1
        kills_by_means.append({})
    
    if "ClientUserinfoChanged:" in line: 
        player = substring(line, line.find('n\\')+2, line.find('\\t'))
        if player not in games[gamesCount]['players']:
            games[gamesCount]['players'].append(player)
            games[gamesCount]['kills'][player] = 0

    if "<world> killed" in line:
        player = substring(line, line.find('<world> killed')+15, line.find(' by'))
        games[gamesCount]['kills'][player] -= 1
        games[gamesCount]['total_kills'] += 1

    if 'killed' in line and '<world> killed' not in line:
        killer = substring(line, re.search('\d:\s', line).span()[1], line.find(' killed'))
        games[gamesCount]['kills'][killer] += 1
        games[gamesCount]['total_kills'] += 1
    
    if 'by' in line:
        mean_of_death = substring(line, re.search('by ', line).span()[1], len(line)-1)
        if mean_of_death in kills_by_means[gamesCount]:
            kills_by_means[gamesCount][mean_of_death] += 1
        else:
            kills_by_means[gamesCount][mean_of_death] = 1



# -------------- Task 1 --------------
print('TASK 1')
for i in range(0, len(games)):
    print('game_' + str(i+1) +':', json.dumps(games[i], indent=4))

# -------------- Task 2 --------------
ranking = {}
print('\nTASK 2')
for i in range(0, len(games[i]['kills'])-1):
    for key, value in games[i]['kills'].items():
        if key in ranking:
            ranking[key] += value
        else:
            ranking[key] = value

print('RANKING:')
for key, value in ranking.items():
    print('PLAYER ' + str(key) + ' ' + str(value) + ' KILLS')

for i in range(0, len(games[i]['kills'])-1):
    print('\n Game ' + str(i+1))
    for key, value in games[i]['kills'].items():
        print('PLAYER ' + str(key) + ' ' + str(value) + ' KILLS')


# -------------- Task 3 --------------
print('\nCAUSAS DE MORTE:')
for i in range(0, len(kills_by_means)):
    print('game_' + str(i) + ': ', json.dumps(kills_by_means[i], indent=4) + '\n')
