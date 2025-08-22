import tkinter as tk
from tkinter import messagebox
from config import FIRSTCLICK

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
    def __init__(self, master, label_string_var): # moves, high_score):
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
        self.cell_stack = []
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

        if len(self.cell_stack) == 0:
#        if FIRSTCLICK is None:
 #           FIRSTCLICK = cell_button
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
            #  valid cell that is firstclick
            cell_button.config(bg = "pink")
            cell_data[0] = (row, col, 0) # set previous cell data
            cell_data[1] = (row, col, cell_data[0][2] +1) # set current cell data
            self.cell_stack.append(cell_data[1])
            self.moves += 1
            if cell_data[1][2] > self.high_score:
                self.high_score = cell_data[1][2]     
            cell_button.config(text = f"{cell_data[1][2]}")
            self.change_label()
            change_cell_colors(self, row, col, False)
        else:
            # if click on 1  if clicked again ask want to end?

####
  # should do when pop results to len == 0
    ####        if cell_button == FIRSTCLICK:
    ####            on_closing()
####            
            # valid next choice
            if cell_color == "lightgreen": # change to lightgreen
                cell_button.config(bg = "pink")
                # get prev
                cell_data[0] = self.cell_stack[len(self.cell_stack) -1] # set previous cell data

                previous_cell_data = cell_data[0] # previous cell data
                widget = self.grid_slaves(previous_cell_data[0],previous_cell_data[1])[0]
                color = widget['bg']
                if color == "pink":
                    widget.config(bg="lightblue")
                change_cell_colors(self, previous_cell_data[0],previous_cell_data[1], True)

                cell_data[1] = (row, col, cell_data[0][2] +1) # set current cell data
                self.cell_stack.append(cell_data[1])
                self.moves += 1
                if cell_data[1][2] > self.high_score:
                    self.high_score = cell_data[1][2]     
                cell_button.config(text = f"{cell_data[1][2]}")
                self.change_label()
                change_cell_colors(self, row, col, False)
            else:
                # if clicked on red
                pass


###                        print(widget)
                        #time.sleep(10)  # Pause for 5 seconds                
                    
             


            # find prev_cell (pink) = current_cell

            # send to change_cell_colors(current_cell[0],current_cell[1], old_new)
#                change_cell_colors(board, self.current_cell[0],self.current_cell[1], True)
            # change current cell to lightblue
###            else:
            # save prevcell = (self.current_cell[0],self.current_cell[1], self.data
            
            # currentcell = (row, column prevcell[2] +1)
            # change clicked to "pink"
            # config clicked text to currencell[2]
            # change all new choices
#            change_cell_colors(board, self.current_cell[0],self.current_cell[1], False)
                pass
###        elif current_bg_color == "pink":    
        # if firstclick button don't do
        
            # want to back up to prevcell
            # change do old == true on currentcell coords
            # change pink to lightgray
            # change prevcell bg == pink 
            # change do old == false on prevcell coords
###            pass


#            clicked_widget.config(bg="pink")


# if lightgreen then ok to place, find prevcell (pink by checking rule choices, ex row+3col+0, row+2col+2)
#   change other choices if lightgreen change to lightgray,  when find pink save as tuple(row,col,number,bg).
#   change prev to lightblue, change clicked to pink with data as prevcell[3] +1,
#   now change new choices to lightgreen  if numb == 100 then win


###        if check_valid_choice(board, row, column):
            # if lightgreen
            # else pink
###            pass

###        print(f"Clicked on cell at Row: {row}, Column: {column}")
        # You can now perform actions based on the clicked cell

###        print(f"Cell clicked! Data: {self.data}")
        # You can add more complex logic here based on the cell's data

###        print(f"button bg  {current_bg_color}")

###        if current_bg_color == "lightgray":
#            clicked_widget.config(bg="yellow")
###            clicked_widget.config(bg="lightgreen")

        
###        if current_bg_color == "yellow" and self.data == "":
###            clicked_widget.config(text=f"{self.prev_cell[2]+1}")
    # prev_cell will be set elsewhere, just here to test
###            self.prev_cell = (row, column, 2,"red")

# when click 
# 1 check if bg= lightgreen or pink
# if lightgreen then ok to place, find prevcell (pink by checking rule choices, ex row+3col+0, row+2col+2)
#   change other choices if lightgreen change to lightgray,  when find pink save as tuple(row,col,number,bg).
#   change prev to lightblue, change clicked to pink with data as prevcell[3] +1,
#   now change new choices to lightgreen  if numb == 100 then win
# if pink then need to change all lightgreen choices to lightgray, change pink to lightgray,
#   change prevcell to pink, change data to "".  now change new choices to lightgreen from new pink cell

