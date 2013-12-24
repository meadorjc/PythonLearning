#Caleb Meador 12/23/2013 meadorjc at gmail.com
#adapted from http://www.wellho.net/mouth/4027_Collections-in-Python-list-tuple-dict-and-string-.html

#Collections in python:
# list, tuple, dict, string

#lists:
# start at 0
# mutable
# NOT an array
# NOT necessarily at successive mem. locs
# vector-esque (?)

#tuples
# start at 0
# NOT mutable - must rebuild and replace
# fast and straight-fwd, but inefficient to change

#dicts
#comarative to database tables w/ 2 columns,
# a key and a value
# similar to PHP's associative arrays
# similar to hashes in Perl
# fast access to data via keys, but not sortable

#strings
# collection of chars.
# NOT mutable: like tuples must rebuild to change

#constructors
# [] for list
# {} for dict
# () for tuple
# "" for string (or '' or """""")

#dereference operator = [] for any


#examples 
# from http://www.wellho.net/resources/ex.php?item=y111/coldem

#list - mutable
names = ["Charky", "Barkey", "Larson", "Sonlar"]

#tuple - immutable 
days = ("Monday", "Tuesday", "nextday", "Thorsday")

#dict - mutable and keyed by name
routes = {"X72":"NYC - Chicagogo", "272":"Berkley - Dallas",
          "XX2":"Chippenham - Trollbridg the pretty way"}
              
#string can be treated as a list of letters
place = "Well House Manor"

print(names[1])
print(days[1])
print(place[1])
print(routes["272"])

names[2] = "Graham"; names [3] = "Lisa"
for name in names:
  print("Give some black pudding to", name)
  
#days[3] = "Wednesday"

# Can't assign to tuplemember - previous line is a comment!
for day in days:
  print("We will learn on", day)
  
#place[0] = "B"
# Can't assign to string member - previous line is a comment
for letter in place:
  print("Gimme a ", letter)
  
routes["C"] = "St Ives - Cambridge" #Adds new - new key
routes["272"] = "Bowerhill - Bath" #Replaces - key exists
for route in routes.keys():
  print(route, "goes between", routes[route])

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  





