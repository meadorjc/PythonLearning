#caleb meador meadorjc at gmail.com
#adapted from http://www.wellho.net/net/search.php4?search=python+path

import os, time, re
objects = os.listdir(".")
sofar = 0
headercheck = re.compile(r'^#C', re.IGNORECASE)
header = "#Caleb Meador meadorjc at gmail.com\n"
for item in objects:
  size = os.path.getsize(item)
  print(item, "\t", size, "\n")
  if (item != '.git' and item != 'README.md'):
    file = open(item, "r+")
    print(file.readline(), "\n")
    file.seek(0)
    if headercheck.search(file.readline()) != None:
      print("\ttrue\n")
      testfile = open("itemtest.py", "w") 
      file.seek(0)
      text = file.read()
      #file.seek(0)
      testfile.write(header)
      testfile.write(text)
    else:
      print("\tfalse\n")
    # if size > sofar:
    # sofar = size
    # name = item
# print("Largest file is ", name, " at ", str(sofar), " bytes")
# changed = os.path.getmtime(name)
# reform = time.ctime(changed)
r = {}                #dict constructor

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


