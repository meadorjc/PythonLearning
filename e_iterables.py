#Caleb Meador meadorjc at gmail.com
#taken from
#http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained

#Everything you can use "for X in Y:" on is an iterable
#lists, strings, files

print("\n\nIterable")
mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in mylist:
  print(i*i)
  
#generators
#You can only iterate over them once
#They do not store the values in memory; generated on the fly
print("\n\nGenerator")
mygenerator = (x*x for x in range(11))
for i in mygenerator:
  print(i)
  
#yield
#A keyword that is used like return, except the function will return
# a generator

def createGenerator():
  mylist = range(11)
  for i in mylist:
    yield i*i
    
mygenerator = createGenerator() #create a generator
print("\n\n", mygenerator,"\n\n") #mygenerator is an OBJECT!
 
print("\n\nYields")

for i in mygenerator:
 print(i)
 
#NOTE: When you call the function, the code you have written in the function body DOES NOT RUN!
#The function returns the generator object

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 