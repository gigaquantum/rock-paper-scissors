"""
Student C: Statistics & Analysis
- Track win/loss/tie for each throw type
- Calculate win percentage
- Track current streak (wins/losses)
- Longest win streak
- Most common player choice
- Most common AI choice
- Head-to-head results by throw type
"""

gameData = [
    [
        {"playerMove": "rock", "aiMove": "paper", "winner": "ai"},
        {"playerMove": "scissors", "aiMove": "paper", "winner": "player"},
        {"playerMove": "scissors", "aiMove": "scissors", "winner": "none"},
    ],
    [
        {"playerMove": "scissors", "aiMove": "rock", "winner": "ai"},
        {"playerMove": "scissors", "aiMove": "paper", "winner": "player"},
        {"playerMove": "rock", "aiMove": "scissors", "winner": "player"},
    ],
]


def _trackWinLossTie(data): #the underscore before the name denotes that this is a private function, and is to be used internally. The only function I will be calling into my Main program will be statisticsReport. 
    """Tracks the result of each match/throw for the player."""

    allResults = {
        "rock": {"win": 0, "loss": 0, "tie": 0},
        "paper": {"win": 0, "loss": 0, "tie": 0},
        "scissors": {"win": 0, "loss": 0, "tie": 0},
    }
    for tournament in data:
        for match in tournament:
            choice = match["playerMove"]
            winner = match["winner"]

            if winner == "none":
                winner = "tie"

            if winner == "player":
                allResults[choice]["win"] += 1
            elif winner == "ai":
                allResults[choice]["loss"] += 1
            elif winner == "tie":
                allResults[choice]["tie"] += 1

    print("WINS, LOSS AND TIE BY THROW TYPE")
    for choice in allResults.keys():
        print(
            f"{'-' * 40}\n{choice.upper()}\n{'-' * 40}\nWins: {allResults[choice]['win']}\nLosses: {allResults[choice]['loss']}\nTies: {allResults[choice]['tie']}"
        )


def _collectMatchResult(data):
    """This makes a list of the wins, loss, ties per tournament. This can then be used in other functions."""
    matchResult = []
    for tournament in data:  # collect my match results in order of being played
        for match in tournament:
            if match["winner"] == "player":
                matchResult.append("win")
            elif match["winner"] == "ai":
                matchResult.append("loss")
    return matchResult


def _allWinLossTie(data):
    """Tracks the wins, losses and ties across all tournaments."""
    win = 0
    loss = 0
    tie = 0
    for tournament in data:
        for match in tournament:
            if match["winner"] == "player":
                win += 1
            elif match["winner"] == "ai":
                loss += 1
            elif match["winner"] == "none":
                tie += 1
    return win, loss, tie


# calculate win percentage
def _winPercentage(data):
    """Tracks the percentage of wins for the user across all tournaments."""
    win, loss, tie = _allWinLossTie(data)
    totalMatch = win + loss + tie
    if totalMatch == 0:  # no division by 0
        print(f"Not enough matches have been played")
    else:
        formula = (win / totalMatch) * 100
    print(f"The players' win percentage is: {formula:.2f}%")


def currentStreak(data):
    """If the last 2 matches have been wins then user is on a winning streak, if last 2 matches have been losses, user is on a losing streak."""
    matchResult = _collectMatchResult(data)  # this calls my function above that stores all my match results

    lastPlay = matchResult[-1:]  # compares only the last 2 results from the tournament
    streakCount = 1

    secondToLast = len(matchResult)-2 #am going to iterate backwards so this shows that i am starting from the second to last match
    while secondToLast >= 0 and matchResult[secondToLast] == lastPlay:
        streakCount += 1
        secondToLast -= 1 
    
    if lastPlay == "win":
        streakLabel = "winning streak"
    elif lastPlay == "loss":
        streakLabel = "losing streak"
    else:
        streakLabel = "tie streak"
    
    if streakCount >= 2:
        print(f"You are currentlu in a {streakLabel} of length: {streakCount}")
   

def _longestWinStreak(data):
    """Takes a look at each tournament and determines what the longest streak in that tournament was."""
    matchResult = _collectMatchResult(data)

    longestStreak = 1
    currentStreakCount = 1
    longestStreakType = matchResult[0] #this makes it so I start with the first match result

    for r in range(1,len(matchResult)): #I start looping through the results from the second match onward
        if matchResult[r] == matchResult[r - 1]:
            currentStreakCount += 1
        else:
            currentStreakCount = 1 #resets my streak count bc it was broken
        
        if currentStreakCount > longestStreak:
            longestStreak = currentStreakCount
            longestStreakType = matchResult[r]
    
    if longestStreakType == "win":
        streakLabel = "winning streak"
    elif longestStreakType == "loss":
        streakLabel = "losing streak"
    else:
        streakLabel = "tie streak"

    print(f"The longest streak for the player is: {longestStreak} and it was a {streakLabel}.")


