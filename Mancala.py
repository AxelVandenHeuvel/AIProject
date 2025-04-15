import random


class Mancala:
    def __init__(self, pits_per_player=6, stones_per_pit=4):
        """
        The constructor for the Mancala class defines several instance variables:

        pits_per_player: This variable stores the number of pits each player has.
        stones_per_pit: It represents the number of stones each pit contains at the start of any game.
        board: This data structure is responsible for managing the Mancala board.
        current_player: This variable takes the value 1 or 2, as it's a two-player game, indicating which player's turn it is.
        moves: This is a list used to store the moves made by each player. It's structured in the format (current_player, chosen_pit).
        p1_pits_index: A list containing two elements representing the start and end indices of player 1's pits in the board data structure.
        p2_pits_index: Similar to p1_pits_index, it contains the start and end indices for player 2's pits on the board.
        p1_mancala_index and p2_mancala_index: These variables hold the indices of the Mancala pits on the board for players 1 and 2, respectively.
        """
        self.pits_per_player = pits_per_player
        self.board = [stones_per_pit] * (
                    (pits_per_player + 1) * 2)  # Initialize each pit with stones_per_pit number of stones
        self.players = 2
        self.current_player = 1
        self.moves = []
        self.p1_pits_index = [0, self.pits_per_player - 1]
        self.p1_mancala_index = self.pits_per_player
        self.p2_pits_index = [self.pits_per_player + 1, len(self.board) - 1 - 1]
        self.p2_mancala_index = len(self.board) - 1

        # Zeroing the Mancala for both players
        self.board[self.p1_mancala_index] = 0
        self.board[self.p2_mancala_index] = 0

    def display_board(self):
        """
        Displays the board in a user-friendly format
        """
        player_1_pits = self.board[self.p1_pits_index[0]: self.p1_pits_index[1] + 1]
        player_1_mancala = self.board[self.p1_mancala_index]
        player_2_pits = self.board[self.p2_pits_index[0]: self.p2_pits_index[1] + 1]
        player_2_mancala = self.board[self.p2_mancala_index]

        print('P1               P2')
        print('     ____{}____     '.format(player_2_mancala))
        for i in range(self.pits_per_player):
            if i == self.pits_per_player - 1:
                print('{} -> |_{}_|_{}_| <- {}'.format(i + 1, player_1_pits[i],
                                                       player_2_pits[-(i + 1)], self.pits_per_player - i))
            else:
                print('{} -> | {} | {} | <- {}'.format(i + 1, player_1_pits[i],
                                                       player_2_pits[-(i + 1)], self.pits_per_player - i))

        print('         {}         '.format(player_1_mancala))
        turn = 'P1' if self.current_player == 1 else 'P2'
        print('Turn: ' + turn)

    def valid_move(self, pit):
        """
        Function to check if the pit chosen by the current_player is a valid move.
        """

        # write your code here
        if self.pits_per_player < pit or pit < 1:
            print("Pit chosen is not within bounds of possible pits to choose")
            return False

        if self.current_player == 1:
            pit_index = self.p1_pits_index[0] + (pit - 1)
            if self.board[pit_index] == 0:
                print("INVALID MOVE")
                return False
        else:
            pit_index = self.p2_pits_index[0] + (pit - 1)
            if self.board[pit_index] == 0:
                print("INVALID MOVE")
                return False
        # pass
        return True

    def random_move_generator(self):
        """
        Function to generate random valid moves with non-empty pits for the random player
        """

        # write your code here
        available_nonempty_pits = []

        if self.current_player == 1:
            for pit in range(1, self.pits_per_player + 1):
                if self.board[pit - 1] > 0:
                    available_nonempty_pits.append(pit)
        else:
            for pit in range(1, self.pits_per_player + 1):
                index = self.p2_pits_index[0] + (pit - 1)
                if self.board[index] > 0:
                    available_nonempty_pits.append(pit)
        if available_nonempty_pits:
            return random.choice(available_nonempty_pits)
        else:
            return None

    def play(self, pit):
        """
        This function simulates a single move made by a specific player using their selected pit. It primarily performs three tasks:
        1. It checks if the chosen pit is a valid move for the current player. If not, it prints "INVALID MOVE" and takes no action.
        2. It verifies if the game board has already reached a winning state. If so, it prints "GAME OVER" and takes no further action.
        3. After passing the above two checks, it proceeds to distribute the stones according to the specified Mancala rules.

        Finally, the function then switches the current player, allowing the other player to take their turn.
        """
        if self.isGameOver():
            print("GAME OVER")

        if not self.valid_move(pit):
            return self.board
            print("INVALID MOVE")

        if self.current_player == 1:
            index = self.p1_pits_index[0] + (pit - 1)
            curr_mancala_index = self.p1_mancala_index
            other_mancala_index = self.p2_mancala_index
            own_pits_range = range(self.p1_pits_index[0], self.p1_pits_index[1] + 1)
        else:
            index = self.p2_pits_index[0] + (pit - 1)
            curr_mancala_index = self.p2_mancala_index
            other_mancala_index = self.p1_mancala_index
            own_pits_range = range(self.p2_pits_index[0], self.p2_pits_index[1] + 1)

        stones_at_index = self.board[index]
        self.board[index] = 0
        curr = index
        # distributing the stones at the chosen pit
        while stones_at_index > 0:
            curr = (curr + 1) % len(self.board)
            if curr == other_mancala_index:
                continue
            stones_at_index -= 1
            self.board[curr] += 1
        # check if one of stones you distribute ended up alone on your side
        if curr in own_pits_range and self.board[curr] == 1:
            opposite_side = (len(self.board) - 2) - curr
            if self.board[opposite_side] > 0:
                captured_stones = self.board[opposite_side] + self.board[curr]
                self.board[curr_mancala_index] += captured_stones
                self.board[curr] = 0
                self.board[opposite_side] = 0
        self.moves.append((self.current_player, pit))

        if self.isGameOver():
            self.winning_eval()
            return self.board

        # plauyer switch
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

        return self.board

    def isGameOver(self):
        p1_empty = sum(self.board[self.p1_pits_index[0]: self.p1_pits_index[1] + 1]) == 0
        p2_empty = sum(self.board[self.p2_pits_index[0]: self.p2_pits_index[1] + 1]) == 0
        return p1_empty or p2_empty

    def winning_eval(self):
        """
        Function to verify if the game board has reached the winning state.
        Hint: If either of the players' pits are all empty, then it is considered a winning state.
        """
        if self.isGameOver():

            for i in range(self.p1_pits_index[0], self.p1_pits_index[1] + 1):
                self.board[self.p1_mancala_index] += self.board[i]
                self.board[i] = 0

            for i in range(self.p2_pits_index[0], self.p2_pits_index[1] + 1):
                self.board[self.p2_mancala_index] += self.board[i]
                self.board[i] = 0

            player1_score = self.board[self.p1_mancala_index]
            player2_score = self.board[self.p2_mancala_index]
            if player1_score > player2_score:
                print("Player 1 won")
            elif player2_score > player1_score:
                print("Player 2 won")
            else:
                print("Both players have the same amount of stones, tie.")
            return True

        return None

        # write your code here
        pass