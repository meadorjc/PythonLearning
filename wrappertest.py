class Wrapper(object):
    def __init__(self,wrapped,*callbacks):
        self.wrapped = wrapped
        self.callbacks = callbacks

    def __getattr__(self,name):
        res = self.wrapped.__getattribute__(name)
        if not callable(res):
            return res
        def wrap(*args,**kwargs):
            for c in self.callbacks:
                c(self.wrapped,f,*args,**kwargs)
            return res(*args,**kwargs)
        return wrap

    def __str__(self):
        return self.wrapped.__str__()

#def type_try(f, v, ign):
 # return lambda f,v,ign: called.append((f,v))

  #in this example I will keep a record of each call performed on a list
called = []
#this is the list
a = []
f = list.append
#print(type_try(f, v, ign))
#and this is the wrapped list
w = Wrapper(a,lambda f,v,ign: called.append((f,v)) )
#I append an element to the wrapper
w.append(1)
#and I can see that it modify the original list
print (a)
#the print of the wrapped is well behaved, having defined the __str__ function
print (w)
#and we can see which function we called and which were the parameters
print (called)