import tkinter as tk


class BlockPlacer:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=500, height=500, bg="black")
        self.canvas.pack()
        self.blocks = []
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

        # self.delete_block_button = tk.Button(
        #     root, text="Delete Block", command=self.delete_block
        # )
        # self.delete_block_button.pack()
        self.canvas.bind("<Button-1>", self.place_object)
        grid_distance = 50
        self.grid_size = grid_distance
        self.grid_spacing = grid_distance
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
            self.start_flags.append(
                self.canvas.create_oval(
                    x + self.grid_size / 2 - 10,
                    y + self.grid_size / 2 - 10,
                    x + self.grid_size / 2 + 10,
                    y + self.grid_size / 2 + 10,
                    fill="red",
                )
            )
            # self.placing_start_flag = False
        elif self.placing_end_flag:
            if len(self.end_flags) >= 1:
                self.canvas.delete(self.end_flags.pop(0))
            x, y = self.get_grid_coordinates(event.x, event.y)
            self.end_loc = x, y
            self.end_flags.append(
                self.canvas.create_oval(
                    x + self.grid_size / 2 - 10,
                    y + self.grid_size / 2 - 10,
                    x + self.grid_size / 2 + 10,
                    y + self.grid_size / 2 + 10,
                    fill="Blue",
                )
            )
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

    def run(self):
        self.set_zero_states()
        self.label["text"] = "Running"
        print(self.start_loc)
        print(self.end_loc)


root = tk.Tk()
app = BlockPlacer(root)
root.mainloop()
