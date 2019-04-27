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
        self.exp_list = ['0']

    def create_widgets(self):
        # self.expression_var = StringVar()
        # self.expression_var.set('0')
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
                button.bind('<Button-1>', self.calc)

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

        self.display_var = tk.StringVar()
        self.display_var.set('0')  

        dispay_label = ttk.Label(self, textvariable=self.display_var)
        dispay_label.grid(column=0, row=0, columnspan=4, sticky=(tk.N, tk.S, tk.E, tk.W))

    def calc(self, event):
          #print(event.widget['text'])
          char = event.widget['text']
          #self.display_var.set(char)]
          last = self.exp_list[-1]

          print("char: "+char)

          if char == '=':
            if last in ('+', '-', '*', '/', '**', '//'): 
                self.exp_list.pop()
            exp = eval(''.join(self.exp_list))
            self.exp_list = [str(exp)]
            print("self.exp.list: "+str(self.exp_list))

            self.exp_list = [list(self.exp_list)+[char]]
            #elif char == "C":
             #  self.exp_list = ["0"]
          if char == "C":
                self.display_var.set(["0"])
          print("self.display_var.get()"+self.display_var.get())

root=tk.Tk()
root.title("Minakami's calculator")
CreateUi(root)


root.mainloop()
