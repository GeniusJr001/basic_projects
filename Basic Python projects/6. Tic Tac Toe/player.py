import math
import random

class Player:
    #initializing the letters the player is going to use
    def __init__(self, letter):
        #the letter we want to use is only x and o
        self.letter = letter
        
    #all players should be able to play their next move
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    #initializing the super class
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        #This is to get a random spot when playing
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter+ "\'s turn. Input move 0-9: ")
            #we are going to check if the value is correct
            #  if it is an integer 
            # if the spot is available on the board
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again!")
                
        return val
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #randomly choose a move
        else:
            #using a minimax algorithm to find the next position to play to
            square = self.minimax(game, self.letter)["position"]
            return square
        #defining the minimax algorithm
    def minimax(self, state, player):
        max_player = self.letter #yourself
        other_player = "O" if player == "X" else "X"
            
        if state.current_winner == other_player:
            return {"position": None,
                    "score": 1*(state.num_empty_squares()+1) if other_player == max_player else -1 * (state.num_empty_squares()+1)
                    }
        #defining a full game that can no longer take in any values   
        elif not state.empty_squares():
            return {"postion": None, "score": 0}
        if player == max_player:
            best ={"position": None, "score": -math.inf} #This allows each score to maximize the larger
        else:
            best ={"position": None, "score": math.inf}
                
        for possible_move in state.available_moves():
                # step 1: make a move and try the spot
            state.make_move(possible_move, player)
                # step 2: recurse using minimax algorithm to simulate a game after making that move
            sim_score = self.minimax(state, other_player) #alternating players
                # step 3 undo the move
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move
                # step 4: update the dictionaries when needed
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score #replace list 
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score #replace list
        return best
        