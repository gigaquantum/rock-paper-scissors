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

def _normalizeWinner(match): #in some places in parts of the comprehensive game code the winner is referenced as "none" and others its "tie". This will help my stats not get mixed up and ensure proper tracking. Will need this function for other functions!
    """This makes sure all my winner labels are the same, if the label is none it renames it as 'tie'."""
    winner = match.get("winner","tie")
    if winner == "none":
        winner = "tie"
    return winner 

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
            winner = _normalizeWinner(match)

            if winner == "player":
                allResults[choice]["win"] += 1
            elif winner == "ai":
                allResults[choice]["loss"] += 1
            elif winner == "tie":
                allResults[choice]["tie"] += 1

    print(f"{bold}WINS, LOSS AND TIE BY THROW TYPE{reset}") #prints a summary table using ANSI codes: throw type should be bold and cyan, wins, losses, tie labels should be bold and their respective values should be printed with no effects.
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
        for match in tournament:  #this loop converts the match outcomes into strings of win, loss, tie and adds them into a list 
            winner = _normalizeWinner(match)
            if winner == "player":
                matchResult.append("win")
            elif winner == "ai":
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
            winner = _normalizeWinner(match)
            if winner == "player":
                win += 1
            elif winner == "ai":
                loss += 1
            else:
                tie += 1
    return win, loss, tie


def _winPercentage(data):
    """Computes the win percentage across the entirety of the game (also known as the series). The formula for percentage is: the total number of wins divided by the total number of matches played and the quotient multiplied by 100.Prints answer rounded to 2 decimal places."""
    win, loss, tie = _allWinLossTie(data)
    totalMatch = win + loss + tie
    if totalMatch == 0: #handles division by zero
        print("Win percentage unavailable as no matches were played.")
        return  
    formula = (win / totalMatch) * 100
    print(f"{bold}You won {cyan}{formula:.2f}%{reset} {bold}of the matches{reset}")


def currentStreak(data):
    """Check's the player's current streak (wins, loss or tie) by looking at the last match results and comparing them with the current match results.Prints a message if the player is currently in a streak of at least 2 consecutive wins, losses or ties. """
    matchResult = _collectMatchResult(data)  # this calls my function above that stores all my match results

    lastPlay = matchResult[-1]  # compares only the last 2 results from the tournament
    streakCount = 1

    secondToLast = (len(matchResult) - 2)  # am going to iterate backwards so this shows that I am starting from the second to last match
    while secondToLast >= 0 and matchResult[secondToLast] == lastPlay:
        streakCount += 1
        secondToLast -= 1

    if lastPlay == "win":  #this if elif else will label what kind of streak type it is
        streakLabel = "winning streak"
    elif lastPlay == "loss":
        streakLabel = "losing streak"
    else:
        streakLabel = "tie streak"

    if streakCount >= 2: #only prints if streak is greater than 2
        print(f"You are currently in a {streakLabel} of length: {streakCount}")


def _longestWinStreak(data):
    """Calculates and prints the player's longest win streak across all tournaments. If the player never had a streak of 2 or more consecutive wins, prints a message indicating a win streak never ocurred."""
    matchResult = _collectMatchResult(data)

    longestStreak = 0
    currentStreakCount = 0

    for result in matchResult:
        if result == "win":
            currentStreakCount += 1
            if currentStreakCount > longestStreak:
                longestStreak = currentStreakCount
        else:
            currentStreakCount = 0 #resets my counter if the outcome wasn't a win
    
    if longestStreak <= 1: #only prints if the win streak is 1 or less
        print(f"{bold}You had no win streaks!{reset}")
    else:
        print(f"{bold}Your longest win streak was: {cyan}{longestStreak}{reset}")


