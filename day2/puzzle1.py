from adventOfCode import getPuzzleDataFromDay


inputData = getPuzzleDataFromDay(2)
processedData = inputData.split("\n")[:-1]

rock = {
    "pointsForUsing": 1,
    "against": {"A": 3, "B": 0, "C": 6}
}

paper = {
    "pointsForUsing": 2,
    "against": {"A": 6, "B": 3, "C": 0}
}

scissors = {
    "pointsForUsing": 3,
    "against": {"A": 0, "B": 6, "C": 3}
}

elements = {
    "X": rock,
    "Y": paper,
    "Z": scissors
}

score = 0

for round in processedData:
    opponentPlay = round[0]
    myPlay = round[2]

    score += elements[myPlay]["pointsForUsing"]
    score += elements[myPlay]["against"][opponentPlay]

print(score)