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
        self.board = [
            [State() for _ in range(col_size)] for _ in range(row_size)
        ]

    def validate_location(self, row, col):
        if row > self.row_size or col > self.col_size:
            raise IndexError(f"Index Error, {row}, {col} out of bounds")

    def add_target(self, row, col):
        self.validate_location(row, col)
        self.board[row][col].make_target()

    def add_start(self, row, col):
        self.validate_location(row, col)
        self.board[row][col].make_start()

    def add_wall(self, row, col):
        self.validate_location(row, col)
        self.board[row][col].make_searched()

    def __str__(self):
        string_board = ""
        for row in self.board:
            row_string = "".join(str(col) for col in row)
            string_board += f"{row_string}\n"
        return string_board


class State:
    """
    class represents the states on the board.
    The States are:
    - start
    - searched
    - searching
    - target
    ...
    Attributes
    ----------
    seached : bol
        It has been searched and can no longer be searched
    seaching : bol
        Where the search wil expand from
    target : bol
        The search ends once the target is reached
    . . .
    Methods
    -------
    make_start()
        Sets start to true.

    make_searched()
        Sets searched to true.

    make_searching()
        Sets searching to true.

    make_target()
        Sets target to true and not_searched to true.
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
        self.searched = True

    def gameover(self):
        return self.target and self.searched

    def __str__(self):
        if self.target == True:
            return "F"
        elif self.start == True:
            return "S"
        elif self.searched == True:
            return "x"
        elif self.searching == True:
            return "X"
        else:
            return "O"


def deapth_first_search(board: Board, startx, starty):

    visited = [[startx, starty]]
    queue = []
    queue.extend(neighbors(board, startx, starty))

    while queue:
        board.board[queue[0][0]][queue[0][1]].make_searched()
        print(board)
        if board.board[queue[0][0]][queue[0][1]].gameover():
            break
        else:
            print(queue)
            visited.append(queue[0])
            queue.extend(neighbors(board, queue[0][0], queue[0][1]))
            queue = list({tuple(k): None for k in queue})
            queue.pop(0)


def neighbors(board: Board, row, col):
    neighbors = []
    if row + 1 < board.row_size:
        if not board.board[row + 1][col].searched:
            print()
            neighbors.append([row + 1, col])
    if col + 1 < board.col_size:
        if not board.board[row][col + 1].searched:
            neighbors.append([row, col + 1])
    if row - 1 > board.row_size:
        if not board.board[row - 1][col].searched:
            neighbors.append([row - 1, col])
    if col - 1 > board.col_size:
        if not board.board[row][col - 1].searched:
            neighbors.append(board.board[row, col - 1])
    return neighbors


def main():
    board = Board(10, 10)
    board.add_start(0, 0)
    board.add_target(4, 5)
    print(board)
    deapth_first_search(board, 0, 0)


if __name__ == "__main__":
    main()
