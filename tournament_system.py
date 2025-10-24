"""
Student B: Tournament System
- Best-of-3, best-of-5, best-of-7 formats
- Round tracking (display current round, scores)
- Match winner determination
- Series winner determination
- Ability to play multiple series
"""
from aiLogic import getRandomAiMove, getCounterAiMove, getPatternAiMove

# play_series(5, 3, "random")
def playSeries(numTournaments, roundsPerTournament, difficulty):
        print(f"You are playing {numTournaments} tournaments")
        print(f"With each tournaments consisting of {roundsPerTournament} rounds")
        print(f"Your difficulty is {difficulty}")
        

def determineWinner(playerMove: str, aiMove: str) -> str:
    if playerMove == aiMove:
        return "tie"
    elif (playerMove == "rock" and aiMove == "scissors") or \
         (playerMove == "paper" and aiMove == "rock") or \
         (playerMove == "scissors" and aiMove == "paper"):
        return "player"
    else:
        return "computer"     

    # Ask for the number of rounds
roundInput = input("Choose format: best-of-3, best-of-5, or best-of-7: ")

if roundInput == "3":
        roundsPerTournament = 3
elif roundInput == "5":
        roundsPerTournament = 5
elif roundInput == "7":
        roundsPerTournament = 7
else:
        print("Invalid format. Defaulting to best-of-3.")
        roundsPerTournament = 3

difficultyInput = input("Choose AI difficulty: random, counter, or pattern: ").lower()

if difficultyInput in ["random", "counter", "pattern"]:
        difficulty = difficultyInput
else:
        print("Invalid difficulty. Defaulting to random.")
        difficulty = "random"

allMatchData = []
requiredWins = (roundsPerTournament // 2) + 1

numTournaments = input("How many tournaments would you like to play? ")

for t in range(int(numTournaments)):
    
        print(f"\n Tournament {t + 1} — Best of {roundsPerTournament}")
        playerScore = 0
        computerScore = 0
        tournamentData= []

        roundNumber = 1
        while playerScore < requiredWins and computerScore < requiredWins:
            print(f"\n Round {roundNumber}")
            playerMove = str(input("Choose rock, paper, or scissors: ")).lower()
            if playerMove not in ["rock", "paper", "scissors"]:
                print("Invalid move. Try again.")
                continue
            
            # All the Ai's difficulty
            if difficulty == "random":
                aiMove = getRandomAiMove()
            elif difficulty == "counter":
                aiMove = getCounterAiMove(allMatchData)
            elif difficulty == "pattern":
                aiMove = getPatternAiMove(allMatchData)
            else:
                aiMove = getRandomAiMove()

            print(f" AI chose: {aiMove}")
            

            
            winner = determineWinner(playerMove, aiMove)

            if winner == "player":
                    playerScore += 1
                    print("You win this round!")
            elif winner == "computer":
                    computerScore += 1
                    print("Computer wins this round!")
            else:
                    print("It's a tie!")

            roundNumber += 1

        tournamentData.append({
                "player_move": playerMove,
                "ai_move": aiMove,
                "winner": winner
            })

        print(f"Score — You: {playerScore}, Computer: {computerScore}")


        allMatchData.append(tournamentData)

        print(f"\n Final Tournament Score — You: {playerScore}, Computer: {computerScore}")
        if playerScore > computerScore:
            print("You won the tournament!")
        else:
            print("Computer won the tournament!")

print("\n Series complete!")
    
playAgain = input("\nWant to play again? (yes/no): ").lower()
if playAgain == "yes":
        playSeries(numTournaments, roundsPerTournament, difficulty)
else:
        print(" Thanks for playing! See you next time.")
