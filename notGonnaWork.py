import tkinter as tk


class BlockPlacer:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=500, height=500, bg='black')
        self.canvas.pack()
        self.blocks = []
        self.flags = []
        self.placing_block = False
        self.placing_flag = False
        self.selected_item = None
        self.place_block_button = tk.Button(root, text='Place Block', command=self.start_placing_block)
        self.place_block_button.pack()
        self.place_flag_button = tk.Button(root, text='Place Flag', command=self.start_placing_flag)
        self.place_flag_button.pack()
        self.delete_block_button = tk.Button(root, text='Delete Block', command=self.delete_block)
        self.delete_block_button.pack()
        self.canvas.bind('<Button-1>', self.place_object)
        self.grid_size = 50
        self.grid_spacing = 50
        self.draw_grid()

    def start_placing_block(self):
        self.placing_block = True
        self.placing_flag = False

    def start_placing_flag(self):
        self.placing_flag = True
        self.placing_block = False

    def place_object(self, event):

        if self.placing_block:
            x, y = self.get_grid_coordinates(event.x, event.y)
            self.blocks.append(self.canvas.create_rectangle(x, y, x + self.grid_size, y + self.grid_size, fill='white'))
            self.placing_block = False
        elif self.placing_flag:
            if len(self.flags) >= 2:
                self.canvas.delete(self.flags.pop(0))
            x, y = self.get_grid_coordinates(event.x, event.y)
            self.flags.append(self.canvas.create_oval(x + self.grid_size / 2 - 10, y + self.grid_size / 2 - 10,
                                                      x + self.grid_size / 2 + 10, y + self.grid_size / 2 + 10,
                                                      fill='red'))
            self.placing_flag = False
        else:
            self.selected_item = self.canvas.find_closest(event.x, event.y)[0]

    def delete_block(self):
        if self.selected_item is not None and self.selected_item in self.blocks:
            self.canvas.delete(self.selected_item)
            self.blocks.remove(self.selected_item)
            self.selected_item = None

    def draw_grid(self):
        for i in range(0, 500, self.grid_spacing):
            self.canvas.create_line(i, 0, i, 500, fill='white')
            self.canvas.create_line(0, i, 500, i, fill='white')

    def get_grid_coordinates(self, x, y):
        return (self.grid_spacing * int(x / self.grid_spacing)), (self.grid_spacing * int(y / self.grid_spacing))


root = tk.Tk()
app = BlockPlacer(root)
root.mainloop()
