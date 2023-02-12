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
            - if there already is a start on the board

    validate_location(row, col)
        Returns true if the given cords are in the array false otherwise
    """

    def __init__(self, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size
        self.board = [
            [State() for _ in range(col_size)] for _ in range(row_size)
        ]

    def validate_location(self, coord):
        row, col = coord
        if (
            0 <= row
            and row < self.row_size
            and 0 <= col
            and col < self.col_size
        ):
            if not self.board[row][col].searched:
                return True
        else:
            return False

    def add_target(self, coord):
        row, col = coord
        if not self.validate_location(coord):
            raise IndexError("cords out of bounds")
        self.board[row][col].make_target()

    def add_start(self, coord):
        row, col = coord
        if not self.validate_location(coord):
            raise IndexError("cords out of bounds")
        self.board[row][col].make_start()

    def add_wall(self, coord):
        row, col = coord
        if not self.validate_location(coord):
            raise IndexError("cords out of bounds")
        self.board[row][col].make_wall()

    def add_path(self, path):
        for coord in path:
            row, col = coord
            self.board[row][col].make_path()

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
    - wall
    - path
    - target
    ...
    Attributes
    ----------
    searched : bol
        It has been searched and can no longer be searched
    start : bol
        Where the algorithm will start from
    target : bol
        The search ends once the target is reached
    wall : bol
        Can not be searched
    path : bol
        Path that the algorithm takes
    . . .
    Methods
    -------
    make_start()
        Sets start to true.

    make_searched()
        Sets searched to true.

    make_path()
        Sets path to true.

    make_target()
        Sets target to true and not_searched to true.

    make_wall()
        Sets wall and searched to true.

    gameover()
        returns if the State is target and searched
    """

    def __init__(self):
        self.searched = False
        self.path = False
        self.target = False
        self.start = False
        self.wall = False

    def make_searched(self):
        self.searched = True

    def make_path(self):
        self.path = True
        self.searched = True

    def make_target(self):
        self.target = True

    def make_start(self):
        self.start = True
        self.searched = True

    def make_wall(self):
        self.wall = True
        self.searched = True

    def gameover(self):
        return self.target and self.searched

    def __str__(self):
        if self.target == True:
            return "F"
        elif self.start == True:
            return "S"
        elif self.wall == True:
            return "|"
        elif self.path == True:
            return "-"
        elif self.searched == True:
            return "x"
        else:
            return "O"


# runs breath first search on the specified board given a start location
def breath_first_search(board: Board, starting_node):
    search_list = []
    visited_nodes = set()
    path_sofar = []
    queue = [[starting_node, path_sofar]]

    while queue:
        current_node, path = queue.pop(0)
        search_list.append(current_node)
        path.append(current_node)
        board.board[current_node[0]][current_node[1]].make_searched()
        visited_nodes.add(current_node)

        if board.board[current_node[0]][current_node[1]].gameover():
            board.add_path(path)
            return path, search_list

        current_node_neighbors = neighbors(board, current_node)
        for node in current_node_neighbors:
            if node not in visited_nodes:
                queue.append([node, path.copy()])
                visited_nodes.add(node)
    return None, search_list


# gets the unsearched neighbors adjacent to the specifed cord
def neighbors(board: Board, node):
    row, col = node
    neighbors = []
    coords = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]
    for coord in coords:
        if board.validate_location(coord):
            neighbors.append(coord)

    return neighbors


def depth_first_search(board: Board, starting_node):
    search_list = []
    visited_nodes = set()
    path_sofar = []
    queue = [[starting_node, path_sofar]]

    while queue:
        current_node, path = queue.pop(0)
        path.append(current_node)
        search_list.append(current_node)
        board.board[current_node[0]][current_node[1]].make_searched()
        visited_nodes.add(current_node)

        if board.board[current_node[0]][current_node[1]].gameover():
            board.add_path(path)
            return path, search_list

        current_node_neighbors = neighbors(board, current_node)
        for node in current_node_neighbors:
            if node not in visited_nodes:
                queue.insert(0, [node, path.copy()])
                visited_nodes.add(node)

    return None, search_list


def main():
    board = Board(10, 10)
    board.add_start((0, 0))
    board.add_target((4, 5))
    board.add_wall((0, 1))
    board.add_wall((1, 1))
    breath_first_search(board, (0, 0))
    print(board)
    board2 = Board(10, 10)
    board2.add_start((0, 0))
    board2.add_target((4, 5))
    board2.add_wall((0, 1))
    board2.add_wall((1, 1))
    depth_first_search(board2, (0, 0))

    print(board2)


if __name__ == "__main__":
    main()
