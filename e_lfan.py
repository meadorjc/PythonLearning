#caleb meador 12/23/2013 meadorjc at gmail
#practice creating a dict from an input file
#adapted from tutorial http://www.wellho.net/resources/ex.php?item=y201/lfan

"""This is a program which reads a web server access log
file and counts the number of times each browser has visited,
outputting the resutls sorted by the number of accesses"""

##load modules

import re #regex? yes: http://docs.python.org/2/library/re.html
import os.path

##define functions
def byvisits(first, second):
  return counter[first] - counter[second]
  
try: 
  bytes = os.path.getsize("test.txt")
except:
  print ("\nSorry - input file not available\n")
  exit(1)
print("\nProcessing", int(bytes/1024), "kbytes")

##Open the file, prepare the match pattern and counter collection
fh = open("test.txt", "r") #r mode is read only; #w is for write
space = re.compile(r'\s+') #regex for whitespace? Yes obj. construct
counter = {}                #dict constructor

#Parse the file, counting the number of accesses from each host
for line in fh.readlines():
  parts = space.split(line) #create a list delim'd @ space
  #c-notation == counter{"parts[0]":"(parts[0]? parts[0]+1 : 0)"}
  counter[parts[0]] = counter.get(parts[0],0) + 1
  
#sort a list of the visiting hosts
#make a list of keys: converts
visitors = list(counter.keys())
#sort it using special trick for p33 http://blog.labix.org/2008/06/27/watch-out-for-listdictkeys-in-python-3
print(visitors)
visitors.sort()
print(visitors)
print(byvisits)

##print out the full reseults, count lines and visits
vh = 0; vi = 0
for browse_host in visitors:
  print(counter[browse_host], browse_host)
  vh += 1
  vi += counter[browse_host]

#output counts and end program

print("Total of ", vi, "visits from", vh, "hosts")


