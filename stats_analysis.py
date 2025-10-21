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


def track_player_choice(data):
    """Tracks the player's choice throughout the tournament, returns the most common choice."""
    player_rock = 0
    player_scissors = 0 
    player_paper = 0 
    
    for tournament in data:
        for match in tournament:
            if match["player_move"] == "rock":
                player_rock += 1
            elif match["player_move"] == "scissors":
                player_scissors += 1
            elif match["player_move"] == "paper":
                player_paper += 1
    
    most_common_player_choice = ""
    if player_rock < player_scissors > player_paper:
        most_common_player_choice = "scissors"
    elif player_scissors < player_rock > player_paper:
        most_common_player_choice = "rock"
    else:
        most_common_player_choice = "paper"

    return most_common_player_choice

def track_ai_choice(data):
    """Tracks AI's choice throughout the tournament, returns its most common choice."""
    ai_rock = 0
    ai_scissors = 0 
    ai_paper = 0 
    
    for tournament in data:
        for match in tournament:
            if match["ai_move"] == "rock":
                ai_rock += 1
            elif match["ai_move"] == "scissors":
                ai_scissors += 1
            elif match["ai_move"] == "paper":
                ai_paper += 1
    
    most_common_ai_choice = ""
    if ai_rock < ai_scissors > ai_paper:
        most_common_ai_choice = "scissors"
    elif ai_scissors < ai_rock > ai_paper:
        most_common_ai_choice = "rock"
    else:
        most_common_ai_choice = "paper"

    return most_common_ai_choice


# def head_to_head(data):
#     """Keeps track of the results based on throw type."""
#     rock = 0
#     scissors = 0
#     paper = 0

#     scissor_winner_p = 0
#     scissor_winner_ai = 0
#     scissor_tie = 0

#     rock_winner_p = 0
#     rock_winner_ai = 0
#     rock_tie = 0

#     paper_winner_p = 0
#     paper_winner_ai = 0
#     paper_tie = 0

#     for tournament in data: 
#         for match in tournament:
#             if match["player_move"] == "scissors" or match['ai_move'] == "scissors":
#                 scissors += 1 
#             if match["winner"] == "player" and match["player_move"] == "scissors":
#                 scissor_winner_p += 1
#             elif match["winner"] == "ai" and match["ai_move"] == "scissors":
#                 scissor_winner_ai += 1
#             elif match["winner"] == "none" and match["ai_move"] == "scissors" and match["player_move"] == "scissors":
#                 scissor_tie += 1


#     for tournament in data: 
#         for match in tournament:
#             if match["player_move"] == "rock" or match['ai_move'] == "rock":
#                 rock += 1 
#             if match["winner"] == "player" and match["player_move"]== "rock":
#                 rock_winner_p += 1
#             elif match["winner"] == "ai" and match["ai_move"]== "rock":
#                 rock_winner_ai += 1
#             elif match["winner"] == "none" and match["ai_move"]=="rock" and match["player_move"] == "rock":
#                 rock_tie += 1


#     for tournament in data: 
#         for match in tournament:
#             if match["player_move"] == "paper" or match['ai_move'] == "paper":
#                 paper += 1 
#             if match["winner"] == "player" and match["player_move"]== "paper":
#                 paper_winner_p += 1
#             elif match["winner"] == "ai" and match["ai_move"]== "paper":
#                 paper_winner_ai += 1
#             elif match["winner"] == "none" and match["ai_move"]=="paper" and match["player_move"] == "paper":
#                 paper_tie += 1

#     return rock, paper, scissors, rock_tie, rock_winner_ai, rock_winner_p, paper_tie, paper_winner_ai, paper_winner_p, scissor_tie, scissor_winner_ai, scissor_winner_p

def head_to_head(data):
    all_results = {
        "rock": {"total": 0 , "player_win": 0, "ai_win": 0, "tie": 0},
        "paper": {"total": 0 , "player_win": 0, "ai_win": 0, "tie": 0},
        "scissors": {"total": 0 , "player_win": 0, "ai_win": 0, "tie": 0}
    }
    for tournament in data:
        for match in tournament:
            match_winner = match["winner"]
            for choice in all_results.keys():
                if choice in (match["player_move"],match["ai_move"]): #what were the moves played during this match (player's,ai) and the choice checks if the rock, paper, or scissors matches one of them 
                    all_results[choice]["total"] += 1 

                    if match_winner == "player" and match["player_move"]== choice:
                        all_results[choice]["player_win"] += 1
                    elif match_winner == "ai" and match["ai_move"] == choice:
                        all_results[choice]["ai_win"] += 1
                    else:
                        all_results[choice]["tie"]+= 1
    return all_results
#potentially print as a table? 

