#caleb meador meadorjc at gmail.com 3/12/2014
#Recursively search through folders for .aspx and aspx.cs files and 
# inject code to display the page source code
#
#building up to adapation for database project formatting
#some code adapted from http://www.diveintopython3.net/porting-code-to-python-3-with-2to3.html

import os, re, sys, string
from os.path import join, getsize

#regex object checks that file ends in sql or mysql and is a lab/exercise
# formEndTag = re.compile(r"""
       # \b</form>\b        #find the closing form tag""", re.VERBOSE)
 
# headEndTag = re.compile(r"""
 # \b</head>\b    #find the closing head tag""", re.X | re.M) #verbose and multiline mode


filecount = 0
matchcount = 0
   
for root, dirs, files in os.walk('.'):
  print(root, "~", dirs, "~", files, "~\n\n") #debug
  for name in files:
    if name.rpartition(".")[4] == 'aspx':               #test filename
      filecount += 1
      filepath = os.path.join(root, name)             #create pathstring
      print('\n\n************************************\n',filepath)
      infile = open(filepath, "r+")
      
      code = infile.read()
      
      matches = re.subn(r'</head>', injectAspxHead, code)
      
      print(matches)
      
      matches = re.subn(r'</form>', injectAspxCode, code)  

      print(matches)

      print()
      
      print('Filecount:', filecount, '\nMatchcount: ', matchcount)
      
      code = py2printpipe.sub(r'print(\2, file=\1)', code)
      
      #go to start and rewrite file
      infile.seek(0)
      infile.write(code)
      
#execute    
os.walk('.')

def injectAspxHead():
  return 
    """
    <script src="syntaxhighlighter/scripts/shCore.js"></script>
    <script src="syntaxhighlighter/scripts/shBrushCSharp.js"></script>
    <link href="syntaxhighlighter/styles/shCoreDefault.css" rel="stylesheet" />
    <script type="text/javascript">SyntaxHighlighter.all();</script>
    </head>
    """

def injectAspxHead():
  return """
    <asp:Button ID="btnCodeDisplay" runat="server" Text="Display Source Code" onClick="btnCodeDisplay_Click" CausesValidation="false"/>
    <asp:Label ID="lblCodeDisplay" runat="server" Text="<pre class='brush: csharp;'/>" Visible ="false">
    </asp:Label>
    <style type="text/css">
    #btnCodeDisplay { margin-top:1em !Important; margin-right: 50% !Important;}
    </style>
    </form>   
    """





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
