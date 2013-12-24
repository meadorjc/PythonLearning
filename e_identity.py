#Caleb Meador 12/23/2013 meadorjc @ gmail.com
#adapted from http://www.wellho.net/mouth/4092_Identity-in-Python.html

#Difference between "the same," "equal," and "identical."
print("\n\nMutable objects: lists etc.\n")
a = [10]  #list
b = [10]  #different list
c = a     #another name for list a

print( a==b )     #equal? true

print ( a is b )  #same?  false

print ( a is c )   #same? true

#Ok, so a list is a mutable object...therefore it cannot the object
#can change at different instantiations.  However, immutable objects
#such integers, floats, strings, and tuples must be recreated with a
#new object to change them; they are only bound(stored) once for
#efficiency (I assume this means different object addresses?)
#Therefore, the IS keyword will produce different results.
print("\n\nImmutable objects: integer, floats etc.\n")

a = 10
b = 10
c = a
print (a == b)  #equal? true

print (a is b)  #same? true a is the same object as b!

print (a is c) #same? true
