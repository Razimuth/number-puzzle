import tkinter as tk
from tkinter import ttk
from cells import CellObject, cell_clicked
from cells3 import CellObject

def display_board(board):
    cells = []
    for row in range(10):
        row_cells = []
        for column in range(10):
            current_cell = (0,0,0)
            prev_cell = (0,0,0)
            cell_data = ""
#        cell_data = f"Value {r*10 + c}"
            cell = CellObject(board, row, column, cell_data, prev_cell, current_cell)
            row_cells.append(cell)
        cells.append(row_cells)




#    root = tk.Tk()
#    root.title("10x10 Number Puzzle")
#    root.geometry('1000x800')
#    board = tk.Frame(root)
#    board.place(x=60, y=100, width=860, height=630)
 #   board.geometry('860x630')

    # Create column headers (A, B, C...)
#    for col_index in range(10):
#        header_text = chr(65 + col_index)  # Convert 0-9 to A-J
#        col_label = tk.Label(board, text=header_text, relief="solid", width=8, height=3)
#        col_label.grid(row=0, column=col_index + 1, padx=1, pady=1) # +1 for left-side row labels

    # Create row headers (1, 2, 3...)
#    for row_index in range(10):
#        row_label = tk.Label(board, text=str(row_index + 1), relief="solid", width=8, height=3)
#        row_label.grid(row=row_index + 1, column=0, padx=1, pady=1) # +1 for top-side column labels

    # Create the 10x10 grid of cells
#    cell_num = 1
"""
    buttons = []  # To store references to buttons
    
    for row in range(10):
        row_buttons = []
        for col in range(10):
#            tk.Label(board, text=f"{cell_num}", relief="solid", borderwidth=2).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        # Create a button for each cell
            button = tk.Button(board, text=f"", width=5, bg="lightgray",
                        command=lambda r=row, c=col: cell_clicked(r, c, buttons))
            button.grid(row=row, column=col, padx=2, pady=2) # Place button in the grid
            row_buttons.append(button)
        buttons.append(row_buttons)
          
"""            


#           tk.Button(board, text=f"({row},{col})",
#                        command=lambda r=row, c=col: cell_clicked(r, c)).grid(row=row,
#                        column=col, padx=2, pady=2) # Place button in the grid
#            cell_label = ttk.Label(board, text=f"{cell_num}")
#            cell_label = tk.Label(board, text=f"({row},{col})", relief="ridge", width=8, height=3)
#            cell_label.grid(row=row, column=col, padx=20, pady=20) # Offset by 1 for headers
 #           cell_label.grid(row=row + 1, column=col + 1, padx=1, pady=1) # Offset by 1 for headers
#            cell1 = CellObject(board, 0, 0, " 1 ")
#           cell_num += 1
#    ttk.Separator(board, orient="horizontal").grid(row=0, column=0, columnspan=10, sticky="n")
#    ttk.Separator(board, orient="vertical").grid(row=0, column=0, rowspan=10, sticky="e")

    #cell1 = CellObject(board, 0, 0, " 1 ")

#    root.mainloop()
#    return
#if __name__ == "__main__":
#    create_grid_with_labels()



"""
class GameWindow:
    def __init__(self, font_size=32):
        self._root = tk.Tk()
        self._root.title('10 x 10 Number Puzzle')
        self._root.geometry('1000x800')

        self._font_size = font_size
        self._board = tk.Frame(self._root, bg='white')
        self._board.grid(row=0, rowspan=10)
#        self._build_game_frame()

        self._bottom_frame = tk.Frame(self._root)
        self._bottom_frame.grid(row=10)
#        self._build_bottom_frame()

def build_board():
    pass

def buuld_game_grid():
    pass

def build_labels():
    pass
"""