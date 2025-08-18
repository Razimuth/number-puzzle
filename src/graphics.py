import tkinter as tk

def display_board(board):
#    root = tk.Tk()
#    root.title("10x10 Number Puzzle")
#    root.geometry('1000x800')
#    board = tk.Frame(root)
#    board.place(x=60, y=100, width=860, height=630)
 #   board.geometry('860x630')

    # Create column headers (A, B, C...)
    for col_index in range(10):
        header_text = chr(65 + col_index)  # Convert 0-9 to A-J
        col_label = tk.Label(board, text=header_text, relief="solid", width=8, height=3)
        col_label.grid(row=0, column=col_index + 1, padx=1, pady=1) # +1 for left-side row labels

    # Create row headers (1, 2, 3...)
    for row_index in range(10):
        row_label = tk.Label(board, text=str(row_index + 1), relief="solid", width=8, height=3)
        row_label.grid(row=row_index + 1, column=0, padx=1, pady=1) # +1 for top-side column labels

    # Create the 10x10 grid of cells
    for row in range(10):
        for col in range(10):
            cell_label = tk.Label(board, text=f"({row},{col})", relief="ridge", width=8, height=3)
            cell_label.grid(row=row + 1, column=col + 1, padx=1, pady=1) # Offset by 1 for headers

#    root.mainloop()

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