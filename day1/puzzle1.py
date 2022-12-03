from adventOfCode import getPuzzleDataFromDay


inputData = getPuzzleDataFromDay(1)
processedData = inputData.split("\n\n")
s = list(processedData[-1])
processedData[-1] = "".join(s[:-1])

highestCalories = 0

for elf in processedData:
    caloriesCarriedByOneElf = [ int(itemCalories) for itemCalories in elf.split("\n") ]
    currentCalories = sum(caloriesCarriedByOneElf)

    if currentCalories > highestCalories:
        highestCalories = currentCalories

print(highestCalories)