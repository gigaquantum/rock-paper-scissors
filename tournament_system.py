"""
Student B: Tournament System
- Best-of-3, best-of-5, best-of-7 formats
- Round tracking (display current round, scores)
- Match winner determination
- Series winner determination
- Ability to play multiple series
"""
from ai_logic import get_random_ai_move, get_counter_ai_move, get_pattern_ai_move

# play_series(5, 3, "random")
def play_series(num_tournaments, rounds_per_tournament, difficulty):
        print(f"You are playing {num_tournaments} tournaments")
        print(f"With each tournaments consisting of {rounds_per_tournament} rounds")
        print(f"Your difficulty is {difficulty}")
        

def determine_winner(player_move: str, ai_move: str) -> str:
    if player_move == ai_move:
        return "tie"
    elif (player_move == "rock" and ai_move == "scissors") or \
         (player_move == "paper" and ai_move == "rock") or \
         (player_move == "scissors" and ai_move == "paper"):
        return "player"
    else:
        return "computer"     

    # Ask for the number of rounds
round_input = input("Choose format: best-of-3, best-of-5, or best-of-7: ")

if round_input == "3":
        rounds_per_tournament = 3
elif round_input == "5":
        rounds_per_tournament = 5
elif round_input == "7":
        rounds_per_tournament = 7
else:
        print("Invalid format. Defaulting to best-of-3.")
        rounds_per_tournament = 3

difficulty_input = input("Choose AI difficulty: random, counter, or pattern: ").lower()

if difficulty_input in ["random", "counter", "pattern"]:
        difficulty = difficulty_input
else:
        print("Invalid difficulty. Defaulting to random.")
        difficulty = "random"

all_match_data = []
required_wins = (rounds_per_tournament // 2) + 1

num_tournaments = input("How many tournaments would you like to play? ")

for t in range(int(num_tournaments)):
    
        print(f"\n Tournament {t + 1} — Best of {rounds_per_tournament}")
        player_score = 0
        computer_score = 0
        tournament_data = []

        round_number = 1
        while player_score < required_wins and computer_score < required_wins:
            print(f"\n Round {round_number}")
            player_move = input("Choose rock, paper, or scissors: ").lower()=
            if player_move not in ["rock", "paper", "scissors"]:
                print("Invalid move. Try again.")
                continue
            
            # All the Ai's difficulty
            if difficulty == "random":
                ai_move = get_random_ai_move()
            elif difficulty == "counter":
                ai_move = get_counter_ai_move(all_match_data)
            elif difficulty == "pattern":
                ai_move = get_pattern_ai_move(all_match_data)
            else:
                ai_move = get_random_ai_move()

            print(f" AI chose: {ai_move}")
            

            
            winner = determine_winner(player_move, ai_move)

            if winner == "player":
                    player_score += 1
                    print("You win this round!")
            elif winner == "computer":
                    computer_score += 1
                    print("Computer wins this round!")
            else:
                    print("It's a tie!")

            round_number += 1

        tournament_data.append({
                "player_move": player_move,
                "ai_move": ai_move,
                "winner": winner
            })

        print(f"📊 Score — You: {player_score}, Computer: {computer_score}")


        all_match_data.append(tournament_data)

        print(f"\n Final Tournament Score — You: {player_score}, Computer: {computer_score}")
        if player_score > computer_score:
            print("You won the tournament!")
        else:
            print("Computer won the tournament!")

print("\n Series complete!")
    
play_again = input("\nWant to play again? (yes/no): ").lower()
if play_again == "yes":
        play_series(num_tournaments, rounds_per_tournament, difficulty)
else:
        print(" Thanks for playing! See you next time.")


    



 
        
