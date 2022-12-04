from adventOfCode import getPuzzleDataFromDay


inputData = getPuzzleDataFromDay(4)
listOfSectionAssigments = inputData.split("\n")[:-1]

occurrencies = 0

for pair in listOfSectionAssigments:
    firstElfSections = [ int(element) for element in pair.split(",")[0].split("-") ]
    secondElfSections = [ int(element) for element in pair.split(",")[1].split("-") ]

    if secondElfSections[0] >= firstElfSections[0] and secondElfSections[1] <= firstElfSections[1]:
        occurrencies += 1
    elif firstElfSections[0] >= secondElfSections[0] and firstElfSections[1] <= secondElfSections[1]:
        occurrencies += 1

print(occurrencies)