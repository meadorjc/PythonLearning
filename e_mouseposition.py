#caleb meador 1/14/2014 meadorjc at gmail.com
#adapted from http://stackoverflow.com/questions/19529460/tkinter-program-displays-the-location-of-the-mouse-pointer-on-the-canvas-when-th



from tkinter import *                
width = 250
height = 250
class MainGUI:
    def __init__(self):
        window = Tk() 
        window.title("Display Cursor Position")
        self.canvas = Canvas(window, bg = "white", width = width, height = height)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.processMouseEvent)
        self.canvas.focus_set()
        window.mainloop()
    def processMouseEvent(self, event):
      mouse_coordinates= str(event.x) + ", " + str(event.y)
      self.canvas.create_text(event.x, event.y, text = mouse_coordinates)
        #self.canvas.insert(cursorPoint)
MainGUI()