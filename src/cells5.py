import tkinter as tk

class CellObject:
    def __init__(self, master, row, column, text="", command=None):
        """
        Initializes a CellObject, representing a button in the grid.

        Args:
            master: The parent widget (e.g., a Tkinter Frame or Tk root).
            row: The row index for the button in the grid.
            column: The column index for the button in the grid.
            text: The text to display on the button.
            command: The function to call when the button is clicked.
        """
        self.button = tk.Button(master, text=text, command=command)
        self.button.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)

class ButtonGridApp:
    def __init__(self, root, rows, cols):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.buttons = []

        # Configure grid resizing
        for i in range(rows):
            root.grid_rowconfigure(i, weight=1)
        for j in range(cols):
            root.grid_columnconfigure(j, weight=1)

        self._create_grid_of_buttons()

    def _create_grid_of_buttons(self):
        for r in range(self.rows):
            row_buttons = []
            for c in range(self.cols):
                button_text = f"R{r}C{c}"
                # You can pass a specific command for each button here
                button_command = lambda r=r, c=c: self._button_click(r, c)
                cell = CellObject(self.root, r, c, text=button_text, command=button_command)
                row_buttons.append(cell)
            self.buttons.append(row_buttons)

    def _button_click(self, row, col):
        print(f"Button at Row {row}, Column {col} clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter Button Grid")

    app = ButtonGridApp(root, rows=5, cols=5) # Create a 5x5 grid of buttons
    root.mainloop()