"""
🎮 Mancala Game - Python Project

This script implements the classic board game Mancala, featuring two modes:
- A simplified board (3 pits, 2 stones) for basic mechanics testing.
- A full board mode (6 pits, 4 stones) where the player faces a random-move opponent.

Includes:
- Full game logic (distribution, skipping opponent's mancala, capturing)
- Input validation and display updates after each move
- Random opponent mode for gameplay testing

Ideal for learning game simulations and turn-based logic in Python.
"""

#!/usr/bin/env python
# coding: utf-8


# ** RULES **
# 
#   - Players sit on opposite sides of the long edge of the board
#   - There are 6 small pits in the middle of the board and 2 large ones at each end.  The small ones in the middle and the large pit on your right are yours.  The small ones on the other side and the large pit to your opponent's right are theirs
#   - The large pits at the end of the board are called Mancalas
#   - Set up the board with 4 stones per small pit (none in the mancalas)
#   - On every turn, select a pit on your side of the board that contains one or more stones,  then distribute its stones, one stone per pit, in an counter-clockwise direction until you have no stones remaining
#   - If you encounter your opponent's mandala, skip it
#   - If you encounter your mancala, drop a stone into it
#   - If the last stone lands in an empty pit on your side of the board, capture this stone and any stones in your opponent's pit on the other side of the board, collect all of these stones, including the one that just landed, and place them into your mancala.
#   - The player who still has stones on his side of the board when the game concludes places all of these pieces into their mancala.
#   - The player with the most stones in their mancala is declared the winner. If both players have an equal number of stones in their mancala, the game results in a tie.



import random
random.seed(109)