def _trackPlayerChoice(data):
    """Tracks the player's choice throughout the tournament, returns the most common choice."""
#    playerRock = 0
#    playerScissors = 0
#    playerPaper = 0

#    for tournament in data:
#        for match in tournament:
#            if match["playerMove"] == "rock":
#                playerRock += 1
#            elif match["playerMove"] == "scissors":
#                playerScissors += 1
#            elif match["playerMove"] == "paper":
#                playerPaper += 1
#
#    mostCommonPlayerChoice = ""
#    if playerRock < playerScissors > playerPaper:
#        mostCommonPlayerChoice = "scissors"
#    elif playerScissors < playerRock > playerPaper:
#        mostCommonPlayerChoice = "rock"
#    else:
#        mostCommonPlayerChoice = "paper"

    playerCounts = {"rock": 0, "paper": 0, "scissors": 0}

    for tournament in data:
        for match in tournament:
            choice = match["playerMove"]
            if choice in playerCounts:
                playerCounts[choice] += 1
        
    max_count = max(playerCounts.values())
    mostCommonPlayerChoice = [choice for choice, count in playerCounts.items()if count == max_count]
    if len(mostCommonPlayerChoice) == 1:
        print(f"Most common player choice: {mostCommonPlayerChoice[0]}")
    else:
        print(f"There was a tie between most common moves: {mostCommonPlayerChoice[0]}, {mostCommonPlayerChoice[1]}")


def _trackAiChoice(data):
    """Tracks AI's choice throughout the tournament, returns its most common choice."""

    aiCounts = {"rock": 0, "paper": 0, "scissors": 0}

    for tournament in data:
        for match in tournament:
            choice = match["playerMove"]
            if choice in aiCounts:
                aiCounts[choice] += 1
        
    max_count = max(aiCounts.values())
    mostCommonAiChoice = [choice for choice, count in aiCounts.items()if count == max_count]
    if len(mostCommonAiChoice) == 1:
        print(f"Most common player choice: {mostCommonAiChoice[0]}")
    else:
        print(f"There was a tie between most common moves: {mostCommonAiChoice[0]}, {mostCommonAiChoice[1]}")


def _headToHead(data): 
    allResults = {
        "rock": {"total": 0, "playerWin": 0, "aiWin": 0, "tie": 0},
        "paper": {"total": 0, "playerWin": 0, "aiWin": 0, "tie": 0},
        "scissors": {"total": 0, "playerWin": 0, "aiWin": 0, "tie": 0},
    }
    for tournament in data:
        for match in tournament:
            matchWinner = match["winner"]

            if matchWinner == "none":
                matchWinner = "tie" 

            for choice in allResults.keys():
                if (choice in (match["playerMove"], match["aiMove"])):  # what were the moves played during this match (player's,ai) and the choice checks if the rock, paper, or scissors matches one of them
                    allResults[choice]["total"] += 1

                    if matchWinner == "player" and match["playerMove"] == choice:
                        allResults[choice]["playerWin"] += 1
                    elif matchWinner == "ai" and match["aiMove"] == choice:
                        allResults[choice]["aiWin"] += 1
                    elif matchWinner in ["tie" , "none"]:  #####tried to fix tie counter here 
                        allResults[choice]["tie"] += 1

    print("HEAD-TO-HEAD STATS BY THROW TYPE")
    for choice in allResults.keys():
        print(
            f"{'-' * 40}\n{choice.upper()}\n{'-' * 40}\nTotal Played: {allResults[choice]['total']}\nPlayer Won: {allResults[choice]['playerWin']}\nAI Won: {allResults[choice]['aiWin']}\nTies: {allResults[choice]['tie']}"
        )


BOLD = "\033[1m"
RESET = "\033[0m"

def statisticsReport(gameData):
    """Generates the final statistics report for the game. It calls upon the other functions and puts it all together."""
    print(f"{BOLD}{'-' * 15}STATISTICS REPORT{'-' * 15}{RESET}\n")
    _trackWinLossTie(gameData)  # player's win/loss/tie by throw type
    print("\n\n" + "-" * 40)
    _winPercentage(gameData)  # the percentage that the player wins over the number of matches
    print("-" * 40)
    _longestWinStreak(gameData)
    print("-" * 40)
    _trackPlayerChoice(gameData)
    print("-" * 40)
    _trackAiChoice(gameData)
    print("-" * 40 + "\n\n")
    _headToHead(gameData)
