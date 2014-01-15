import tkinter
from tkinter import ttk

root = tkinter.Tk()

style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'green'), ('active', 'pink'), ('!pressed', 'yellow')],
    background=[('pressed', 'red'), ('active', 'blue'), ('!pressed', 'green') ]
    )

colored_btn = ttk.Button(text="A CAUSE DE GARCONS", style="C.TButton")#.pack()
colored_btn.grid(column=0, row=0, padx=10, pady=10)
root.mainloop()