import re
teststr = "5 blue Game 2: red; 10 blue 5 green; 5 red 14 green; 25 Game 34: red"
a = ["red", "green", "blue"]

print(max(map(lambda x: int(x), re.findall(r'Game ([0-9]+):', teststr))))

color_maxes = {"red": 12, "green": 13, "blue": 14}
print(color_maxes.keys())