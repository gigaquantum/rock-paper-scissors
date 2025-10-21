"""
Student A: Core Game Logic & AI
- Implement basic rock-paper-scissors rules
- Random AI (completely random choices)
- Pattern AI (looks for player patterns in last 3-5 moves)
- Counter AI (plays what would beat player's most common choice)
- Input validation for player choices
"""

import random

MOVE_CHOICES = ["rock", "paper", "scissors"]


def flatten_match_data(move_data: list[list[dict]]) -> list[dict]:
    """Flattens the match data to prepare it for analysis."""

    return [match_dict for tournament in move_data for match_dict in tournament]


def get_random_ai_move() -> str:
    """Chooses a random move."""
    return MOVE_CHOICES[random.randint(0, 2)]


def get_counter_to_move(move: str) -> str:
    if move == "rock":
        return "paper"
    if move == "paper":
        return "scissors"
    if move == "scissors":
        return "rock"
    raise ValueError(f"'{move}' is not a valid move.")


def get_top_move(rock_count: int, paper_count: int, scissors_count: int) -> str:
    """Gets the top move based on the provided counts. If there's a tie, randomly chooses from the tied top moves."""

    top_moves = []
    if rock_count >= paper_count and rock_count >= scissors_count:
        top_moves.append("rock")
    if paper_count >= rock_count and paper_count >= scissors_count:
        top_moves.append("paper")
    if scissors_count >= rock_count and scissors_count >= paper_count:
        top_moves.append("scissors")

    # this selects a random move from the top moves when there's a tie
    return top_moves[random.randint(0, len(top_moves) - 1)]


def get_counter_ai_move(move_data: list[list[dict]]) -> str:
    """Chooses the move countering the player's most used move. If multiple moves are tied for being the most used, one of the tied moves will be randomly selected to be countered."""

    flattened_data = flatten_match_data(move_data)

    rock_count = 0
    paper_count = 0
    scissors_count = 0
    for round in flattened_data:
        if round["player_move"] == "rock":
            rock_count += 1
        elif round["player_move"] == "paper":
            paper_count += 1
        else:
            scissors_count += 1

    move_to_counter = get_top_move(rock_count, paper_count, scissors_count)
    return get_counter_to_move(move_to_counter)


def get_pattern_ai_move(move_data: list[list[dict]], context_length: int = 3) -> str:
    """Predicts the player's next move based on the player's previous moves, up to the context_length number of moves. If there's a tie, select randomly from the top predictions. If there's no data, selects a random move. If there's only one previous round, selects the move that beats the user's first move."""

    flattened_data = flatten_match_data(move_data)
    if len(flattened_data) == 0:
        return get_random_ai_move()
    if len(flattened_data) == 1:
        return get_counter_to_move(flattened_data[0]["player_move"])

    num_dimensions = min(context_length, len(flattened_data) - 1)

    move_counts = {move: 0 for move in MOVE_CHOICES}
    for _ in range(num_dimensions):
        higher_dimension_move_counts = {move: move_counts for move in MOVE_CHOICES}
        move_counts = higher_dimension_move_counts

    for i in range(len(flattened_data) - num_dimensions):
        window = flattened_data[i : i + num_dimensions + 1]
        move_order = []
        for move_dict in window:
            move_order.append(move_dict["player_move"])
        selected_combo = move_counts
        for move in move_order[:-1]:
            next_level = selected_combo[move]
            selected_combo = next_level
        selected_combo[move_order[-1]] += 1

    move_order_context = []
    for move_dict in flattened_data[-num_dimensions:]:
        move_order_context.append(move_dict["player_move"])
    current_context_data = move_counts
    for move in move_order_context:
        next_level = current_context_data[move]
        current_context_data = next_level

    move_to_counter = get_top_move(
        current_context_data["rock"],
        current_context_data["paper"],
        current_context_data["scissors"],
    )
    return get_counter_to_move(move_to_counter)


if __name__ == "__main__":
    test_data = [
        [
            {"player_move": "rock", "ai_move": "paper", "winner": "ai"},
            {"player_move": "scissors", "ai_move": "paper", "winner": "player"},
            {"player_move": "scissors", "ai_move": "scissors", "winner": "none"},
        ],
        [
            {"player_move": "scissors", "ai_move": "rock", "winner": "ai"},
            {"player_move": "scissors", "ai_move": "paper", "winner": "player"},
            {"player_move": "rock", "ai_move": "scissors", "winner": "player"},
        ],
    ]

    print("Random AI Move:", get_random_ai_move())
    print("Counter AI Move:", get_counter_ai_move(test_data))
    print("Counter AI Move:", get_pattern_ai_move(test_data))
