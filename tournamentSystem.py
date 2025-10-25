"""
Student B: Tournament System
- Best-of-3, best-of-5, best-of-7 formats
- Round tracking (display current round, scores)
- Match winner determination
- Series winner determination
- Ability to play multiple series
"""
#we can use these to make the output more user friendly and easier to read
bold = "\033[1m"
reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"
underline = "\033[4m"

import time

from typing import Callable, Literal

from aiLogic import getRandomAiMove, getCounterAiMove, getPatternAiMove
from statsAnalysis import statisticsReport, currentStreak


def _waitForUser():
    time.sleep(2)
    input("\nPress any key and hit enter to continue...")


def _determineWinner(playerMove: str, aiMove: str) -> str:
    if playerMove == aiMove:
        return "tie"
    elif (
        (playerMove == "rock" and aiMove == "scissors")
        or (playerMove == "paper" and aiMove == "rock")
        or (playerMove == "scissors" and aiMove == "paper")
    ):
        return "player"
    else:
        return "ai"


# playSeries(5, 3, "random")
def playSeries(
    numTournaments: int,
    roundsPerTournament: int,
    difficulty: Literal["random", "counter", "pattern"],
    clearOutput: Callable,
) -> bool:
    clearOutput()
    print(f"You are playing {numTournaments} tournaments.")
    print(f"With each tournaments consisting of {roundsPerTournament} rounds.")
    print(f"Your difficulty is {difficulty}.")
    _waitForUser()

    allMatchData = []
    requiredWins = (roundsPerTournament // 2) + 1

    for t in range(int(numTournaments)):
        clearOutput()
        print(f"\n{bold}{underline}Tournament {t + 1} — Best of {roundsPerTournament}{reset}")
        playerScore = 0
        aiScore = 0
        allMatchData.append([])
        roundNumber = 0
        while playerScore < requiredWins and aiScore < requiredWins:
            roundNumber += 1
            print(f"\nRound {roundNumber}")
            playerMove = str(input("Choose rock, paper, or scissors: ")).lower()
            while playerMove not in ["rock", "paper", "scissors"]:
                print(f"{bold}{red}Invalid move. Try again.{reset}")
                playerMove = str(input("\nChoose rock, paper, or scissors: ")).lower()

            # All the AI's difficulty
            if difficulty == "counter":
                aiMove = getCounterAiMove(allMatchData)
            elif difficulty == "pattern":
                aiMove = getPatternAiMove(allMatchData)
            else:
                aiMove = getRandomAiMove()
            print(f"AI chose: {aiMove}")

            winner = _determineWinner(playerMove, aiMove)
            if winner == "player":
                playerScore += 1
                print("You win this round!")
            elif winner == "ai":
                aiScore += 1
                print("AI wins this round!")
            else:
                print("It's a tie!")
            print(f"Score — You: {playerScore}, AI: {aiScore}")
            allMatchData[-1].append(
                {"playerMove": playerMove, "aiMove": aiMove, "winner": winner}
            )
            currentStreak(allMatchData)

        print(f"\n{bold}Final Tournament Score — {green}You: {playerScore}{reset}, {bold}{purple}AI: {aiScore}{reset}")
        if playerScore > aiScore:
            print(f"{bold}{green}You won the tournament!")
        else:
            print(f"{bold}{purple}AI won the tournament!")
        _waitForUser()

    clearOutput()
    print("Series complete!\n")

    statisticsReport(allMatchData)
    _waitForUser()
    clearOutput()
    playAgain = input("\nWant to play again? (yes/no): ").lower()
    if playAgain == "yes":
        clearOutput()
        return True
    else:
        print(f"{bold}Thanks for playing! See you next time.")
        return False
