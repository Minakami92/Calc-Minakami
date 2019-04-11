#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
LAYOUT = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+'],
]


class CreateUi(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        dispay_label = ttk.Label(
            self, text='0'
        )
        dispay_label.grid(
            column=0, row=0, columnspan=4, sticky=(tk.N, tk.S, tk.E, tk.W)
        )

        for y, row in enumerate(LAYOUT, 1):
            for x, char in enumerate(row):
                button = ttk.Button(self, text=char)
                button.grid(column=x, row=y, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

root=tk.Tk()
root.title("Minakami's calculator")
CreateUi(root)

root.mainloop()
