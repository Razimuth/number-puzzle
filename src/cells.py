import tkinter as tk
from tkinter import ttk
#from main import Cell_Num

Cell_Num = 0

class Cell:
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

    
    """Callback function when a grid cell (button) is clicked."""
    print(f"Clicked cell at Row: {row}, Column: {col}")


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