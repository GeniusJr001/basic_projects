import random
#creating a board object to represent the minesweeper game
class Board:
    #dim_size is dimension size
    #num_bombs is number of bombs
    def __init__(self, dim_size,num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.assign_values_to_board()
        #create a board
        self.board = self.make_new_board()
        #initialise a set to keep track of locations uncovered
        #we'll save (row, col) tuples(i.e the index they represent) into the set
        self.dug = set()
    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)] #this creates an array for the board structure
        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            #loc is location
            loc = random(0,self.dim_size**2 -1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == "*":
                #this means means we've already planted a bomb there
                continue 
            board[row][col] = "*" #plant the bomb if not
            bombs_planted += 1
        return board
    def assign_values_to_board(self):
        for r in range (self.dim_size):
            for c in range (self.dim_size):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.get_num_neighbouring_bombs[r][c]
                
    def get_num_neighbouring_bombs(self, row, col):
        num_neighbouring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1) + 1): #setting upper and lower bound
            for c in range(max(0, col-1), min(self.dim_size-1, col+1) + 1):
                if r == row and c == col:
                    #original location
                    continue
                if self.board[r][c] == "*":
                    num_neighbouring_bombs += 1
        return num_neighbouring_bombs
    def dig(self, row, col):
        self.dug.add((row, col)) #keep track of where as been dug
        if self.board[row][col] == "*":
            return False
        elif self.board[row][col] > 0:
            return True
        for r in range(max(0, row-1), min(self.dim_size-1, row+1) + 1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1) + 1):
                if (r, c) in self.dug:
                    continue #dont dig here (because it has already been dug)
                self.dig(r, c)
        return True
    def __str__(self): #This function allows the output to print what this object returns
        #first a new array visible to the user
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "
#defining a play function
def play(dim_size=10, num_bombs=10):
    #step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)
    #step 2: show the user the board and ask where they want to dig
    #step 3a: if location is a bomb show the game over message
    #      b: if location is not a bomb then we dig recursively until each square is at least next to a bomb
    #step 4: repeat steps 2 and 3 until there are no more places to dig ->VICTORY
    pass