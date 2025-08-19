import tkinter as tk

def handle_cell_click(event):
    """Function to handle a click on a grid cell."""
    clicked_widget = event.widget
    grid_data = clicked_widget.grid_info()
    row = grid_data['row']
    column = grid_data['column']
    print(f"Clicked on cell at Row: {row}, Column: {column}")
    # You can now perform actions based on the clicked cell
