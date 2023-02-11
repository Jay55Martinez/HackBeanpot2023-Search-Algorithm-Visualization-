class Board:
    """
    Class represents the grid where the search algorithm will take place.
    The board will be a 2d list and each element in the list wil be a State 
    object.
    ...
    Attributes
    ----------
    column_size : int
        the size of the board x
    row_size : int
        the size of the board y
    board : 2d list
        A 2d list of States
    ...
    Methods
    -------
    add_target(row, col)
        adds the target cell to the board at the specified cords.
        throws error:
            - if the cords are larger than the boards dims
            - if there already is a target on the board
        
    add_start(row, col)
        adds the starting cell to the board at the specified cords.
        throws error:
            - if the cords are larger than the boards dims
            - if there already is a start on the board
    
    add_wall(row, col)
        adds a wall to the board at the specified cords.
        throws error:
            - if the cords are larger than the boards dims
            - if the specified cell contains a State that is not not searched
    """
    
    def __init__(self, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size
        self.board = [[State() for _ in range(col_size)]
                      for _ in range(row_size)
                      ]
        
    def add_target(self, row, col):
        if row > self.row_size or col > self.col_size:
            raise IndexError("target Index Error")
        self.board[row][col].make_target()
    
    def add_start(self, row, col):
        if row > self.row_size or col > self.col_size:
            raise IndexError("target Index Error")
        self.board[row][col].make_start()
        
    def add_wall(self, row, col):
        if row > self.row_size or col > self.col_size:
            raise IndexError("target Index Error")
        self.board[row][col].make_searched()
    
    def __str__(self):
        string_board = ''
        for row in range(self.row_size):
            for col in range(self.col_size):
                string_board += str(self.board[row][col])
            string_board += '\n'
        return f'' + string_board
                
class State:
    """
    class represents the states on the board.
    The States are:
    - not_searched
    - searched
    - searching
    - target
    ...
    Attributes
    ----------
    not_searched : bol
        It can be searched by a searching cell
    seached : bol
        It has been searched and can no longer be searched
    seaching : bol
        Where the search wil expand from
    target : bol
        The search ends once the target is reached
    . . .
    Methods
    -------
    make_not_searched()
        Sets not_searched to true.
        throws error:
            - if searched is true
            
    make_searched()
        Sets searched to true.
        
    make_searching()
        Sets searching to true.
    
    make_target()
        Sets target to true and not_searched to true.
        throws error:
            - if searched or searching is true
    """
    
    def __init__(self):
        self.searched = False
        self.searching = False
        self.target = False
        self.start = False
    
    def make_searched(self):
        self.searched = True
    
    def make_searching(self):
        self.searching = True
        self.searched = True
    
    def make_target(self):
        self.target = True
        
    def make_start(self):
        self.start = True
    
    def __str__(self):
        if self.target == True:
            return f'F'
        elif self.start == True:
            return f'S'
        elif self.searched == True:
            return f'x'
        elif self.searching == True:
            return f'X'
        else:
            return f'O'

def main():
    board = Board(10, 10)
    board.add_start(0, 0)
    board.add_target(9, 9)
    print(board)

if __name__ == "__main__":
    main()