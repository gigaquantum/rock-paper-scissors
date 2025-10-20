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


def track_win_loss_tie(data):
    """Tracks the result of each match/throw for the player."""
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


#calculate win percentage
def win_percentage(wins,loss,tie):
    """Tracks the percentage of wins for the user across all tournaments"""
    total_match = wins + loss + tie
    if total_match == 0: #no division by 0 
        return 0 
    return((wins/total_match)*100)

def current_streak(wins,loss):
    """If the last 2 matches have been wins then user is on a winning streak, if last 2 matches have been losses, user is on a losing streak."""