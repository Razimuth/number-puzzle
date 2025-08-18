import tkinter as tk
#from tkinter import ttk
from graphics import display_board

def main():

    root = tk.Tk()
    root.title("10x10 Number Puzzle")
    root.geometry('1000x800')
    board = tk.Frame(root)
    board.place(x=60, y=100, width=860, height=630)

    display_board(board)

    root.mainloop()

    # window
#    root = tk.Tk()
#    root.title("10 x 10 Number Puzzle")
#    root.geometry("1000x800")

    # labels down left side A B C D E F G H I J   across top 1 2 3 4 5 6 7 8 9 10
#    label1 = tk.Label(master= root, text= '1 ', background= 'blue')
#    label11 = ttk.Label(master= root, text= 'A ', background= 'blue')
#    button1 = ttk.Button(master= root, text= 'Start')
#    entry = ttk.Entry(master= root)

    # define the grid 10 x 10
#    root.columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight= 1)
#    root.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight= 1)

    # placing a widget
#    label1.grid(row= 0, column= 1, sticky= 'n')
#    label1.grid(row= 1, column= 0, sticky= 'n')

    # Example with frames
#    frame1 = tk.Frame(root, bg="lightblue")
#    frame1.grid(row=0, column=10, sticky="e")

#    button_in_frame = tk.Button(frame1, text="Button in Frame 1")
#    button_in_frame.grid(row=0, column=10, padx=10, pady=10)

# Create a Frame with a specific width and height
# The size is in pixels
#    frame = tk.Frame(root, width=400, height=200, bg="lightblue")

# Pack the frame to make it visible
# You might need to use pack_propagate(0) or grid_propagate(0) on the frame
# to prevent it from shrinking or expanding to fit its contents
#    frame.pack(padx=20, pady=20)
#    frame.pack_propagate(0) # Prevents the frame from resizing to fit its contents

# Add a label inside the frame to demonstrate content
#    label = tk.Label(frame, text="This is a fixed-size frame", bg="lightblue")
#    label.pack(pady=50)

#    num_rows = 10
#    num_cols = 10

#    for row in range(num_rows):
#        for col in range(num_cols):
#            # Create a Frame or Label for each cell
#            cell_frame = tk.Frame(
#                master=window,
#                relief=tk.RAISED,  # Add a raised border for visual separation
#                borderwidth=1
#            )
#            cell_frame.grid(row=row, column=col, padx=2, pady=2) # Add padding

#            # You can add content to each cell, e.g., a Label
#            cell_label = tk.Label(master=cell_frame, text=f"R{row}C{col}")
#            cell_label.pack(padx=5, pady=5) # Pack the label inside the frame

#    for i in range(num_rows):
#        window.grid_rowconfigure(i, weight=1)
#    for i in range(num_cols):
#        window.grid_columnconfigure(i, weight=1)

    # runs window
#    root.mainloop()

    pass




if __name__ == "__main__":
        main()
