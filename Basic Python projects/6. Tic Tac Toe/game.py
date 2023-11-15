from player import HumanPlayer, GeniusComputerPlayer, RandomComputerPlayer
# Creating a class for tictactoe(This carries the structure of the board the moves available to all players)
class TicTactoe:
    #initialising the class (this takes in the size of the board and keeps track of the winner)
    def __init__(self):
        self.board = [" " for i in range(9)] # a list to represent a 3*3 board
        self.current_winner = None #keep track of winner
    #telling the row and the column in the board
    def print_board(self):
        #this gets the row
        for row in [self.board[i*3:((i+1)*3)] for i in range(3)]:
            print("| "+ " | ".join(row) + " |")
    # assigning a value to the board to know where to play next(@staticmethod)
    @staticmethod
    def print_board_num():
        # 0|1|2 This just tells which no correspond to each board
        number_board = [[str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| "+ " | ".join(row) + " |")
    # defining the moves available to the player        
    def available_moves(self):
        moves = []
        #"""This assigns tuples(i.e the sequence of the objects) like given a numerical value to each postion of the board"""
        for (i, spot) in enumerate(self.board):    #["x", "x", "o"] -> [(0, "x"),(1, "x"),[2, "o"]]
            if spot == " ":
                moves.append(i)
        return moves
    #defining the empty spaces yet to be played
    def empty_squares(self):
        return " " in self.board
    #defining no of empty spaces
    def num_empty_squares(self):
        return len(self.available_moves())
    #definig a make move function
    def make_move(self, square, letter):
        #if valid move then we want to make move assigned to letter
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False #Instead of using an else condition before it it can be witten like this
    #defining a function to check for the winner
    def winner(self, square, letter):
        #checking the row for a three in a row win
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        #checking the column for a three in a row win
        col_ind = square % 3
        column = [self.board[col_ind +i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        #checking diagonals
        # note the only possible diagonals are 0,2,4,6,8
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
#defining a play function(for we to know where to play next)
def play(game, x_player, o_player, print_game=True):
    #return the winner if there is
    if print_game:
        game.print_board_num()
        
    letter = "X" #starting letter
    # iterate while the game still has empty squares(i.e continue in the loop until all the board is filled)
    while game.empty_squares():
        # get move from appropriate player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        #defining a function that makes a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f"makes a move to square {square}")
                game.print_board()
                print(" ") #printing just an empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + " You won!!")
                return letter
        #after we've made our move we need to alternate letters
        letter = "O" if letter =="X" else "X"
    if print_game:
        print("It's a tie")

if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTactoe()
    play(t, x_player, o_player, print_game=True)