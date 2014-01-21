#caleb meador 01/06/2014
#adapted from http://www.tkdocs.com/tutorial/firstexample.html

import sys
sys.path.insert(0, 'c:\\users\\compy\\documents\\github\\pythonlearning')

from PeriodicCoordinateMap import *

from tkinter import *
from tkinter import ttk
import zlib
from PIL import Image
import pybel


def callback(event):
  print ("clicked at", event.x, event.y)

# adapted from: http://stackoverflow.com/questions/16383530/python-return-current-cursor-position-and-position-last-left-mouse-click  
def on_motion(event, coords_list):
  check_periodic_map(event.x, event.y, coords_list)
  
def check_periodic_map(x, y, coords_list):
  #highlight = Canvas(periodic_canvas)
  highlight = Canvas(periodic_lbl_frame)
  for item in coords_list:
    x0 = highlight.canvasx(item[0])
    y0 = highlight.canvasy(item[1])
    x1 = highlight.canvasx(item[2])
    y1 = highlight.canvasy(item[3])
    if ((x > x0 and x < x1) and (y > y0 and y < y1)):
      print (x, y, (x0,y0,x1,y1))
      highlight.create_rectangle(x0,y0,x1,y1, outline="blue")
      highlight.pack()
    else:
      highlight.delete(ALL)
    


  
#create coord-map object and populate list.
icon_map = PeriodicCoordinateMap()
list_of_icon_coords = icon_map.getIconCoords()
  
#define root surface    
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

#periodic table image
#periodic_canvas = Canvas(periodic_lbl_frame)
periodic_lbl = ttk.Label(periodic_lbl_frame, text="periodic_table")

#import periodic image and attach to label
periodic_t = PhotoImage(file="Periodic_table.gif")
#periodic_canvas.create_image((0,0))
periodic_lbl['image'] = periodic_t

#create event callback for clicking on image
#periodic_canvas.bind("<Motion>", lambda event: on_motion(event, list_of_icon_coords))
periodic_lbl.bind("<Motion>", lambda event: on_motion(event, list_of_icon_coords))

#pack periodic table, frame into display
periodic_lbl_frame.pack(side=LEFT, fill=BOTH, expand=1, anchor=W, padx=10, pady=10)
#periodic_canvas.pack()
periodic_lbl.pack()

#create atom view box
view_lbl_frame = ttk.LabelFrame(root, text="View Box", height=300, width=300)
view_lbl = ttk.Label(view_lbl_frame)

#pack atom view box into output
view_lbl_frame.pack(side=RIGHT, fill=BOTH, expand=1, anchor=E, padx=10, pady=10)




root.mainloop()
