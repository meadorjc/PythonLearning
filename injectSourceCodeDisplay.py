#caleb meador meadorjc at gmail.com 3/12/2014
#Recursively search through folders for .aspx and aspx.cs files and 
# inject code to display the page source code
#
# see what buttons this source code injected: http://jcmeador.azurewebsites.net/
# under AdvWebDev home / about
#


import os, re, sys, string
from os.path import join, getsize


#global consts
EXT_PART = 2
FILE_PART = 0
HEAD_TAG = '(<\/head>)'
FORM_TAG = '(<\/form>)'
CONTENT_TAG = '(<\/asp\:Content>)' # <asp:Content>
MASTER_FILE = r"MasterPageFile"
END_BRACKET = '\s*\}\s*(\})\s*\Z'
END_BRACKET_ALT = '(\})\Z'
SKIP_TAGS = (r"syntaxhighlighter", r"btnCodeDisplay", r"btn")
VIEW_EXTS = ('aspx', 'master')
CONTROL_EXTS = ('aspx.cs', 'master.cs')
CLASS_EXTS = ('cs')
STYLE_EXTS = ('css')



#syntaxhighlighter files at master head
def injectMasterHead(fileName, funcNameExt):
  return """
    <%-- meadorjc: This code was inserted automatically using injectSourceCodeDisplay.py --%>
    <script src="<%# ResolveUrl("~/packages/syntaxhighlighter/scripts/shCore.js") %>"></script>
    <script src="<%# ResolveUrl("~/packages/syntaxhighlighter/scripts/shBrushCSharp.js") %>"></script>
    <link href="<%# ResolveUrl("~/packages/syntaxhighlighter/styles/shCoreDefault.css") %>" rel="stylesheet" />
    <script type="text/javascript">SyntaxHighlighter.all();</script>
    """

#syntaxhighlighter files at aspx head
def injectAspxHead(fileName, funcNameExt):
  return """
    <%-- meadorjc: This code was inserted automatically using injectSourceCodeDisplay.py --%>
    <script src="<%= ResolveUrl("~/packages/syntaxhighlighter/scripts/shCore.js") %>"></script>
    <script src="<%= ResolveUrl("~/packages/syntaxhighlighter/scripts/shBrushCSharp.js") %>"></script>
    <link href="<%= ResolveUrl("~/packages/syntaxhighlighter/styles/shCoreDefault.css") %>" rel="stylesheet" />
    <script type="text/javascript">SyntaxHighlighter.all();</script>
    """

#button to display aspx-form source code
def injectAspxForm(fileName, funcNameExt):
  return """
    <%-- meadorjc: This code was inserted automatically using injectSourceCodeDisplay.py --%>
    <asp:Button ID="btnCodeDisplay"""+funcNameExt+"""" runat="server" Text="Display """+re.sub('\_', '.', funcNameExt[1:])+""" Code" onClick="btnCodeDisplay"""+funcNameExt+"""_Click" CausesValidation="false"/>
    <asp:Label ID="lblCodeDisplay"""+funcNameExt+ """" runat="server" Text="" Visible ="false">
    </asp:Label>
    <style type="text/css">
    #btnCodeDisplay"""+funcNameExt+""" { margin-top:1em !Important; margin-right: 50% !Important;}
    </style>  
    """
#button to display aspx-form source code
def openCodeDDL(fileName, funcNameExt):
  return """
    <%-- meadorjc: This code was inserted automatically using injectSourceCodeDisplay.py --%>
    <asp:DropDownList ID="ddlCodeDisplay"""+funcNameExt+"""" runat="server" AutoPostBack="True" OnSelectedIndexChanged="ddlCodeDisplay"""+funcNameExt+"""_SelectedIndexChanged">
    """    
    <style type="text/css">
    #ddlCodeDisplay"""+funcNameExt+""" { margin-top:1em !Important; margin-right: 50% !Important;}
    </style>  
def injectCodeListItems(filename, funcNameExt)
  return """
  <asp:ListItem Text="name" Value="&quot;~/AdvWebDev/&quot;"></asp:ListItem>
            </asp:DropDownList>

"""

def closeCodeDDL            
            
