import board as board_code

class Controller:
    """
    Class represents the controller for the path finding code.
    ...
    Attributes
    ----------
    algorithms : Dictionary
        a dictionary that correlates the name of an algorithm to its function object
    board : Board
        the board
    start_row : int
        the Y index of the starting point for the algorithm
    start_col : int
        the X index of the starting point for the algorithm
    end_row : int
        the Y index of the ending point for the algorithm
    end_col : int
        the X index of the ending point for the algorithm
    ...
    Methods
    -------
    run()
        Runs the provided algorithm on the provided board.
        throws error:
            - if the board is null
            - if the algorithm name does not exist in the dictionary
    """

    def __init__(self, board, start_row, start_col, end_row, end_col):
        self.board = board
        self.board.add_start(start_row, start_col)
        self.board.add_target(end_row, end_col)
        self.algorithms = {"deapth_first" : board_code.deapth_first_search, "test" : self.test }

    def test(self, board : board_code.Board, start_row : int, start_col : int):
        print("Great\n")

    def run(self, algo):
        self.algorithms[algo](self.board, 0, 0)

if (__name__ == "__main__"):
    print("make controller\n")
    controller = Controller(board_code.Board(4, 3), 0, 0, 2, 2)
    print("run controller\n")
    controller.run("test")
    controller.run("deapth_first")