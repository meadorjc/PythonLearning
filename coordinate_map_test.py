import imp
import sys
sys.path.insert(0, 'c:\\users\\compy\\documents\\github\\pythonlearning')
from tkinter import *
from PIL import Image
from PeriodicCoordinateMap import *


root = Tk()
canv = Canvas(root, height=450, width=800)
canv.pack()
icon_map = PeriodicCoordinateMap()
icon_list = icon_map.getIconCoords()
icon_map.create_icons(canv, icon_list)


root.mainloop()