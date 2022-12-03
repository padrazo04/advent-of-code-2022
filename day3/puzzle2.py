from adventOfCode import getPuzzleDataFromDay

inputData = getPuzzleDataFromDay(3)
elvesRucksacks = inputData.split("\n")[:-1]

priority = { "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
             "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, 
             "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26 }

sumOfPriorities = 0

for i in range(0, len(elvesRucksacks), 3):
    firstElfItems = elvesRucksacks[i]
    secondElfItems = elvesRucksacks[i+1]
    thirdElfItems = elvesRucksacks[i+2]

    for item in firstElfItems:
        if item in secondElfItems and item in thirdElfItems:
            sumOfPriorities += priority[item.lower()]
            sumOfPriorities += 26 if item.isupper() else 0
            break

print(sumOfPriorities)