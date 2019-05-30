import re
import json

# file = open(input('Digite o arquivo de entrada: '), 'r')
file = open('games_teste.log', 'r')

lines = file.readlines()

games = []

def newGame():
    games.append({
            'total_kills': 0,
            'players': [],
            'kills': {}
        })

def substring(string, init, end):
    return string[init:end]

gamesCount = -1
for line in lines:
    if "InitGame:" in line: 
        newGame()
        gamesCount = gamesCount + 1
    
    if "ClientUserinfoChanged:" in line: 
        player = substring(line, line.find('n\\')+2, line.find('\\t'))
        if player not in games[gamesCount]['players']:
            games[gamesCount]['players'].append(player)
            games[gamesCount]['kills'][player] = 0

    if "<world> killed" in line:
        player = substring(line, line.find('<world> killed')+15, line.find(' by'))
        games[gamesCount]['kills'][player] -= 1
        games[gamesCount]['total_kills'] += 1
        print(games[gamesCount])

    