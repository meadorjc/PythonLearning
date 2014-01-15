#caleb meador meadorjc at gmail.com
#Change basic types of python 2x syntax to 3x 
#
#building up to adapation for database project formatting
#some code adapted from http://www.diveintopython3.net/porting-code-to-python-3-with-2to3.html


import os, re, sys, string
from os.path import join, getsize

#regex object checks that file ends in sql or mysql and is a lab/exercise
py2print = re.compile(r"""
 \bprint\b        #word must begin with print (i.e. not 'imprintable', etc)
 
 (?!            #begin conditional; if string is not
 \s* [(]        #whitespace and (
 |              #or
 \s* [>>]       #whitespace and >>
 )              #end conditional
                #then
 (              #group \1 begin
 .*             #then select all after print()
 )              #group \1 end
 
 """, re.VERBOSE)
 
py2printpipe = re.compile(r"""
 \bprint\b      #word must begin with print(i.e. not 'imprintable', etc)
 \s* >>       #0-n whitespace and >> chars
 \s*          #0-n whitespace
 
 (            #begin group \1  
 .*?          #select anything non-greedy
 )            #end group \1
 [,]          #non-greedy * delimiter
 
 (            #begin group \2
 .*           #select anything greedy
 [^,]         #dont include the last ',' char
 )            #end group \2
 [,?]$        #may or may not be ',' @ end 
 """, re.X | re.M) #verbose and multiline mode


filecount = 0
matchcount = 0
   
for root, dirs, files in os.walk('.'):
  #print(root, "~", dirs, "~", files, "~\n\n") #debug
  for name in files:
    if name.rpartition(".")[2] == 'py':               #test filename
      filecount += 1
      filepath = os.path.join(root, name)             #create pathstring
      print('\n\n************************************\n',filepath)
      infile = open(filepath, "r+")
      
      code = infile.read()
     
      results = py2print.findall(code)
      
      matchcount += len(results)
      
      #print( out results before changing)
      for match in results:
        print(r'print(', match, ')\n')
        
      results = py2printpipe.findall(code)
      matchcount += len(results)
      print()
      for match in results:
        print('print(', match[1], ', file=', match[0],')\n')
      
      print('Filecount:', filecount, '\nMatchcount: ', matchcount)
      
      #replace any iteration of py 2 print( with print())
      #old: print( "" | var)
      #new: print ("") | (var)
      code = py2print.sub(r'print(\1)', code)


      #replace any iteration of augmented print( assignment (>>))
      #old print( 1, 2, 3, file=sys.stderr)
      #new print(1, 2, 3, file=sys.std)
      code = py2printpipe.sub(r'print(\2, file=\1)', code)
      
      #go to start and rewrite file
      infile.seek(0)
      infile.write(code)
      
#      header = "/*Caleb Meador meadorjc at gmail.com*/\n"
#      headercheck = re.compile(r'^[/][*]C', re.IGNORECASE)  #regex header-test
      # try:                                                  #unicode error handle
        # print(infile.readline())
        # infile.seek(0)
      # except UnicodeEncodeError:
        # print("unprintable character: continuing")
        
      #if headercheck.search(infile.readline()) == None: #search for any sig-head
        # print("\tNo signature header detected\n\n")
        # infile.seek(0)
        # text = infile.read()
        # # infile.seek(0)      #uncomment these 3 to write a signature
        # # infile.write(header)
        # # infile.write(text)
        # infile.seek(0)
        # try:                                                #unicode error handle
          # print(infile.readlines(3))
          # infile.seek(0)
        # except UnicodeEncodeError:
          # print("unprintable character: continuing")
          
      # else: #if a signature exists, leave it alone
        # print("\tSignature header detected\n")
  
  

#execute    
os.walk('.')









# # sofar = 0
# # headercheck = re.compile(r'^#C', re.IGNORECASE)
# # header = "#Caleb Meador meadorjc at gmail.com\n"
# # for item in objects:
  # # size = os.path.getsize(item)
  # # print(item, "\t", size, "\n")
  # # if (item != '.git' and item != 'README.md'):
    # # file = open(item, "r+")
    # # print(file.readline(), "\n")
    # # file.seek(0)
    # # if headercheck.search(file.readline()) == None:
      # # print("\ttrue\n")
      # # file.seek(0)
      # # text = file.read()
      # # file.seek(0)
      # # file.write(header)
      # # file.write(text)
    # # else:
      # # print("\tfalse\n")
    # # if size > sofar:
    # # sofar = size
    # # name = item
# # print("Largest file is ", name, " at ", str(sofar), " bytes")
# # changed = os.path.getmtime(name)
# # reform = time.ctime(changed)