class Mancala:
    # Game's States
    RUNNING = 0
    INVALID_MOVE = 1
    GAME_OVER =  2

    def __init__(self, pits_per_player=6, stones_per_pit = 4):
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
        self.board = [stones_per_pit] * ((pits_per_player+1) * 2)  # Initialize each pit with stones_per_pit number of stones
        self.players = 2
        self.current_player = 1
        self.moves = []
        self.p1_pits_index = [0, self.pits_per_player-1]
        self.p1_mancala_index = self.pits_per_player
        self.p2_pits_index = [self.pits_per_player+1, len(self.board)-1-1]
        self.p2_mancala_index = len(self.board)-1

        # Zeroing the Mancala for both players
        self.board[self.p1_mancala_index] = 0
        self.board[self.p2_mancala_index] = 0

        self.state = Mancala.RUNNING

    def display_board(self):
        """
        Displays the board in a user-friendly format
        """
        player_1_pits = self.board[self.p1_pits_index[0]: self.p1_pits_index[1]+1]
        player_1_mancala = self.board[self.p1_mancala_index]
        player_2_pits = self.board[self.p2_pits_index[0]: self.p2_pits_index[1]+1]
        player_2_mancala = self.board[self.p2_mancala_index]

        print('P1               P2')
        print('     ____{}____     '.format(player_2_mancala))
        for i in range(self.pits_per_player):
            if i == self.pits_per_player - 1:
                print('{} -> |_{}_|_{}_| <- {}'.format(i+1, player_1_pits[i],
                        player_2_pits[-(i+1)], self.pits_per_player - i))
            else:
                print('{} -> | {} | {} | <- {}'.format(i+1, player_1_pits[i],
                        player_2_pits[-(i+1)], self.pits_per_player - i))

        print('         {}         '.format(player_1_mancala))
        turn = 'P1' if self.current_player == 1 else 'P2'
        print('Turn: ' + turn)

    def get_pit_index(self, pit):
        """
        Function to convert player's pit to the pit index in the game board array

            P1      [7]       P2
                 ---------
        [0] 1 -> | 0 | 0 | <- 3 [6]
        [1] 2 -> | 0 | 0 | <- 2 [5]
        [2] 3 -> | 0 | 0 | <- 1 [4]
                 ---------
                    [3]
        """

        if self.current_player == 2:
            pit_index = pit + self.pits_per_player
        else:
            pit_index = pit - 1

        return pit_index

    def valid_move(self, pit):
        """
        Function to check if the pit chosen by the current_player is a valid move.
        """
        pit_index = self.get_pit_index(pit)

        # Determine the valid pit range for the current player
        valid_pits_range = self.p1_pits_index if self.current_player == 1 else self.p2_pits_index

        # Check if the pit has stones and is within the current player's valid pit range
        if self.board[pit_index] > 0 and valid_pits_range[0] <= pit_index <= valid_pits_range[1]:
            self.moves.append((self.current_player, pit))
            return True

        return False

    def random_move_generator(self):
        """
        Function to generate random valid moves with non-empty pits for the random player
        """
        valid_pits_range = self.p1_pits_index if self.current_player == 1 else self.p2_pits_index

        valid_pits = []
        for i in range(valid_pits_range[0], valid_pits_range[1] + 1):
            if self.board[i] > 0:
                valid_pits.append(i)

        move = random.choice(valid_pits)

        # Re-adjust index based on current player
        move = move + 1 if self.current_player == 1 else move - self.pits_per_player

        return move

    def play(self, pit):
        """
        This function simulates a single move made by a specific player using their selected pit. It primarily performs three tasks:
        1. It checks if the chosen pit is a valid move for the current player. If not, it prints "INVALID MOVE" and takes no action.
        2. It verifies if the game board has already reached a winning state. If so, it prints "GAME OVER" and takes no further action.
        3. After passing the above two checks, it proceeds to distribute the stones according to the specified Mancala rules.

        Finally, the function then switches the current player, allowing the other player to take their turn.
        """
        print(f"Player {self.current_player} chose pit: {pit}")

        if not self.valid_move(pit):
            self.state = Mancala.INVALID_MOVE
            print("INVALID MOVE\n")
            return self.state
        print()

        self.state = Mancala.RUNNING

        """
        - On every turn, select a pit on your side of the board that contains one or more stones, then distribute its stones, one stone per pit, in an counter-clockwise direction until you have no stones remaining
        - If you encounter your opponent's mandala, skip it
        - If you encounter your mancala, drop a stone into it
        - If the last stone lands in an empty pit on your side of the board, capture this stone and any stones in your opponent's pit on the other side of the board, collect all of these stones, including the one that just landed, and place them into your mancala.
        """
        pit_index = self.get_pit_index(pit)

        stones_to_distribute = self.board[pit_index]
        self.board[pit_index] = 0

        # Determine opponent's mancala index so we can skip over during the stone distribution
        opponent_mancala_index = self.p2_mancala_index if self.current_player == 1 else self.p1_mancala_index

        next_pit = (pit_index + 1) % len(self.board)
        last_pit = None

        # Distribute stones
        while stones_to_distribute > 0:
            if next_pit != opponent_mancala_index:
                self.board[next_pit] += 1
                stones_to_distribute -= 1
                last_pit = next_pit

            next_pit = (next_pit + 1) % len(self.board)

        # Check for capture: if the last stone landed in an empty pit on the current player's side
        if last_pit is not None and self.board[last_pit] == 1:
            # Set player's pit range and mancala index
            if self.current_player == 1:
                player_pits_range, player_mancala_index = self.p1_pits_index, self.p1_mancala_index
            else:
                player_pits_range, player_mancala_index = self.p2_pits_index, self.p2_mancala_index

            if player_pits_range[0] <= last_pit <= player_pits_range[1]:
                opposite_pit = self.pits_per_player * 2 - last_pit
                captured = self.board[last_pit] + self.board[opposite_pit]
                self.board[player_mancala_index] += captured
                self.board[last_pit] = 0
                self.board[opposite_pit] = 0

        self.current_player = self.current_player % self.players + 1

        # Check winning here since the stones should be distributed for the last move so that we can calculate final scores correctly
        if self.winning_eval():
            self.state = Mancala.GAME_OVER

        return self.state

    def winning_eval(self):
        """
        Function to verify if the game board has reached the winning state.
        Hint: If either of the players' pits are all empty, then it is considered a winning state.
        """
        # Sum the stones in the pits for each player
        p1_stone_count = sum(self.board[self.p1_pits_index[0]:self.p1_pits_index[1] + 1])
        p2_stone_count = sum(self.board[self.p2_pits_index[0]:self.p2_pits_index[1] + 1])

        # Check if the game ends
        if p1_stone_count == 0 or p2_stone_count == 0:
            print("GAME OVER\n")

            p1_total_stones = p1_stone_count + self.board[self.p1_mancala_index]
            p2_total_stones = p2_stone_count + self.board[self.p2_mancala_index]

            print(f"Player 1 total stones is {p1_total_stones}.")
            print(f"Player 2 total stones is {p2_total_stones}.")

            if p1_total_stones > p2_total_stones:
                print(f"PLAYER 1 WON!\n")
            elif p2_total_stones > p1_total_stones:
                print(f"PLAYER 2 WON!\n")
            else:
                print("Tie!")

            # Update final board
            for i in range(len(self.board)):
                self.board[i] = 0
            self.board[self.p1_mancala_index] = p1_total_stones
            self.board[self.p2_mancala_index] = p2_total_stones

            return True

        return False




# Mancala part 1 
game = Mancala(pits_per_player = 3, stones_per_pit = 2)
print(game.board)
game.display_board()

# Player 1 selects pit 1 (1-based index)
game.play(1)
game.display_board()

# Player 2 selects pit 2
game.play(2)
game.display_board()

# Player 1 selects pit 3
game.play(3)
game.display_board()

# Player 2 selects pit 2
game.play(2)
game.display_board()

# Player 1 selects pit 1
game.play(1)
game.display_board()

# Printing the list of moves
print("\nList of valid moves:")
for move in game.moves:
    player, pit = move
    print(f"Player {player} selected pit {pit}")



# Mancala part 2
random.seed(109) # I had to add this bcs for some reason it wasn't registering it from the previous cell
game = Mancala(pits_per_player = 6, stones_per_pit = 4)
game.display_board()

human_moves = [6,5,4,3,2]

for human_move in human_moves:
    game.play(human_move)
    game.display_board()

    game.play(game.random_move_generator())
    game.display_board()

# Printing the list of moves
print("\nList of valid moves:")
for move in game.moves:
    player, pit = move
    print(f"Player {player} selected pit {pit}")