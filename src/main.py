import tkinter as tk
from cells import MainApp

def main():
    title = ("10x10 Number Puzzle")
    size = (830, 810)
    num_rows = 10
    num_columns = 10
    MainApp(title, size, num_rows, num_columns)
if __name__ == "__main__":
        main()
