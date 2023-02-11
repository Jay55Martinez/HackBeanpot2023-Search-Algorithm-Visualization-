import numpy as np

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
        self.board = [[State.notsearched]*col_size]*row_size
        
    def add_target(self, row, col):
        if row > self.row_size or col > self.col_size:
            raise IndexError("target Index Error")
        self.board[row][col] = State.target
    
    def add_start(self, row, col):
        if row > self.row_size or col > self.col_size:
            raise IndexError("target Index Error")
        self.board[row][col] = State.searching
        
    def add_wall(self, row, col):
        if row > self.row_size or col > self.col_size:
            raise IndexError("target Index Error")
        self.board[row][col] = State.searched
    
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
            - if any searched is true
    """
    def __init__(self):
        self.not_searched = False
        self.searched = False
        self.searching = False
        self.target = False
    
    def make_not_searched(self):
        if self.searched == True:
            raise ReferenceError('trying to make a searched State not searched')
        self.not_searched = True
    
    def make_searched(self):
        self.searched = True
    
    def make_searching(self):
        self.searching = True
    
    def make_target(self):
        self.target = True