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

#can use these to improve user experience
bold = "\033[1m"
reset = "\033[0m"
cyan = "\033[36m"

def _trackWinLossTie(data):  # the underscore before the name denotes that this is a private function, and is to be used internally. The only function I will be calling into my Main program will be statisticsReport.
    """Tracks the number of wins, losses and ties for each move type the player chose. Will print a nicely formatted summary with all the information."""

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

    print(f"{bold}WINS, LOSS AND TIE BY THROW TYPE{reset}")
    for choice in allResults.keys():
        print(
            f"{'-' * 60}\n{cyan}{bold}{choice.upper()}{reset}\n{'-' * 60}\n"
            f"{bold}Wins:{reset} {allResults[choice]['win']}\n"
            f"{bold}Losses:{reset} {allResults[choice]['loss']}\n"
            f"{bold}Ties:{reset} {allResults[choice]['tie']}"
        )


def _collectMatchResult(data):
    """Compiles all match results throughout the entirety of the game (also known as the series) into a single list. Returns a list of strings with all the match outcomes:'win','lose','tie'."""
    matchResult = []
    for tournament in data:  # collect my match results in order of being played
        for match in tournament:
            if match["winner"] == "player":
                matchResult.append("win")
            elif match["winner"] == "ai":
                matchResult.append("loss")
            else:
                matchResult.append("tie")
    return matchResult


def _allWinLossTie(data):
    """Computes the number of wins, losses and ties throughout the entirety of the game (also known as the series) and returns it as a tuple (wins,losses,ties)."""
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


def _winPercentage(data):
    """Computes the win percentage across the entirety of the game (also known as the series). The formula for percentage is: the total number of wins divided by the total number of matches played and the quotient multiplied by 100.Prints answer rounded to 2 decimal places."""
    win, loss, tie = _allWinLossTie(data)
    totalMatch = win + loss + tie
    formula = (win / totalMatch) * 100
    print(f"{bold}You won {cyan}{formula:.2f}%{reset} {bold}of the matches{reset}")

#continue cleaning code and docstrings
def currentStreak(data):
    """If the last 2 matches have been wins then user is on a winning streak, if last 2 matches have been losses, user is on a losing streak."""
    matchResult = _collectMatchResult(data)  # this calls my function above that stores all my match results

    lastPlay = matchResult[-1]  # compares only the last 2 results from the tournament
    streakCount = 1

    secondToLast = (len(matchResult) - 2)  # am going to iterate backwards so this shows that i am starting from the second to last match
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
        print(f"You are currently in a {streakLabel} of length: {streakCount}")


def _longestWinStreak(data):
    """Takes a look at each tournament and determines what the longest streak in that tournament was."""
    matchResult = _collectMatchResult(data)

    longestStreak = 1
    currentStreakCount = 1
    longestStreakType = matchResult[0]  # this makes it so I start with the first match result

    for r in range(
        1, len(matchResult)
    ):  # I start looping through the results from the second match onward
        if matchResult[r] == matchResult[r - 1]:
            currentStreakCount += 1
        else:
            currentStreakCount = 1  # resets my streak count bc it was broken

        if currentStreakCount > longestStreak:
            longestStreak = currentStreakCount
            longestStreakType = matchResult[r]
    
    if longestStreak == 1:
        print(f"{bold}You had no streaks!{reset}")

    if longestStreakType == "win":
        streakLabel = "winning streak"
    elif longestStreakType == "loss":
        streakLabel = "losing streak"
    else:
        streakLabel = "tie streak"

    print(
        f"{bold}Your longest streak was: {cyan}{longestStreak}{reset}{bold} and it was a {cyan}{streakLabel}.{reset}"
    )


def _trackPlayerChoice(data):
    """Tracks the player's choice throughout the tournament, returns the most common choice."""
    playerCounts = {"rock": 0, "paper": 0, "scissors": 0}

    for tournament in data:
        for match in tournament:
            choice = match["playerMove"]
            if choice in playerCounts:
                playerCounts[choice] += 1

    max_count = max(playerCounts.values())
    mostCommonPlayerChoice = [
        choice for choice, count in playerCounts.items() if count == max_count
    ]
    if len(mostCommonPlayerChoice) == 1:
        print(
            f"{bold}Most common player move: {cyan}{mostCommonPlayerChoice[0]}{reset}"
        )
    else:
        print(
            f"{bold}Most common player move was tied between: {cyan}{', '.join(mostCommonPlayerChoice[:-1])}, and {mostCommonPlayerChoice[-1]}{reset}"
        )


