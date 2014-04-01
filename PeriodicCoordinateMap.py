#caleb meador 1/19/2014 meadorjc at gmail.com
#testing for periodic table matching

from tkinter import *
import functools

def howdy():
  print("hi there")

class PeriodicCoordinateMap:
        
    MAX_GROUP_SIZE = 7
    
    #includes lanthanides & actinides at end
    atom_name = [ 'H', 'He', 'Li', 'Be', 'B', 'C', 'N',
                  'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si',
                  'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc',
                  'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co',
                  'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As',
                  'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y',
                  'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh',
                  'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb',
                  'Te', 'I', 'Xe', 'Cs', 'Ba', 'La',
                  'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu',
                  'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm',
                  'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re',
                  'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl',
                  'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr',
                  'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np',
                  'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es',
                  'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db',
                  'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg',
                  'Cn', 'Uut', 'Fl', 'Uup', 'Lv', 'Uus', 'Uuo']

    group_sizes = [7, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 7]
    period_size = [2, 8, 8, 18, 18, 32, 32]
    lantha_acti_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    
    total_group_count = 18
    lantha_acti_count = 15

    #the following are arbitrary pixel coords based on periodic.gif  
    ele_icon_width = 37
    ele_icon_height = 37

    y_to_next_icon = 40
    x_to_next_icon = 40

    list_of_icon_coords = []
    
    def getIconCoords(self):
 
        #calculate std elements icons
        for group in range(self.total_group_count):
            y_origins = []
            x_origins = []
            y_end = []
            x_end = []
            
            #starting point of H icon
            initial_x = 63
            initial_y = 54 +((self.MAX_GROUP_SIZE - self.group_sizes[group]) * self.y_to_next_icon)
            
            for period in range(self.group_sizes[group]):
                
                x_origins.append((group*self.x_to_next_icon) + initial_x)
                y_origins.append((period*self.y_to_next_icon) + initial_y)


                x_end.append((group*self.x_to_next_icon) + initial_x + self.ele_icon_width)
                y_end.append((period*self.y_to_next_icon) + initial_y + self.ele_icon_height)
            
            
                self.list_of_icon_coords.append((x_origins[period], y_origins[period], x_end[period], y_end[period]))
        
        #calculcate lantha/acti element icons
        for group in range(self.lantha_acti_count):
             
             #initial lantha/acti element coords
             init_l_a_coords = [183,355]

             y_origins = []
             x_origins = []
             y_end = []
             x_end = []

             for period in range(self.lantha_acti_list[group]):
                x_origins.append((group*self.x_to_next_icon) + init_l_a_coords[0])
                y_origins.append((period*self.y_to_next_icon) + init_l_a_coords[1])


                x_end.append((group*self.x_to_next_icon) + init_l_a_coords[0] + self.ele_icon_width)
                y_end.append((period*self.y_to_next_icon) + init_l_a_coords[1] + self.ele_icon_height)

                self.list_of_icon_coords.append((x_origins[period], y_origins[period], x_end[period], y_end[period]))

        
        return self.list_of_icon_coords
    
        
    def create_buttons(self, _parent, list_of_icon_coords, callback_click):
      count = 0
      
      self.list_of_icon_coords.sort(key=lambda item:item[1])
      
      #create a list of all buttons
      button_list = []
      
      for item in self.list_of_icon_coords:
        count += 1
        b_x_coord = item[0]
        b_y_coord = item[1]
        b_height = 37
        b_width = 37
        
        if count == 57 or count == 75:
          continue
        
        #58 -> 72 and 74->89
        elif count > 57 and count <= 74:
          atom_no = count + 14
        
        #76->104 and 90->118
        elif count > 75 and count <= 90:
          atom_no = count + 28
        
        #91-> 57  and 104->71
        elif count > 90 and count <= 105:
          atom_no = count - 34
                 
        #106->89 and 120->103
        elif count > 105 and count <= 120:
          atom_no = count - 17
        else:
          atom_no = count;

        b = Button(_parent, bg='grey', highlightcolor='green', bd=2, text=str(atom_no)+'\n'+self.atom_name[atom_no-1], fg="black", padx=2, pady=2, command=functools.partial(callback_click, atom_no))
        button_list.append(b)
        b.place(x=b_x_coord, y=b_y_coord, height=b_height, width= b_width)
      
      return button_list
         
    
    

#for testing        
#icon_map = PeriodicCoordinateMap()
#list_of_icon_coords = icon_map.getIconCoords()
#print(type (list_of_icon_coords))
#for item in list_of_icon_coords:
#  print(item)
    
