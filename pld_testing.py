#caleb meador 01/06/2014
#adapted from http://www.tkdocs.com/tutorial/firstexample.html

def callback(event):
  print ("clicked at", event.x, event.y)

# adapted from: http://stackoverflow.com/questions/16383530/python-return-current-cursor-position-and-position-last-left-mouse-click  
def on_motion(event):
  print(event.x, event.y)

from tkinter import *
from tkinter import ttk
import zlib
from PIL import Image
import pybel
    
root = Tk()
root.title("Project Lewis-Dot")

# # #not yet
# # # style = ttk.Style()

# # # style.map("C.TButton",
    # # # foreground=[('pressed', 'green'), ('active', 'pink'), ('!pressed', 'yellow')],
    # # # background=[('pressed', 'red'), ('active', 'blue'), ('!pressed', 'green') ]
    # # # )
  
# # #chem_canvas = ttk.Frame(root, padding="3 3 12 12")

# # #periodic_table = ttk.Frame(root, borderwidth = 5, relief="sunken", width=200, height=100)

#periodic table frame
periodic_lbl_frame = ttk.LabelFrame(root, text='Periodic Table', height=300, width=300)

#periodic table
periodic_lbl = ttk.Label(periodic_lbl_frame, text="periodic_table")

#import periodic image and attach to label
periodic_t = PhotoImage(file="Periodic_table.gif")
periodic_lbl['image'] = periodic_t

#create event callback for clicking on image
periodic_lbl.bind("<Motion>", on_motion)



#pack periodic table, frame into display
periodic_lbl_frame.pack(side=LEFT, fill=BOTH, expand=1, anchor=W, padx=10, pady=10)
periodic_lbl.pack()

#create atom view box
view_lbl_frame = ttk.LabelFrame(root, text="View Box", height=300, width=300)
view_lbl = ttk.Label(view_lbl_frame)

#pack atom view box into output
view_lbl_frame.pack(side=RIGHT, fill=BOTH, expand=1, anchor=E, padx=10, pady=10)

  


root.mainloop()
