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

## Game data stored as a list of tournaments, with each tournament being a list of dictionaries that contain the user choice, AI choice, and winner of the match

# For example:
#data = [
#   [
#       {"player_move": "rock", "ai_move": "paper", "winner": "ai"},
#        {"player_move": "scissors", "ai_move": "paper", "winner": "player"},
#        {"player_move": "scissors", "ai_move": "scissors", "winner": "none"},
#    ],
#    [
#        {"player_move": "scissors", "ai_move": "rock", "winner": "ai"},
#        {"player_move": "scissors", "ai_move": "paper", "winner": "player"},
#        {"player_move": "rock", "ai_move": "scissors", "winner": "player"},
#    ],
#]

#tournament is the [] and each match is {}

#track win/loss/tie for each throw type
def track_win_loss_tie(data):
    wins = 0
    loss = 0 
    tie = 0 
    for tournament in data:
        for match in tournament:
            if match["winner"] == "player":
                wins += 1
            elif match["winner"] == "ai":
                loss += 1
            elif match["winner"] == "none":
                tie += 1
    return wins, loss, tie


