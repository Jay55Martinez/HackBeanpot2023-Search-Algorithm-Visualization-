import tkinter as tk
from board import Board, breath_first_search


class BlockPlacer:
    def __init__(self, root):
        self.root = root
        self.grid_dimension = 10
        self.grid_size = 50
        self.grid_spacing = self.grid_size
        actual_height = self.grid_size * self.grid_dimension
        self.canvas = tk.Canvas(
            root, width=actual_height, height=actual_height, bg="black"
        )
        self.canvas.pack()
        self.blocks = []
        self.block_locs = []
        self.start_flags = []
        self.end_flags = []
        self.set_zero_states()
        self.selected_item = None
        self.place_start_flag_button = tk.Button(
            root,
            text="Place Start Flag",
            command=self.start_placing_start_flag,
        )
        self.start_loc = None
        self.end_loc = None
        self.place_start_flag_button.pack()
        self.place_end_flag_button = tk.Button(
            root,
            text="Place End Flag",
            command=self.start_placing_end_flag,
        )
        self.place_end_flag_button.pack()
        self.place_block_button = tk.Button(
            root, text="Place Block", command=self.start_placing_block
        )
        self.place_block_button.pack()
        self.to_delete = []

        # self.delete_block_button = tk.Button(
        #     root, text="Delete Block", command=self.delete_block
        # )
        # self.delete_block_button.pack()
        self.canvas.bind("<Button-1>", self.place_object)
        self.draw_grid()
        self.label = tk.Label(root, text="")
        # this creates a new label to the GUI
        self.label.pack()
        self.run = tk.Button(
            root,
            text="Run path finding algorithm",
            command=self.run,
        )
        self.run.pack()
        self.reset = tk.Button(
            root,
            text="Reset",
            command=self.reset,
        )
        self.reset.pack()

    def set_zero_states(self):
        self.placing_block = False
        self.placing_start_flag = False
        self.placing_end_flag = False

    def start_placing_end_flag(self):
        new_state = not self.placing_end_flag
        self.set_zero_states()
        self.placing_end_flag = new_state
        if self.placing_end_flag:
            self.label["text"] = "Place End Flag Now"
        else:
            self.label["text"] = "Cleared"

    def start_placing_block(self):
        new_state = not self.placing_block
        self.set_zero_states()
        self.placing_block = new_state
        if self.placing_block:
            self.label["text"] = "Place Block Now"
        else:
            self.label["text"] = "Cleared"

    def start_placing_start_flag(self):
        new_state = not self.placing_start_flag
        self.set_zero_states()
        self.placing_start_flag = new_state
        if self.placing_start_flag:
            self.label["text"] = "Place Start Flag Now"
        else:
            self.label["text"] = "Cleared"

    def place_object(self, event):

        if self.placing_block:
            x, y = self.get_grid_coordinates(event.x, event.y)
            print("location is", x, y)
            self.block_locs.append((x, y))
            self.blocks.append(
                self.canvas.create_rectangle(
                    x, y, x + self.grid_size, y + self.grid_size, fill="white"
                )
            )
            # self.placing_block = False
        elif self.placing_start_flag:
            if len(self.start_flags) >= 1:
                self.canvas.delete(self.start_flags.pop(0))
            x, y = self.get_grid_coordinates(event.x, event.y)
            self.start_loc = x, y
            self.start_flags.append(self.create_oval(x, y, "red"))
            # self.placing_start_flag = False
        elif self.placing_end_flag:
            if len(self.end_flags) >= 1:
                self.canvas.delete(self.end_flags.pop(0))
            x, y = self.get_grid_coordinates(event.x, event.y)
            self.end_loc = x, y
            self.end_flags.append(self.create_oval(x, y, "Blue"))

            # self.placing_start_flag = False
        else:
            self.selected_item = self.canvas.find_closest(event.x, event.y)[0]

    # def delete_block(self):
    #     if (
    #         self.selected_item is not None
    #         and self.selected_item in self.blocks
    #     ):
    #         self.canvas.delete(self.selected_item)
    #         self.blocks.remove(self.selected_item)
    #         self.selected_item = None

    def draw_grid(self):
        for i in range(0, 500, self.grid_spacing):
            self.canvas.create_line(i, 0, i, 500, fill="white")
            self.canvas.create_line(0, i, 500, i, fill="white")

    def get_grid_coordinates(self, x, y):
        return (self.grid_spacing * int(x / self.grid_spacing)), (
            self.grid_spacing * int(y / self.grid_spacing)
        )

    def create_oval(self, x, y, fill):
        var = self.canvas.create_oval(
            x + self.grid_size / 2 - 10,
            y + self.grid_size / 2 - 10,
            x + self.grid_size / 2 + 10,
            y + self.grid_size / 2 + 10,
            fill=fill,
        )
        return var

    def reset(self):
        if self.start_flags:
            self.canvas.delete(self.start_flags.pop(0))
        if self.end_flags:
            self.canvas.delete(self.end_flags.pop(0))
        for block in self.blocks:
            self.canvas.delete(block)
        self.blocks = []
        self.block_locs = []
        self.set_zero_states()
        self.start_loc = None
        self.end_loc = None
        for dot in self.to_delete:
            self.canvas.delete(dot)
        self.to_delete = []

    def run(self):
        self.set_zero_states()
        self.label["text"] = "Running"
        print(self.start_loc)
        print(self.end_loc)
        print(self.grid_dimension)
        print(self.grid_spacing)
        board = Board(self.grid_dimension, self.grid_dimension)
        start_x = self.start_loc[0] // self.grid_spacing
        start_y = self.start_loc[1] // self.grid_spacing
        board.add_start((start_x, start_y))
        end_x = self.end_loc[0] // self.grid_spacing
        end_y = self.end_loc[1] // self.grid_spacing
        board.add_target((end_x, end_y))
        block_locs = [
            (loc[0] // self.grid_spacing, loc[1] // self.grid_spacing)
            for loc in self.block_locs
        ]
        for block_loc in block_locs:
            board.add_wall(block_loc)
        found_path, search_list = breath_first_search(
            board, (start_x, start_y)
        )
        print(found_path)
        print(search_list)
        for x, y in search_list[1:-1]:
            root.tksleep(150)
            grid_x = x * self.grid_spacing
            grid_y = y * self.grid_spacing
            self.to_delete.append(self.create_oval(grid_x, grid_y, "yellow"))
            self.label["text"] = f"Searching: {x}, {y}"
        for x, y in found_path[1:-1]:
            root.tksleep(150)
            grid_x = x * self.grid_spacing
            grid_y = y * self.grid_spacing
            self.to_delete.append(self.create_oval(grid_x, grid_y, "green"))
            self.label["text"] = f"Best path length: {len(found_path)}"


def tksleep(self, time: int) -> None:
    """
    Emulating `time.sleep(milliseconds)`
    Created by TheLizzard, inspired by Thingamabobs
    """
    self.after(time, self.quit)
    self.mainloop()


tk.Misc.tksleep = tksleep

# # Example
# root = tk.Tk()
# root.tksleep(2)
root = tk.Tk()
app = BlockPlacer(root)
root.mainloop()
