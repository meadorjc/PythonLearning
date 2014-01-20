#caleb meador 1/19/2014 meadorjc at gmail.com
#testing for periodic table matching




class PeriodicCoordinateMap:

     
    def getIconCoords(self):

        MAX_GROUP_SIZE = 7
        
        #includes lanthanides & actinides at end
        group_size = [7, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 7]
        period_size = [2, 8, 8, 18, 18, 32, 32]
        lantha_acti_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        
        group_count = 18
        lantha_acti_count = 15

        #the following are arbitrary pixel coords based on periodic.gif  
        ele_icon_width = 37
        ele_icon_height = 37

        y_to_next_icon = 40
        x_to_next_icon = 40

        list_of_icon_coords = []

         
        #calculate std elements icons
        for group in range(group_count):
            y_origins = []
            x_origins = []
            y_end = []
            x_end = []
            
            #starting point of H icon
            initial_x = 63
            initial_y = 54
            for period in range(group_size[group]):
                
                initial_y += (MAX_GROUP_SIZE - group_size[group]) * y_to_next_icon

                x_origins.append((group*x_to_next_icon) + initial_x)
                y_origins.append((period*y_to_next_icon) + initial_y)


                x_end.append((group*x_to_next_icon) + initial_x + ele_icon_width)
                y_end.append((period*y_to_next_icon) + initial_y + ele_icon_height)

            #best way to return this? list_of_std_icons = zip(x_origins, y_origins, x_end, y_end)

        #calculcate lantha/acti element icons
        for group in range(lantha_acti_count):

             init_l_a_coords = [183,355]

             y_origins = []
             x_origins = []
             y_end = []
             x_end = []

             for period in range(lantha_acti_list[group]):
                x_origins.append((group*x_to_next_icon) + init_l_a_coords[0])
                y_origins.append((period*y_to_next_icon) + init_l_a_coords[1])


                x_end.append((group*x_to_next_icon) + init_l_a_coords[0] + ele_icon_width)
                y_end.append((period*y_to_next_icon) + init_l_a_coords[1] + ele_icon_height)

            #best way to return this? list_of_la_icons = zip(x_origins, y_origins, x_end, y_end)

        
        return list_of_icon_coords
    
icon_map = PeriodicCoordinateMap()

list_of_icon_coords = icon_map.getIconCoords()

for item in list_of_icon_coords:
    print (item)
    
