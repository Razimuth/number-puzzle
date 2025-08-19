import tkinter as tk

class CellObject:
    def __init__(self, frame, row, col, data):
        self.data = data
#        self.widget = tk.Button(parent_frame, text=f"Cell ({row},{col})\nData: {data}")
        self.widget = tk.Button(frame, text=f"Cell ({row},{col})\nData: {data}", borderwidth=1,
                           relief="solid", width=10, height=3, bg="lightgray")
#tk.Button(parent_frame, text=f"Cell ({row},{col})\nData: {data}")
        self.widget.grid(row=row, column=col, padx=5, pady=5)
        self.widget.bind("<Button-1>", self.on_click) # Bind left mouse click



    def on_click(self, event):
        clicked_widget = event.widget
        grid_data = clicked_widget.grid_info()
        current_bg_color = clicked_widget['bg']  # Or button.cget('bg')        
        row = grid_data['row']
        column = grid_data['column']
        print(f"Clicked on cell at Row: {row}, Column: {column}")
        # You can now perform actions based on the clicked cell

        print(f"Cell clicked! Data: {self.data}")
        # You can add more complex logic here based on the cell's data

        print(f"button bg  {current_bg_color}")

        if current_bg_color == "lightgray":
            clicked_widget.config(bg="lightblue")



# Example of modifying a cell's data and updating its display
#cell_data[(0, 0)].set_value("Updated!")
#cell_widgets[(0, 0)].config(text=cell_data[(0, 0)].get_value())


root = tk.Tk()
root.title("Grid with Cell Objects")

grid_frame = tk.Frame(root)
grid_frame.pack(padx=10, pady=10)

cells = []
for r in range(10):
    row_cells = []
    for c in range(10):
        cell_data = f"Value {r*10 + c}"
        cell = CellObject(grid_frame, r, c, cell_data)
        row_cells.append(cell)
    cells.append(row_cells)

root.mainloop()