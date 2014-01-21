import sys
sys.path.insert(0, 'c:\\users\\compy\\documents\\github\\pythonlearning')

from PeriodicCoordinateMap import *

from tkinter import *
#from tkinter import ttk
import zlib
from PIL import Image
import pybel

class LewisDotApp:
  
  def __init__(self, root):
    #main frame
    periodic_lbl_frame = LabelFrame(root, text='Periodic Table', height=300, width=300)
    periodic_lbl_frame.pack(side=LEFT, fill=BOTH, expand=1, anchor=W, padx=10, pady=10)
    
    frame_xy = periodic_lbl_frame.grid_bbox()
    print(frame_xy)
    print(periodic_lbl_frame.grid_info())
    
    #pack image as label
    # self.periodic_lbl = Label(periodic_lbl_frame, text="periodic_table")
    # self.periodic_t = PhotoImage(file="Periodic_table.gif")
    # self.periodic_lbl['image'] = self.periodic_t
    # self.periodic_lbl.pack()
    
    self.canvas = Canvas(periodic_lbl_frame)
    self.periodic_t = PhotoImage(file="Periodic_table.gif")
    self.canvas.create_image((400,200), image=self.periodic_t)
    self.canvas.pack()
    
    canvas_xy = self.canvas.bbox(ALL)
    print(canvas_xy)
    
    
    
    
#create root surface
root = Tk()

#create app object
app = LewisDotApp(root)

#run main loop
root.mainloop()

#root.destroy() #optional
    
    
  