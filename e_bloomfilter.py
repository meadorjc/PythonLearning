#caleb meador 01/12/2014 meadorjc at gmail.com 
# adapted from tutorial at http://www.stavros.io/posts/bloom-filter-search-engine/?print

# pybloom.py
import sys
sys.path.insert(0, 'c:/python33x86/Lib/site-packages/pybloom-1.0.2/pybloom')

from pybloom import BloomFilter
import os
import re

POST_DIR = "c:/users/compy/documents/test/"
#read all docs within dir
docs = {post_name: open(POST_DIR + post_name).read() for post_name in os.listdir(POST_DIR)}

#create dict of {"doc name": "lowercase word set"} NOTE: set is a hashtable
split_docs = {name: set(re.split("\W+", contents.lower())) for name, contents in docs.items()}

#this creates a filter defining the number of words in each post (aka inverted index!)
#error rate is the probability of fals positive
filters = {}
for name, words in split_docs.items():
  filters[name] = BloomFilter(capacity = len(words), error_rate=0.1)
  for word in words:
    filters[name].add(word)