def _trackPlayerChoice(data):
    """Tracks the player's choice for a move across all tournaments, then uses this data to determine the most frequently used move. Prints this move and if there is a tie, all the tied moves are printed."""
    playerCounts = {"rock": 0, "paper": 0, "scissors": 0}

    for tournament in data:
        for match in tournament:
            choice = match["playerMove"]
            if choice in playerCounts:
                playerCounts[choice] += 1

    maxCount = max(playerCounts.values()) #this line finds the highest num of times a throw/move was chosen by the player. It stores the largest one in maxCount
    mostCommonPlayerChoice = [choice for choice, count in playerCounts.items() if count == maxCount] #this line handles cases of ties, it iterates through the moves and checks which ones have a count equal to maxCount and adds them to the list mostCommonPlayerChoice

    if len(mostCommonPlayerChoice) == 1:
        print(f"{bold}Most common player move: {cyan}{mostCommonPlayerChoice[0]}{reset}")
    else:
        print(f"{bold}Most common player move was tied between: {cyan}{', '.join(mostCommonPlayerChoice[:-1])}, and {mostCommonPlayerChoice[-1]}{reset}")


def _trackAiChoice(data):
    """Tracks the AI's choice for a move across all tournaments, then uses this data to determine the most frequently used move. Prints this move and if there is a tie, all the tied moves are printed."""

    aiCounts = {"rock": 0, "paper": 0, "scissors": 0}

    for tournament in data:
        for match in tournament:
            choice = match["aiMove"]
            if choice in aiCounts:
                aiCounts[choice] += 1

    maxCount = max(aiCounts.values()) #same logic that was used in trackPlayerChoice
    mostCommonAiChoice = [choice for choice, count in aiCounts.items() if count == maxCount]
    if len(mostCommonAiChoice) == 1:
        print(f"{bold}Most common AI move: {cyan}{mostCommonAiChoice[0]}{reset}")
    else:
        print(
            f"{bold}Most common AI move was tied between: {cyan}{', '.join(mostCommonAiChoice[:-1])}, and {mostCommonAiChoice[-1]}{reset}"
        )


def _headToHead(data):
    """tracks and prints a detailed head-to-head statistics for each move type (rock, paper, scissors) across all tournaments. Prints a detailed summary of: total times the move was played, wins and losses for the player using that move, wins and losses for the AI using that move, number of ties for the move."""
    allResults = {
        "rock": {"total": 0, "playerWin": 0, "playerLoss": 0, "aiWin": 0, "aiLoss": 0, "tie": 0},
        "paper": {"total": 0, "playerWin": 0, "playerLoss": 0, "aiWin": 0, "aiLoss": 0, "tie": 0},
        "scissors": {"total": 0, "playerWin": 0, "playerLoss": 0, "aiWin": 0, "aiLoss": 0, "tie": 0},
    }
    for tournament in data:
        for match in tournament:
            matchWinner = _normalizeWinner(match)
           
            playerChoice = match["playerMove"].strip().lower()
            aiChoice = match["aiMove"].strip().lower()

            allResults[playerChoice]["total"] += 1 #tracks the total number of times each move is played
            allResults[aiChoice]["total"] += 1
                    
    
            if matchWinner == "player":
                allResults[playerChoice]["playerWin"] += 1
                allResults[aiChoice]["aiLoss"] += 1
            elif matchWinner == "ai":
                allResults[aiChoice]["aiWin"] += 1
                allResults[playerChoice]["playerLoss"] += 1
            elif matchWinner == "tie":
                allResults[playerChoice]["tie"] += 1   #only counts the tie once since it should be intuitive that if there is a tie it involed 2 of the "total times" the move was played. So if rock total played was: 2 the tie will print 1.
 
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
    """Generates the final statistics report for the game series. It calls upon the other functions and prints it out nicely formatted."""
    if not gameData or not any(gameData):
        print(f"{bold}No data or insufficient data available to generate statistics.{reset}")
        return

    print(f"{bold}{cyan}{'-' * 15}END OF SERIES STATISTICS REPORT{'-' * 15}{reset}\n") #my table header
    
    #calls all of my private functions to generate the stats report
    _trackWinLossTie(gameData)  
    print("\n\n" + "-" * 60)
    _winPercentage(gameData)  
    print("-" * 60)
    _longestWinStreak(gameData)
    print("-" * 60)
    _trackPlayerChoice(gameData)
    print("-" * 60)
    _trackAiChoice(gameData)
    print("-" * 60 + "\n\n")
    _headToHead(gameData)

