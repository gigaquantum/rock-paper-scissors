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

def collect_match_result(data):
  """This makes a list of the wins, loss, ties per tournament. This can then be used in other functions."""
  match_result = []
  for tournament in data: #collect my match results in order of being played
        for match in tournament:
            if match["winner"] == "player":
                match_result.append("win")
            elif match["winner"] == "ai":
                match_result.append("loss")
  return match_result

#calculate win percentage
def win_percentage(win,loss,tie):
    """Tracks the percentage of wins for the user across all tournaments"""
    total_match = win + loss + tie
    if total_match == 0: #no division by 0 
        return 0 
    return((win/total_match)*100)

def current_streak(data):
    """If the last 2 matches have been wins then user is on a winning streak, if last 2 matches have been losses, user is on a losing streak."""
    match_result = collect_match_result(data) #this calls my function above that stores all my match results 
    if len(match_result) < 2:
        return "No streak yet, not enough matches have been played"
    
    last_two = match_result[-2:] #compares only the last 2 results from the tournament
    streak_count = 0 


    if last_two[0] == last_two[1] and last_two[0] != "tie": #if the last two are the same then my streak count increases, if there is a tie or the last two dont match that breaks the streak
        streak_count += 1
    else:
        streak_count = 0 

    if last_two == ["win","win"]: 
        streak_type = "winning streak"
    elif last_two == ["loss","loss"]:
        streak_type = "losing streak"
    else:
        streak_type = "no streak"
    
    return streak_count , streak_type

    #this code isn't dynamic, so each time a new match is played we need to update the match result, so should we have another function to update it as the game is played? 

def longest_win_streak(data):
    """Takes a look at each tournament and determines what the longest streak in that tournament was."""
    match_result = collect_match_result(data)

    longest_streak = 0 
    current_streak_count = 0

    for r in match_result:
        if r == "win":
            current_streak_count += 1
            if current_streak_count > longest_streak:
                longest_streak = current_streak_count
        else:
            current_streak_count = 0
    
    return longest_streak
    