# C# source code to manipulate button, get and display source code
#formerly string csFileName = Page.Server.MapPath(Page.AppRelativeVirtualPath + ".cs");
def injectCSCode(fileName, funcNameExt):
  return """
    /*meadorjc: This code was inserted automatically using injectSourceCodeDisplay.py*/
    private string csCode = null;
    
    protected String getCode(string url)
    {

      string csFileName = ResolveUrl(url);
      System.IO.StreamReader csFile = new System.IO.StreamReader(csFileName);
      string csCode = csFile.ReadToEnd();
      
      csFile.Close();
      
      return csCode;

    }
    protected void btnCodeDisplay"""+funcNameExt+"""_Click(object sender, EventArgs e)
    {
             
      if (lblCodeDisplay"""+funcNameExt+""".Visible == false)
      {
        lblCodeDisplay"""+funcNameExt+""".Visible = true;
        btnCodeDisplay"""+funcNameExt+""".Text = "Hide """+re.sub('\_', '.', funcNameExt[1:])+""" Source Code";
      }
      else
      {
        btnCodeDisplay"""+funcNameExt+""".Text = "Display """+re.sub('\_', '.', funcNameExt[1:])+""" Source Code";
        lblCodeDisplay"""+funcNameExt+""".Visible = false;
      }
    }
    
    protected void ddlCodeDisplay"""+funcNameExt+"""_SelectedIndexChanged(object sender, EventArgs e)
    {
      if (csCode == null)
      {
        csCode = getCode(ddlCodeDisplay"""+funcNameExt+""".SelectedValue.ToString());
        lblCodeDisplay"""+funcNameExt+""".Text = ("<pre class='brush: csharp;'/>"+csCode+"</pre>");
      }
    }
"""
#inject code into pre-existing code @ specific regex match objects
def injectCode(matchObject, functName, fileName, funcNameExt):
    if matchObject:
      return matchObject.string[matchObject.pos:matchObject.start(1)-1]+functName(fileName, funcNameExt)+matchObject.string[matchObject.start(1):matchObject.endpos]

#make a backup of original file
def backupFile(fileObject, filePath):
  fileData = fileObject.read()
  oldFile = open(filePath+".old", "w")
  oldFile.write(fileData)
  oldFile.close()
 
#multiple matches happen; get the last one found
def getLastMatch(regexObject, code):
    finalMatch = None
    matchIter = regexObject.finditer(code)
    for match in matchIter:
      finalMatch = match
    return finalMatch

#any injected code already found?
def injectedCodeCheck(code):
  for tag in SKIP_TAGS:
    match = re.search(tag, code)
    if match:
      print(match.group(0))
      return True
  return False

#always inject HEAD code, and either ASPX FORM code or MASTER file code
def putAspxCode(funcNameExt, filepath):
        
      aspxFile = open(filepath, "r+")
      aspxCode = aspxFile.read()
     
      if injectedCodeCheck(aspxCode):
        aspxFile.close()
        print("CODE PREVIOUSLY MODIFIED: CONTINUING")
        return

      backupFile(aspxFile, filepath)
      
      #EITHER FORM or MASTER TAG
      print("\nInserting script links")

      #inject references @ </head>
      aspxHead = re.compile(HEAD_TAG)
      aspxHeadMatches = aspxHead.search(aspxCode)
    
      if re.search(MASTER_FILE, aspxCode):
        if aspxHeadMatches:
          aspxCode = injectCode(aspxHeadMatches, injectMasterHead, filepath, funcNameExt)
        aspxContentTag = re.compile(CONTENT_TAG)
        matchObject = getLastMatch(aspxContentTag, aspxCode)
      else:
        if aspxHeadMatches:
          aspxCode = injectCode(aspxHeadMatches, injectAspxHead, filepath, funcNameExt)
        aspxFormTag = re.compile(FORM_TAG)
        matchObject = aspxFormTag.search(aspxCode)
      print("\nInserting aspx code")
      aspxCode = injectCode(matchObject, injectAspxForm, filepath, funcNameExt)
      
      class_filepath_list = []
      root_list = filepath.split("\\")
      app_code_path = root_list[1]+"\\App_Code\\"
      for root, dirs, files in os.walk(app_code_path):
        for class_file in files:
          class_file_path = os.path.join(root, class_file)
          aspxCode = injectCode(matchObject, injectClassButtons, class_file_path, funcNameExt)
          
      
      #go to start and rewrite file
      aspxFile.seek(0)
      aspxFile.write(aspxCode)
      aspxFile.close()
      
