from adventOfCode import getPuzzleDataFromDay


def win(opponentPlay, pointsByElement):
    elementToWinAgainst = {
        "A": "paper",
        "B": "scissors",
        "C": "rock"
    }

    return 6 + pointsByElement[elementToWinAgainst[opponentPlay]]


def draw(opponentPlay, pointsByElement):
    elementToDrawAgainst = {
        "A": "rock",
        "B": "paper",
        "C": "scissors"
    }

    return 3 + pointsByElement[elementToDrawAgainst[opponentPlay]]


def lose(opponentPlay, pointsByElement):
    elementToLoseAgainst = {
        "A": "scissors",
        "B": "rock",
        "C": "paper"
    }

    return pointsByElement[elementToLoseAgainst[opponentPlay]]


inputData = getPuzzleDataFromDay(2)
processedData = inputData.split("\n")[:-1]

pointsByElement = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

score = 0

for round in processedData:
    opponentPlay = round[0]
    result = round[2]

    # I lose
    if result == "X":
        score += lose(opponentPlay, pointsByElement)

    # I draw
    if result == "Y":
        score += draw(opponentPlay, pointsByElement)

    # I win
    if result == "Z":
        score += win(opponentPlay, pointsByElement)

print(score)