"""
Student A: Core Game Logic & AI
- Implement basic rock-paper-scissors rules
- Random AI (completely random choices)
- Pattern AI (looks for player patterns in last 3-5 moves)
- Counter AI (plays what would beat player's most common choice)
- Input validation for player choices
"""

import random
import copy

moveChoices = ["rock", "paper", "scissors"]


def _flattenMatchData(moveData: list[list[dict]]) -> list[dict]:
    """Flattens the match data to prepare it for analysis."""

    return [matchDict for tournament in moveData for matchDict in tournament]


def getRandomAiMove() -> str:
    """Chooses a random move."""
    return moveChoices[random.randint(0, 2)]


def _getCounterToMove(move: str) -> str:
    """Returns the rock-paper-scissors move that beats the given move."""
    if move == "rock":
        return "paper"
    if move == "paper":
        return "scissors"
    if move == "scissors":
        return "rock"
    raise ValueError(f"'{move}' is not a valid move.")


def _getTopMove(rockCount: int, paperCount: int, scissorsCount: int) -> str:
    """Gets the top move based on the provided counts. If there's a tie, randomly chooses from the tied top moves."""

    topMoves = []
    if rockCount >= paperCount and rockCount >= scissorsCount:
        topMoves.append("rock")
    if paperCount >= rockCount and paperCount >= scissorsCount:
        topMoves.append("paper")
    if scissorsCount >= rockCount and scissorsCount >= paperCount:
        topMoves.append("scissors")

    # this selects a random move from the top moves when there's a tie
    return topMoves[random.randint(0, len(topMoves) - 1)]


def getCounterAiMove(moveData: list[list[dict]]) -> str:
    """Chooses the move countering the player's most used move. If multiple moves are tied for being the most used, one of the tied moves will be randomly selected to be countered."""

    flattenedData = _flattenMatchData(moveData)

    rockCount = 0
    paperCount = 0
    scissorsCount = 0
    for round in flattenedData:
        if round["playerMove"] == "rock":
            rockCount += 1
        elif round["playerMove"] == "paper":
            paperCount += 1
        else:
            scissorsCount += 1

    moveToCounter = _getTopMove(rockCount, paperCount, scissorsCount)
    return _getCounterToMove(moveToCounter)


def getPatternAiMove(moveData: list[list[dict]], contextLength: int = 3) -> str:
    """Predicts the player's next move based on the player's previous moves, up to the context_length number of moves. If there's a tie, select randomly from the top predictions. If there's no data, selects a random move. If there's only one previous round, selects the move that beats the user's first move."""

    # flattens the series data into a 1D array of round dictionaries
    flattenedData = _flattenMatchData(moveData)
    if len(flattenedData) == 0:
        return getRandomAiMove()
    if len(flattenedData) == 1:
        return _getCounterToMove(flattenedData[0]["playerMove"])

    numDimensions = min(contextLength, len(flattenedData) - 1)

    # prepares an empty dictionary n dimensions deep
    moveCounts = {move: 0 for move in moveChoices}
    for _ in range(numDimensions):
        higherDimensionMoveCounts = {
            move: copy.deepcopy(moveCounts) for move in moveChoices
        }
        moveCounts = higherDimensionMoveCounts

    # tallies which move came after numDimensions previous move
    for i in range(len(flattenedData) - numDimensions):
        window = flattenedData[i : i + numDimensions + 1]
        moveOrder = []
        for moveDict in window:
            moveOrder.append(moveDict["playerMove"])
        selectedCombo = moveCounts
        for move in moveOrder[:-1]:
            nextLevel = selectedCombo[move]
            selectedCombo = nextLevel
        selectedCombo[moveOrder[-1]] += 1

    # gets the move tallies for moves that came after the player's past numDimensions moves
    moveOrderContext = []
    for moveDict in flattenedData[-numDimensions:]:
        moveOrderContext.append(moveDict["playerMove"])
    currentContextData = moveCounts
    for move in moveOrderContext:
        nextLevel = currentContextData[move]
        currentContextData = nextLevel

    # gets the counter to the player's most common next move (ties broken with random selection)
    moveToCounter = _getTopMove(
        currentContextData["rock"],
        currentContextData["paper"],
        currentContextData["scissors"],
    )
    return _getCounterToMove(moveToCounter)


if __name__ == "__main__":
    testData = [
        [
            {"playerMove": "rock", "aiMove": "paper", "winner": "ai"},
            {"playerMove": "scissors", "aiMove": "paper", "winner": "player"},
            {"playerMove": "paper", "aiMove": "scissors", "winner": "none"},
        ],
        [
            {"playerMove": "rock", "aiMove": "rock", "winner": "ai"},
            {"playerMove": "scissors", "aiMove": "paper", "winner": "player"},
            {"playerMove": "paper", "aiMove": "scissors", "winner": "player"},
        ],
    ]

    print("Random AI Move:", getRandomAiMove())
    print("Counter AI Move:", getCounterAiMove(testData))
    print("Pattern AI Move:", getPatternAiMove(testData))
