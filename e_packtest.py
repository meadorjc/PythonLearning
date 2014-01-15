#caleb meador 1/08/2014 meadorjc at gmail.com
#taken from http://effbot.org/tkinterbook/pack.htm


from tkinter import *

root = Tk()

listbox = Listbox(root)
#fill both horizontally and vert; X = horiz; Y = vert
#expand = assign adt'l space 
listbox.pack(fill=BOTH, expand=1, side=LEFT)

for i in range(20):
  listbox.insert(END, str(i))

#put multiple widgets in a column with pack

w = Label(root, text="red", bg="red", fg="white")
w.pack(side=LEFT,fill=X)#fill=X => make as wide as parent
w = Label(root, text="green", bg="green", fg="black")
w.pack(side=LEFT,fill=X)
w = Label(root, text="blue", bg="blue", fg="white")
w.pack(side=LEFT,fill=X)

#put multiple widgets in a row with side option and fill=Y

w = Label(root, text="red", bg="red", fg="white")
w.pack(side=RIGHT, fill=Y)#fill=X => make as wide as parent
w = Label(root, text="green", bg="green", fg="black")
w.pack(side=RIGHT, fill=Y)
w = Label(root, text="blue", bg="blue", fg="white")
w.pack(side=RIGHT, fill=Y)
  
  
mainloop()