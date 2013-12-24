#Caleb Meador 12/23/2013 adapted from 
#http://www.wellho.net/mouth/4210_If-elif-elif-elif-multiway-selection-in-Python.html
# if trainsPerDay == 8:
#   a()
# elif trainsPerDay > 6 and trainsPerDay < 20:
#   b()
# elif trainsperDay > 6:
#   c()

#etc


#another example
#from adapted from http://www.wellho.net/resources/ex.php?item=y103/if4.py
faren = float(input("\nEnter a temp in celcius ")) * 9.0/5+32
print ("\nCelcius converts to", faren, "farenheit")

if faren > 212:
  print ("\nH20 state: Stream\n")
elif faren > 112:
  print ("\nH20 state: Very hot water\n")
elif faren > 32:
  print ("\nH20 state: water\n")
else:
  print ("\nH20 state: ice\n")
  
  print ("\nH20 State Program Completed\n")
