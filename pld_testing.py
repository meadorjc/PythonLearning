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

def delete_icons(canvas_item):
	for item in canvas_item.find_withtag('icon'):
		canvas_item.delete(item)
	
def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2], item[3], fill='white', outline='blue', activeoutline='green', tags='icon' )
		
		
def on_motion(event, coords_list):
	current = canv.find_withtag('current')
	closest = canv.find_closest(event.x, event.y, 1)
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)
	canv.focus(closest)

	try:
		if 'icon' in current:
			print("Closest, Current:", closest, current)
			selected = closest
			canv.focus(selected)
		#else:
			#canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

# adapted from: http://stackoverflow.com/questions/16383530/python-return-current-cursor-position-and-position-last-left-mouse-click  
# def on_motion(event, coords_list):
  # check_periodic_map(event.x, event.y, coords_list)
  
# def check_periodic_map(x, y, coords_list):
  # #highlight = Canvas(periodic_canvas)
  # #highlight = Canvas(periodic_lbl_frame)
  # for item in coords_list:
    # x0 = highlight.canvasx(item[0])
    # y0 = highlight.canvasy(item[1])
    # x1 = highlight.canvasx(item[2])
    # y1 = highlight.canvasy(item[3])
    # if ((x > x0 and x < x1) and (y > y0 and y < y1)):
      # print (x, y, (x0,y0,x1,y1))
			# # TO DO: MAKE ACTIVE/PASSIVE COLOR
		 # #highlight.create_rectangle(x0,y0,x1,y1, outline="blue")
     # #highlight.pack()
    # #else:
     # #highlight.delete(ALL)
    


  
 
#define root surface    
root = Tk()
root.title("Project Lewis-Dot")

#periodic table frame
periodic_lbl_frame = ttk.LabelFrame(root, text='Periodic Table', height=450, width=790)

#periodic table image
periodic_canvas = Canvas(periodic_lbl_frame, height=450, width=790)
#periodic_lbl = ttk.Label(periodic_lbl_frame, text="periodic_table")

#import periodic image and attach to label
periodic_t = PhotoImage(file="Periodic_table.gif")
x = periodic_canvas.canvasx(0)
y = periodic_canvas.canvasy(0)
print(x, y)
periodic_canvas.create_image((450/2, 790/2), image=periodic_t)
#periodic_lbl['image'] = periodic_t

#create event callback for clicking on image
periodic_canvas.bind("<Motion>", lambda event: on_motion(event, list_of_icon_coords))
# periodic_lbl.bind("<Motion>", lambda event: on_motion(event, list_of_icon_coords))

#pack periodic table, frame into display
periodic_lbl_frame.pack(side=LEFT, fill=BOTH, expand=1, anchor=W, padx=10, pady=10)
periodic_canvas.pack()
#periodic_lbl.pack()

#create atom view box
view_lbl_frame = ttk.LabelFrame(root, text="View Box", height=300, width=300)
view_lbl = ttk.Label(view_lbl_frame)

#pack atom view box into output
view_lbl_frame.pack(side=RIGHT, fill=BOTH, expand=1, anchor=E, padx=10, pady=10)

#create coord-map object and populate list.
icon_map = PeriodicCoordinateMap()
list_of_icon_coords = icon_map.getIconCoords()
list_icons =  []
for item in list_of_icon_coords:
	list_icons.append(canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='blue' )
	# list_icons.append(periodic_canvas.create_rectangle(item[0],item[1],item[2],item[3], outline='blue'))




root.mainloop()
