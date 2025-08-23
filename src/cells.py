import tkinter as tk
from tkinter import messagebox

class MainApp(tk.Tk):
    def __init__(self, title, size, num_rows, num_columns):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.label_text = tk.StringVar()
        self.label_text.set("Click any Light Green Cell to Start")
        self.stats = Stats(self, self.label_text)
        self.board = Board(self, num_rows, num_columns)
        self.stats.pack(fill="both", expand=True)
        self.board.pack()
        self.mainloop()

class Stats(tk.Frame):
    def __init__(self, master, label_string_var):
        super().__init__(master)
        self.place(x= 0, y= 0, height= 50)
        self.my_label = tk.Label(self, textvariable=label_string_var, font=("Helvetica", 16, "bold"))
        self.my_label.pack(padx= 20, expand=True, fill= "both", anchor="center")

class Board(tk.Frame):
    def __init__(self, master, num_rows, num_columns):
        super().__init__(master)
        self.master = master # Reference to MainApp
        self.place(x= 0, y= 50)
        self.rows = num_rows
        self.columns = num_columns
        self.high_score = 0
        self.moves = 0
        self.cell_path = []
        self.buttons = {}  # Dictionary to store buttons by (row, column)
        self.data = {}     # Dictionary to store data associated with each cell
        for r in range(self.rows):
            for c in range(self.columns):
                # Create a Button
                button = tk.Button(self, text=f"", borderwidth=1, font=("Helvetica", 16, "bold"),
                                   relief="solid", width=3, height=2, bg="lightgreen")
                button.grid(row=r, column=c, padx=5, pady=5)
                self.buttons[(r, c)] = button
                # [] prev (row, col, num), current (row, col, num) ]
                self.data[(r, c)] = [(0,0,0),(0,0,0)] #(row, col)
                # Bind the button's click event to a callback function
                button.config(command=lambda row=r, col=c: self.button_clicked(row, col))

    def change_label(self):
        self.master.label_text.set(f"Moves made = {self.moves} with High Score = {self.high_score}")

    def button_clicked(self, row, col):
        # Access the data of the clicked button using row and column
        cell_data = self.data[(row, col)]
        cell_button = self.buttons[(row, col)]
        cell_color = cell_button["bg"]
        # if cell is the first one clicked
        if len(self.cell_path) == 0:
            for row1 in range(self.rows):
                for column1 in range(self.columns):
                    if row == row1 and col == column1:
                        # found clicked 
                        pass
                    else:
                        widget = self.grid_slaves(row1, column1)[0]
                        color = widget['bg']
                        if color == "lightgreen":
                         widget.config(bg="lightgray")
            cell_button.config(bg = "pink")
            cell_data[0] = (row, col, 0) # set previous cell data
            cell_data[1] = (row, col, cell_data[0][2] +1) # set current cell data
            self.cell_path.append(cell_data[1])
            self.moves += 1
            if cell_data[1][2] > self.high_score:
                self.high_score = cell_data[1][2]     
            cell_button.config(text = f"{cell_data[1][2]}")
            self.change_label()
            change_cell_colors(self, row, col, False)
        else:
            # valid next choice
            if cell_color == "lightgreen": # change to lightgreen
                cell_button.config(bg = "pink")
                cell_data[0] = self.cell_path[len(self.cell_path) -1] # set previous cell data
                previous_cell_data = cell_data[0] # previous cell data
                widget = self.grid_slaves(previous_cell_data[0],previous_cell_data[1])[0]
                color = widget['bg']
                if color == "pink":
                    widget.config(bg="lightblue")
                change_cell_colors(self, previous_cell_data[0],previous_cell_data[1], True)

                cell_data[1] = (row, col, cell_data[0][2] +1) # set current cell data
                self.cell_path.append(cell_data[1])
                self.moves += 1
                if cell_data[1][2] > self.high_score:
                    self.high_score = cell_data[1][2]     
                cell_button.config(text = f"{cell_data[1][2]}")
                self.change_label()
                change_cell_colors(self, row, col, False)

                # check if puzzle completed
                if cell_data[1][2] == self.rows * self.columns:
                    on_win()
            else:
                # if clicked on pink
                if cell_color == "pink":
                    answer = True
                    if len(self.cell_path) == 1:
                        answer = on_closing()
                    if answer == True:  # if on_closing() answer = no
                        # remove all choices
                        change_cell_colors(self, row, col, True)
                        # change color to lightgray
                        cell_button.config(bg = "lightgray")
                        cell_button.config(text = "")
                        # pop current off cell path
                        self.cell_path.pop()
                        # change clicked cell data to len(cellpath)-1
                        previous_cell_data = cell_data[0] # previous cell data
                        row = previous_cell_data[0]
                        col = previous_cell_data[1]
                        cell_data = self.data[(row, col)]
                        cell_button = self.buttons[(row, col)]
                        cell_color = cell_button["bg"]
                        # ch ange color to pink
                        cell_button.config(bg = "pink")
                        self.moves += 1
                        if cell_data[1][2] > self.high_score:
                            self.high_score = cell_data[1][2]     
                        cell_button.config(text = f"{cell_data[1][2]}")
                        self.change_label()
                        # create all choices
                        change_cell_colors(self, row, col, False)

def on_closing():
    if messagebox.askyesno("Quit", "Do you really want to close the puzzle?"):
        exit(0)
    return False

def on_win():
    if messagebox.askyesno("YOU WON", "Congratulations You Won!\nDo you want to end the puzzle?"):
        exit(0)
    

# changes cell colors for rule based picks  
# do_old == true (cells = lightgray), false (cells = lightgreen)
def change_cell_colors(board, row, column, do_old):
    for choice in range(8):
        match (choice):
            case 0: # row col+3
                new_row = row
                new_column = column +3
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 1: # row+3 col 
                new_row = row +3
                new_column = column
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 2: # row col-3
                new_row = row
                new_column = column -3
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 3: # row-3 col
                new_row = row -3
                new_column = column
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 4: # row+2 col+2
                new_row = row +2
                new_column = column +2
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 5: # row+2 col-2
                new_row = row +2
                new_column = column -2
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 6: # row-2 col-2
                new_row = row -2
                new_column = column -2
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 7: # row-2 col+2
                new_row = row -2
                new_column = column +2
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue

def change_cell_colors_helper(board, row, column, do_old):
    if row >= 0 and row <=9 and column >=0 and column <=9:
        widget = board.grid_slaves(row, column)[0]
        color = widget['bg']
        if do_old and color == "lightgreen":
            widget.config(bg="lightgray")
        elif not do_old and color == "lightgray":
            widget.config(bg="lightgreen")

