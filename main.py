import random
from Mancala import *


def play_game_2_random_players(pits_per_player=6, stones_per_pit=4):
    game = Mancala(pits_per_player, stones_per_pit)
    turns = 0

    while not game.isGameOver():
        pit = game.random_move_generator()
        if pit is None:
            break

        game.play(pit)
        turns += 1

    p1_score = game.board[game.p1_mancala_index]
    p2_score = game.board[game.p2_mancala_index]

    if p1_score > p2_score:
        winner = 1
    elif p2_score > p1_score:
        winner = 2
    else:
        winner = 0

    return {
        'turns': turns,
        'winner': winner,
        'p1_score': p1_score,
        'p2_score': p2_score
    }


def run_2random_players_simulation(num_games=100, pits_per_player=6, stones_per_pit=4):
    stats = {
        'p1_wins': 0,
        'p2_wins': 0,
        'ties': 0,
        'total_turns': 0
    }

    for _ in range(num_games):
        result = play_game_2_random_players(pits_per_player, stones_per_pit)

        if result['winner'] == 1:
            stats['p1_wins'] += 1
        elif result['winner'] == 2:
            stats['p2_wins'] += 1
        else:
            stats['ties'] += 1

        stats['total_turns'] += result['turns']

    return stats


def print_statistics(stats, num_games):
    print("\nSimulation results:")
    print(f"Total games : {num_games}")

    p1_win_percent = (stats['p1_wins'] / num_games) * 100
    print("\nPlayer 1 (First player):")
    print(f"Games won: {stats['p1_wins']} ({p1_win_percent:.2f}%)")
    print(f"Games lost: {stats['p2_wins']} ({(stats['p2_wins'] / num_games) * 100:.2f}%)")
    print(f"Games tied: {stats['ties']} ({(stats['ties'] / num_games) * 100:.2f}%)")

    p2_win_percent = (stats['p2_wins'] / num_games) * 100
    print("\nPlayer 2 (Second player):")
    print(f"Games won: {stats['p2_wins']} ({p2_win_percent:.2f}%)")
    print(f"Games lost: {stats['p1_wins']} ({(stats['p1_wins'] / num_games) * 100:.2f}%)")
    print(f"Games tied: {stats['ties']} ({(stats['ties'] / num_games) * 100:.2f}%)")

    avg_turns = stats['total_turns'] / num_games
    print(f"\nAverage number of turns per game: {avg_turns:.2f}")

    advantage = p1_win_percent - p2_win_percent
    if advantage > 0:
        print(f"\nYes there is a first move advantage by by {advantage:.2f}%")
    elif advantage < 0:
        print(f"\nNo first move advantage, second player adv of {abs(advantage):.2f}%")
    else:
        print("\nFirst move advantage: NONE, both players have equal win rates")


NUM_GAMES = 100
PITS_PER_PLAYER = 6
STONES_PER_PIT = 4


def main():
    print("Select game mode:")
    print("1. Two Random Players")

    while True:
        try:
            choice = int(input("Enter choice (1): "))
            if choice == 1:
                stats = run_2random_players_simulation(NUM_GAMES, PITS_PER_PLAYER, STONES_PER_PIT)
                print_statistics(stats, NUM_GAMES)
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()