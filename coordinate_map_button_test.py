import imp
import sys
from tkinter import *
from PIL import Image
from PeriodicCoordinateMap import *
import pybel, openbabel as ob



sys.path.insert(0, 'c:\\users\\compy\\documents\\github\\pythonlearning')

def callback_click(atom_no):
  print ("clicked at", atom_no)
  create_new_atom(atom_no)
 
def create_new_atom(atom_no):
  molecule = ob.OBMol()
  atom = molecule.NewAtom()
  atom.SetAtomicNum(atom_no)
  py_mol = pybel.Molecule(molecule)
  drawObject(py_mol, picFrame)
    
def drawObject(mol, parent):
  mol.draw()


root = Tk()
lblFrame = LabelFrame(root, height=450, width=800)
lblFrame.pack(side=LEFT)

picFrame = Label(root, height=200, width =200)
picFrame.pack(side=LEFT)


#create map object and get list of coords
iconMap = PeriodicCoordinateMap()
iconList = iconMap.getIconCoords()

#create buttons and store list of button objects; sort by atom_no
button_list = iconMap.create_buttons(lblFrame, iconList, callback_click)
button_list.sort(key=lambda button:int(button["text"].split('\n')[0]))

for button in button_list:
  print(button["text"].split('\n'))
 


 
  
root.mainloop()