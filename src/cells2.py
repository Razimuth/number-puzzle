import tkinter as tk
from cells import cell_clicked
from events import handle_cell_click

class CellObject:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

#def handle_cell_click(event):
#    """Function to handle a click on a grid cell."""
#    clicked_widget = event.widget
#    grid_data = clicked_widget.grid_info()
#    row = grid_data['row']
#    column = grid_data['column']
#    print(f"Clicked on cell at Row: {row}, Column: {column}")
#    # You can now perform actions based on the clicked cell

root = tk.Tk()
root.title("10x10 Number Puzzle")

# Dictionary to store references to our cell widgets and custom cell objects
cell_widgets = {}
cell_data = {}

for row_idx in range(10):
    for col_idx in range(10):
        # Create a custom CellObject
        cell_obj = CellObject("")
#        cell_obj = CellObject(f"R{row_idx}C{col_idx}")
        cell_data[(row_idx, col_idx)] = cell_obj

        # Create a Tkinter Label to display the cell's value
        button = tk.Button(root, text=cell_obj.get_value(), borderwidth=1,
                           relief="solid", width=10, height=3)
#        button = tk.Button(root, text=cell_obj.get_value(), borderwidth=1,
#                           command=lambda r=row_idx, c=col_idx: cell_clicked(r, c, cell_widgets), relief="solid", width=10, height=3)
        button.grid(row=row_idx, column=col_idx, padx=2, pady=2)
        button.bind("<Button-1>", handle_cell_click) # Bind left-click to each label
        cell_widgets[(row_idx, col_idx)] = button

# Example of modifying a cell's data and updating its display
cell_data[(0, 0)].set_value("Updated!")
cell_widgets[(0, 0)].config(text=cell_data[(0, 0)].get_value())



def cell_clicked(row, col, cell_widgets):
#def cell_clicked(row, col, buttons):
    global Cell_Num
    clicked_button = cell_widgets[(row_idx, col_idx)]    #buttons[row][col]
#    clicked_button = buttons[row][col]
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





root.mainloop()