from adventOfCode import getPuzzleDataFromDay


inputData = getPuzzleDataFromDay(4)
listOfSectionAssigments = inputData.split("\n")[:-1]

occurrencies = 0

for pair in listOfSectionAssigments:
    firstElfSectionsLimits = [ int(element) for element in pair.split(",")[0].split("-") ]
    secondElfSectionsLimits = [ int(element) for element in pair.split(",")[1].split("-") ]

    firstElfSections = range(firstElfSectionsLimits[0], firstElfSectionsLimits[1]+1)
    secondElfSections = range(secondElfSectionsLimits[0], secondElfSectionsLimits[1]+1)

    for sectionOfFirstElf in firstElfSections:
        if sectionOfFirstElf in secondElfSections:
            occurrencies += 1
            break

print(occurrencies)