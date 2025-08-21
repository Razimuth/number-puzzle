import tkinter as tk
from tkinter import messagebox
from config import FIRSTCLICK

class ButtonGrid:
    def __init__(self, root, number_rows, number_columns):
        self.board = root
#        self.root.title("Button Grid with Cell Data")
        self.rows = number_rows
        self.columns = number_columns
        self.buttons = {}  # Dictionary to store buttons by (row, column)
        self.data = {}     # Dictionary to store data associated with each cell

        for r in range(self.rows):
            for c in range(self.columns):
                # Create a Button
                button = tk.Button(self.board, text=f"", borderwidth=1, font=("Helvetica", 20, "bold"),
                                   relief="solid", width=3, height=2, bg="lightgreen")
                button.grid(row=r, column=c, padx=5, pady=5)

#                button = tk.Button(self.root, text=f"Button ({r},{c})")
#                button.grid(row=r, column=c, padx=5, pady=5)
                # Store the button in the dictionary
                self.buttons[(r, c)] = button

                # Store some data for this cell (example: a tuple of coordinates)
                # ( prev (row, col, num), current (row, col, num) )
                self.data[(r, c)] = ((0,0,0),(0,0,0)) #(row, col)

                # Bind the button's click event to a callback function
                button.config(command=lambda row=r, col=c: self.button_clicked(row, col))
#        self.widget.bind("<Button-1>", self.on_click) # Bind left mouse click

    def button_clicked(self, row, col):
        # Access the data of the clicked button using row and column
        cell_data = self.data[(row, col)]
        cell_button = self.buttons[(row, col)]
        cell_color = cell_button["bg"]

#        print(f"Button at ({row},{col}) clicked! Data: {cell_data}")

        # changes all cells to lightgray except clicked if is firstclick 
        global FIRSTCLICK
        if FIRSTCLICK is None:
            FIRSTCLICK = cell_button
            for row1 in range(self.rows):
                for column1 in range(self.columns):
                    if row == row1 and col == column1:
                        # found clicked 
                        pass
                    else:
                        widget = self.board.grid_slaves(row1, column1)[0]
                        color = widget['bg']
                        if color == "lightgreen":
                         widget.config(bg="lightgray")

            #  valid cell that is firstclick
            cell_button.config(bg = "pink")
            cell_data[0] = (row, col, 1) # set previous cell data
            cell_data[1] = (row, col, 1) # set current cell data
            cell_button.config(text = f"{cell_data[1][2]}")
            ###change_cell_colors(self.board, row, col, False)

                # need to do_old = false
#            print(f"First button clicked: {FIRSTCLICK}")
        
        # if not firstclick
        else:
            # if click on 1  if clicked again ask want to end?
            if cell_button == FIRSTCLICK:
                on_closing(self.board)
            else:

                # valid next choice




                if cell_color == "green": # change to lightgreen
 
 
###                    if cell_button == FIRSTCLICK:
                    #  valid cell that is firstclick
                        cell_button.config(bg = "pink")
                        cell_data[(row,col)][0] = (row, col, 1) # set previous cell data
                        cell_data[(row,col)][1] = (row, col, 1) # set current cell data
                        cell_button.config(text = f"{cell_data[(row,col)][1][2]}")
###                    else:
                        # go to prev cell
                        previous_cell_data = cell_data[(row,col)][0] # previous cell data
                        widget = self.board.grid_slaves(previous_cell_data[0],previous_cell_data[1])[0]
                        color = widget['bg']
                        if color == "pink":
                            widget.config(bg="lightblue")

                # now change surrounding lightgreen to lightgray using previous cell




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
def on_closing(board):
    if messagebox.askyesno("Quit", "Do you really want to close the application?"):
        board.destroy()
        exit(0)

###def set_previous_cell_data
###def get_previous_cell_data



# changes cell colrs for rule based picks  
# do_old == true (cells = lightgray), false (cells = lightgreen)
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