# row col+3, row+3 col, row col-3, row-3 col, row+2 col+2, row+2 col-2, row-2 col-2, row-2 col+2
# good if lightgreen or pink, not good if lightgray or lightblue or row < 0 or row > 9 or col < 0 col > 9     



#        cell_button.config(bg="pink")
#        widget = self.board.grid_slaves(row+1, col+1)[0]
#        color = widget['bg']
##                if color == "pink":
#        widget.config(bg="blue")
                
#                print(widget)
#                time.sleep(10)  # Pause for 5 seconds                


# Create the main window and run the application
#root = tk.Tk()
#app = ButtonGrid(root)
#root.mainloop()
def on_closing():
    if messagebox.askyesno("Quit", "Do you really want to close the application?"):
        #Board.destroy()
        exit(0)

###def set_previous_cell_data
###def get_previous_cell_data



# changes cell colrs for rule based picks  
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

    pass

def change_cell_colors_helper(board, row, column, do_old):
    if row >= 0 and row <=9 and column >=0 and column <=9:
        widget = board.grid_slaves(row, column)[0]
        color = widget['bg']
        if do_old and color == "lightgreen":
            widget.config(bg="lightgray")
        elif not do_old and color == "lightgray":
            widget.config(bg="lightgreen")
























"""
import tkinter as tk
from tkinter import ttk
#from main import Cell_Num

Cell_Num = 0

class CellObject:
    def __init__(self, master, row, column, text_content):
        self.frame = ttk.Frame(master, borderwidth=1, relief="solid")
        self.label = ttk.Label(self.frame, text=text_content, width=8, height=3)
        self.label.pack(expand=True, fill="both") # Pack the label inside the frame
        self.frame.grid(row=row, column=column, padx=2, pady=2, sticky="nsew")


def cell_clicked(row, col, buttons):
    global Cell_Num
    clicked_button = buttons[row][col]
    current_color = clicked_button.cget("bg") # Get current background color
    current_text = clicked_button.cget("text")
    
    if current_color == "lightgray": # Check if it's the default color
        clicked_button.config(bg="lightblue")
    else:
        clicked_button.config(bg="lightgray") # Revert to default
    
#    if current_color == "yellow" or current_color == "red":
#        if current_color == "red":



    
    if current_text == "":
        # needs to be yellow
        #    push on stack
        # cell_num could be number of stack items

        Cell_Num += 1
    else:
        # needs to be red
        # need to return to last     use stack 
        
        Cell_Num = int(current_text)
        Cell_Num -=1
    clicked_button.config(text=f"{Cell_Num}")

    
   """ """Callback function when a grid cell (button) is clicked."""
"""    print(f"Clicked cell at Row: {row}, Column: {col}")

"""
"""
import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Button Grid")

        self.buttons = []  # To store references to buttons

        for r in range(3):  # 3 rows
            row_buttons = []
            for c in range(3):  # 3 columns
                button = tk.Button(master, text=f"({r},{c})",
                                   width=10, height=3,
                                   command=lambda row=r, col=c: self.on_button_click(row, col))
                button.grid(row=r, column=c, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def on_button_click(self, row, col):
        clicked_button = self.buttons[row][col]
        current_color = clicked_button.cget("bg") # Get current background color

        if current_color == "lightgray": # Check if it's the default color
            clicked_button.config(bg="blue")
        else:
            clicked_button.config(bg="lightgray") # Revert to default

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
"""
# Create the main application window
#root = tk.Tk()
#root.title("Grid with Cell Objects")

# Configure grid weights for resizing
#for i in range(3):
#    root.grid_rowconfigure(i, weight=1)
#    root.grid_columnconfigure(i, weight=1)

# Create and place instances of CellObject
#cell1 = CellObject(root, 0, 0, "Cell 1")
#cell2 = CellObject(root, 0, 1, "Cell 2")
#cell3 = CellObject(root, 1, 0, "Cell 3")
#cell4 = CellObject(root, 1, 1, "Cell 4")

#root.mainloop()

"""
In this example, CellObject is a custom class that creates a tk.Frame and a tk.Label within it. 
The grid() method is then called on the self.frame object to place it within the main window's grid layout. 
This effectively allows you to manage cell-specific data and visual elements through your custom objects.
"""