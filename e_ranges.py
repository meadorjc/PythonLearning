#range is now a generator
#xrange is gone

#what is def?
#Its a function definition: followed by func name & parameters
#New local symbol table for that func only
#arguments are passed using call by value
#Sidenote: in Python (like C), procedures are funcs that dont return
# a value; or rather, return None
#A bit outdated but:
#http://docs.python.org/release/1.5.1p1/tut/functions.html

#fibonacci
def fib(n): #write up to n
  print("Print a Fibonacci series up to n")
  a, b = 0, 1
  while b < n:
    print(b,)
    a, b = b, a+b #so apparently, a+b is evaluated before b asgn2 a
#now call using fib(n)


#Now lets return it to a list
def fib2(n) : #return list of Fibonacci series up to n
  print("Return a list containing the fibonacci series up to n")
  result = []
  a, b = 0, 1
  while b < n:
    result.append(b)  #see below
    a, b = b, a+b
  return result

f100 = fib2(n = int(input("How many fib-nums? ")))

print("\n", f100)



def squares(g):
  for val in range(g):
    print ("working out ", val)
    yield val*val # what is yield? see e_iterables.py
  
for ref in squares(100):
  print("\n\nboard with ", ref," squares")
  
  