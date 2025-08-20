import tkinter as tk

class CellObject:
    def __init__(self, board, row, column, data, prev_cell, current_cell):
        self.data = data
        self.current_cell = current_cell
        self.prev_cell = prev_cell
#        self.widget = tk.Button(parent_frame, text=f"Cell ({row},{col})\nData: {data}")
#        self.widget = tk.Button(frame, text=f"Cell ({row},{col})\nData: {data}", borderwidth=1,
        self.widget = tk.Button(board, text=f"{data}", borderwidth=1,
#        self.widget = tk.Button(frame, text=(lambda data: data if data > 0 else command=hide_label), borderwidth=1,
                           relief="solid", width=10, height=3, bg="lightgreen")
#tk.Button(parent_frame, text=f"Cell ({row},{col})\nData: {data}")
        self.widget.grid(row=row, column=column, padx=5, pady=5)
        self.widget.bind("<Button-1>", self.on_click) # Bind left mouse click

#  need to set in grid setup ? maybe not
#  add self.prev_cell = (0, 0, 0, "lightgray")   # as a tuple 



    def on_click(self, event):
        clicked_widget = event.widget
        grid_data = clicked_widget.grid_info()
        current_bg_color = clicked_widget['bg']  # Or button.cget('bg')        
        row = grid_data['row']
        column = grid_data['column']
        board = grid_data['in']
#        old_new = 'old'

        # valid next choice
        if current_bg_color == "lightgreen":
            # find prev_cell (pink) = current_cell
            # send to change_cell_colors(current_cell[0],current_cell[1], old_new)
            change_cell_colors(board, self.current_cell[0],self.current_cell[1], True)
            # change current cell to lightblue
            # save prevcell = (self.current_cell[0],self.current_cell[1], self.data
            # currentcell = (row, column prevcell[2] +1)
            # change clicked to "pink"
            # config clicked text to currencell[2]
            # change all new choices
#            change_cell_colors(board, self.current_cell[0],self.current_cell[1], False)
            pass
        elif current_bg_color == "pink":    
            # want to back up to prevcell
            # change do old == true on currentcell coords
            # change pink to lightgray
            # change prevcell bg == pink 
            # change do old == false on prevcell coords
            pass


#            clicked_widget.config(bg="pink")


# if lightgreen then ok to place, find prevcell (pink by checking rule choices, ex row+3col+0, row+2col+2)
#   change other choices if lightgreen change to lightgray,  when find pink save as tuple(row,col,number,bg).
#   change prev to lightblue, change clicked to pink with data as prevcell[3] +1,
#   now change new choices to lightgreen  if numb == 100 then win


        if check_valid_choice(board, row, column):
            # if lightgreen
            # else pink
            pass

        print(f"Clicked on cell at Row: {row}, Column: {column}")
        # You can now perform actions based on the clicked cell

        print(f"Cell clicked! Data: {self.data}")
        # You can add more complex logic here based on the cell's data

        print(f"button bg  {current_bg_color}")

        if current_bg_color == "lightgray":
#            clicked_widget.config(bg="yellow")
            clicked_widget.config(bg="lightblue")

        
        if current_bg_color == "yellow" and self.data == "":
            clicked_widget.config(text=f"{self.prev_cell[2]+1}")
    # prev_cell will be set elsewhere, just here to test
            self.prev_cell = (row, column, 2,"red")

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

def change_cell_colors(board, row, column, do_old):

    print("1")
    for choice in range(8):
        match (choice):
            case 0: # row col+3
                new_row = row
                new_column = column +3
                print('1.0')
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 1: # row+3 col 
                new_row = row +3
                new_column = column
                print('1.1')
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 2: # row col-3
                new_row = row
                new_column = column -3
                print('1.2')
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 3: # row-3 col
                new_row = row -3
                new_column = column
                print('1.3')
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 4: # row+2 col+2
                new_row = row +2
                new_column = column +2
                print('1.4')
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 5: # row+2 col-2
                new_row = row +2
                new_column = column -2
                print('1.5')
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 6: # row-2 col-2
                new_row = row -2
                new_column = column -2
                print('1.6')
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue
            case 7: # row-2 col+2
                new_row = row -2
                new_column = column +2
                print('1.7')
                change_cell_colors_helper(board, new_row, new_column, do_old)
                continue

    pass

def change_cell_colors_helper(board, row, column, do_old):
    print("2")
    if row >= 0 and row <=9 and column >=0 and column <=9:
        print("2.1")
        widget = board.grid_slaves(row, column)[0]
        color = widget['bg']
        if do_old and color == "lightgreen":
            widget.config(bg="lightgray")
        elif not do_old and color == "lightgray":
            widget.config(bg="lightgreen")
        print(widget)


def check_valid_choice(board, row, column):
# row col+3, row+3 col, row col-3, row-3 col, row+2 col+2, row+2 col-2, row-2 col-2, row-2 col+2
    
    widget_at_1_0 = board.grid_slaves(row, column)[0]

    color = widget_at_1_0['bg']
    print(f"color =  {color}")

    widget_at_1_0.config(text="New Label 2 Text")    
    return True


def find_prev_cell():
    # go through all rule allowed placements, if bg= red return status tuple to set as prev_cell
    # value

    pass

def change_cell_choices():
    # go through all rule allowe cells to either set to yellow for choices
    # or set yellow back to lightgray if choice not selected
    # or if red for prev cell then change to lightblue if value not ""
    # or if "" then change to lightgray 
    pass

def check_cell_status(row,col):
    return (row, col, value, bg)



# Example of modifying a cell's data and updating its display
#cell_data[(0, 0)].set_value("Updated!")
#cell_widgets[(0, 0)].config(text=cell_data[(0, 0)].get_value())


#root = tk.Tk()
#root.title("10x10 Number Puzzle")

#grid_frame = tk.Frame(root)
#grid_frame.pack(padx=10, pady=10)

"""
cells = []
for r in range(10):
    row_cells = []
    for c in range(10):
        prev_cell = (0,0,0,"lightgray")
        cell_data = ""
#        cell_data = f"Value {r*10 + c}"
        cell = CellObject(grid_frame, r, c, cell_data, prev_cell)
        row_cells.append(cell)
    cells.append(row_cells)

"""
#root.mainloop()