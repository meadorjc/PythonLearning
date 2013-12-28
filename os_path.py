#caleb meador meadorjc at gmail.com
#building up to adapation for database project formatting
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
    if headercheck.search(file.readline()) == None:
      print("\ttrue\n")
      file.seek(0)
      text = file.read()
      file.seek(0)
      file.write(header)
      file.write(text)
    else:
      print("\tfalse\n")
    # if size > sofar:
    # sofar = size
    # name = item
# print("Largest file is ", name, " at ", str(sofar), " bytes")
# changed = os.path.getmtime(name)
# reform = time.ctime(changed)