#always inject HEAD code, and either ASPX FORM code or MASTER file code
def putClassCode(funcNameExt, filepath):
        
      file = open(filepath, "r+")
      code = file.read()
     
      if injectedCodeCheck(code):
        file.close()
        print("CODE PREVIOUSLY MODIFIED: CONTINUING")
        return

      backupFile(aspxFile, filepath)
      
      #EITHER FORM or MASTER TAG
      print("\nInserting script links")

      #inject references @ </head>
      aspxHead = re.compile(HEAD_TAG)
      aspxHeadMatches = aspxHead.search(aspxCode)
    
      if re.search(MASTER_FILE, aspxCode):
        if aspxHeadMatches:
          aspxCode = injectCode(aspxHeadMatches, injectMasterHead, filepath, funcNameExt)
        aspxContentTag = re.compile(CONTENT_TAG)
        matchObject = getLastMatch(aspxContentTag, aspxCode)
      else:
        if aspxHeadMatches:
          aspxCode = injectCode(aspxHeadMatches, injectAspxHead, filepath, funcNameExt)
        aspxFormTag = re.compile(FORM_TAG)
        matchObject = aspxFormTag.search(aspxCode)
      print("\nInserting aspx code")
      aspxCode = injectCode(matchObject, injectAspxForm, filepath, funcNameExt)

      #go to start and rewrite file
      aspxFile.seek(0)
      aspxFile.write(aspxCode)
      aspxFile.close()
      
#Put CS code after before last bracket.
def putCsCode(funcNameExt, filepath):      
      
      funcNameExt = funcNameExt.rstrip(".cs")

      csFile = open(filepath, "r+")
      csCode = csFile.read()
      
      if injectedCodeCheck(csCode):
        csFile.close()
        print("CODE PREVIOUSLY MODIFIED: CONTINUING")
        return
      
      backupFile(csFile, filepath)
      
      #find "}\n}\nEOF" or something like it
      endBracket = re.compile(END_BRACKET_ALT)
      
      print("\nInserting CS code")
      
      #inject references
      csMatch = getLastMatch(endBracket, csCode)
      if (csMatch):
        csCode = injectCode(csMatch, injectCSCode, filepath, funcNameExt)

      
      #go to start and rewrite file
      csFile.seek(0)
      csFile.write(csCode)
      csFile.close()

def getClassLists(path):
  site_list = []
  temp_file_list = []
  list_of_file_lists = []
  
  for root, dirs, files in os.walk(path):
    root_split = root.split("\\")
    if len(root_split) > 1 and root_split[1] not in site_list:
      site_list.append(root_split[1])
      if temp_file_list != []:
        list_of_file_lists.append(temp_file_list)
      temp_file_list = []
    for file in files:
      file_ext = file.partition(".")[2]
      if  file_ext in CLASS_EXTS:
        temp_file_list.append(file)
  
  return [site_list, list_of_file_lists]

      
def main():
  filecount = 0
  path = "."
  
  if len(sys.argv) > 1:
    path = sys.argv[1]
    
  class_list = []
  class_list = getClassLists(path)
  
  #recursively move through files
  for root, dirs, files in os.walk(path):
    for name in files:
   
      filepath = os.path.join(root, name)         
      #rpartition() maybe?  .split(".")
      namePart = name.partition(".")
      
      filecount += 1
      print("\n\t", namePart, "FileCount", filecount)
       
      #create extension "_fileName_ext"
      funcNameExt = '_'+namePart[FILE_PART]+'_'+namePart[EXT_PART]
      funcNameExt = re.sub('\-', '', funcNameExt)
      
      #insert code in .aspx and .master files
      if namePart[EXT_PART] in VIEW_EXTS:
        putAspxCode(funcNameExt, filepath)
      
      #insert code in aspx.cs and master.cs files
      if namePart[EXT_PART] in CONTROL_EXTS:
        putCsCode(funcNameExt, filepath)
      
      #To be implemented later to test classes, etc.
      #if namePart[EXT_PART] in CLASS_EXTS:
        # putClassCode(funcNameExt, filepath)

        
      
        
if "__main__" == __name__:
  main()

    