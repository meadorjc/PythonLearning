import os, re, urllib.request
 
def main():
  
  
  #count = 0;
  starturl = """http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="""
  #response = ""
  urlnum = "12345"
  
  followLinks(starturl, urlnum)
  
  # for count in range(400):
    # response = getResponse(starturl+urlnum)
    # urlnum = parseResponse(response)
    # print(count, ": ", response, "\t", urlnum, end="\n")
    
def followLinks(url, num):
    data = urllib.request.urlopen(url+num).read().decode('utf-8')
    print(data)
    parse = re.search(r'\d+', data)
    if parse:
      parseNum = parse.string[parse.start():parse.end()]
    else:           
      parseNum = ""
    followLinks(url, parseNum)
    
  
def parseResponse(response):
  
  urlnum = ""
  for letter in response:
      #print (letter, end=" ")
      if str.isdigit(letter):
        urlnum += letter
     
  print (urlnum) 
  
  return urlnum
  
def getResponse(starturl):
  
  response = urllib.request.urlopen(starturl)
  data = response.read()      # a `bytes` object
  print (data)
  return data.decode('utf-8') 
  
  
if "__main__" == __name__:
  main()
  