def _trackAiChoice(data):
    """Tracks AI's choice throughout the tournament, returns its most common choice."""

    aiCounts = {"rock": 0, "paper": 0, "scissors": 0}

    for tournament in data:
        for match in tournament:
            choice = match["aiMove"]
            if choice in aiCounts:
                aiCounts[choice] += 1

    max_count = max(aiCounts.values())
    mostCommonAiChoice = [
        choice for choice, count in aiCounts.items() if count == max_count
    ]
    if len(mostCommonAiChoice) == 1:
        print(f"{bold}Most common AI move: {cyan}{mostCommonAiChoice[0]}{reset}")
    else:
        print(
            f"{bold}Most common AI move was tied between: {cyan}{', '.join(mostCommonAiChoice[:-1])}, and {mostCommonAiChoice[-1]}{reset}"
        )


def _headToHead(data):
    allResults = {
        "rock": {"total": 0, "playerWin": 0, "playerLoss": 0, "aiWin": 0, "aiLoss": 0, "tie": 0},
        "paper": {"total": 0, "playerWin": 0, "playerLoss": 0, "aiWin": 0, "aiLoss": 0, "tie": 0},
        "scissors": {"total": 0, "playerWin": 0, "playerLoss": 0, "aiWin": 0, "aiLoss": 0, "tie": 0},
    }
    for tournament in data:
        for match in tournament:
            matchWinner = match["winner"]
           
            playerChoice = match["playerMove"].strip().lower()
            aiChoice = match["aiMove"].strip().lower()

            if matchWinner == "none":
                matchWinner = "tie"



            allResults[playerChoice]["total"] += 1
            allResults[aiChoice]["total"] += 1
                    
    
            if matchWinner == "player":
                allResults[playerChoice]["playerWin"] += 1
                allResults[aiChoice]["aiLoss"] += 1
            elif matchWinner == "ai":
                allResults[aiChoice]["aiWin"] += 1
                allResults[playerChoice]["playerLoss"] += 1
            elif matchWinner == "tie":
                allResults[playerChoice]["tie"] += 1
 
    print(f"{bold}HEAD-TO-HEAD STATS BY THROW TYPE{reset}")
    for choice in allResults.keys():
        print(
            f"{'-' * 60}\n{cyan}{bold}{choice.upper()}\n{'-' * 60}{reset}{bold}\n"
            f"Total times {choice} was played: {cyan}{allResults[choice]['total']}{reset}{bold}\n"
            f"You won {cyan}{allResults[choice]['playerWin']}{reset}{bold} times using {choice}\n"
            f"You lost {cyan}{allResults[choice]['playerLoss']}{reset}{bold} times using {choice}\n"
            f"AI won {cyan}{allResults[choice]['aiWin']}{reset}{bold} times when it used {choice}\n"
            f"AI lost {cyan}{allResults[choice]['aiLoss']}{reset}{bold} times when it used {choice}\n"
            f"There were {cyan}{allResults[choice]['tie']}{reset}{bold} ties with {choice}{reset}"
        )


def statisticsReport(gameData):
    """Generates the final statistics report for the game. It calls upon the other functions and puts it all together."""
    print(f"{bold}{cyan}{'-' * 15}END OF SERIES STATISTICS REPORT{'-' * 15}{reset}\n")
    _trackWinLossTie(gameData)  # player's win/loss/tie by throw type
    print("\n\n" + "-" * 60)
    _winPercentage(
        gameData
    )  # the percentage that the player wins over the number of matches
    print("-" * 60)
    _longestWinStreak(gameData)
    print("-" * 60)
    _trackPlayerChoice(gameData)
    print("-" * 60)
    _trackAiChoice(gameData)
    print("-" * 60 + "\n\n")
    _headToHead(gameData)

