#Caleb Meador meadorjc at gmail.com
print('hi')
print("now we got it")
print("in python 3, () are required to use print")

#comment.

my_name = 'Zed A. Shaw'
my_age = 35 
my_height = 180


print("Let's talk about %s.", my_name)

print("."*80)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print (end1 + end2 + end3 + end4 + end5 + end6+
end7 + end8 + end9 + end10 + end11 + end12)

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print ("Here are the days: ", days)
print ("Here are the months: ", months)

print ("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)



print("Escape\t	What it does.")
print("\\\t	Backslash ()")
print("\'\t	Single-quote (')")
print('\"\t	Double-quote (")')
print("\t\a	ASCII bell (BEL)")
print("\t\b	ASCII backspace (BS)")
print("\t\f	ASCII formfeed (FF)")
print("\t\n	ASCII linefeed (LF)")
#print("\t\N{name}	Character named name in the Unicode database") 
print("\t(Unicode only)")
print("\t\r ASCII	Carriage Return (CR)")
print("\t\t ASCII	Horizontal Tab (TAB)")
print("\t\u2551	Character with 16-bit hex value xxxx (Unicode only)")
#print("\t\U00253131	Character with 32-bit hex value xxxxxxxx") 
print("\t(Unicode only)")
print("\t\v	ASCII vertical tab (VT)")
print("\t\ooo	Character with octal value ooo")
print("\t\x122	Character with hex value hh")
print("Her\te's a tiny piece of fun code to try out:")

while True:
    for i in ["/","-","|","\\","|"]:
        print(i, "\r")



