import re

file = open('games_teste.log', 'r')

lines = file.readlines()

for line in lines:
    re.search("/ClientUserinfoChanged: \d n\\(.*?)\\/", line)
    