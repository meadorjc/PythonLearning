import os, re, urllib.request
 
def main():
  
  
  starturl = """http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="""
  urlnum = "12345"
  
  followLinks(starturl, urlnum)
      
def followLinks(url, num):
    data = urllib.request.urlopen(url+num).read().decode('utf-8')
    print(data)
    parse = re.search(r'\d+', data)
    if parse:
      parseNum = parse.string[parse.start():parse.end()]
    else:           
      parseNum = ""
    followLinks(url, parseNum)
    
if "__main__" == __name__:
  main()
  