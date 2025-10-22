"""
Student B: Tournament System
- Best-of-3, best-of-5, best-of-7 formats
- Round tracking (display current round, scores)
- Match winner determination
- Series winner determination
- Ability to play multiple series
"""
def play_series():
    print("\n Starting a new series!")
    while True:
        try:
            best_of = int(input("Choose format (3, 5, or 7 rounds): "))
            if best_of in [3, 5, 7]:
                break
            print("Please choose 3, 5, or 7.")
        except ValueError:
            print("Enter a number.")

    wins_needed = best_of // 2 + 1
    player_score = 0
    ai_score = 0
    round_number = 1

    while player_score < wins_needed and ai_score < wins_needed:
        print(f"\nRound {round_number}")
        print(f"Score: Player {player_score} - AI {ai_score}")
    # I have to come back to this and ask Alex which is the player move 
        player = _get_counter_to_move()
        ai = get_ai_move()
        winner = get_winner(player, ai)

        print(f"AI chose {ai}. Result: {winner.upper() }")
        if winner == "player":
            player_score += 1
        elif winner == "ai":
            ai_score += 1

        round_number += 1

    print("\n Series Finished")
    if player_score > ai_score:
        print(f" You win the series {player_score} to {ai_score}!")
    else:
        print(f" AI wins the series {ai_score} to {player_score}!")

while True:
    play_series()
    again = input("\nPlay another series? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break
