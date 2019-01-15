
'''
x=(i for i in  range(5))
next(x)
x.__next__() # both methods are equivalent Underscore underscore next underscore underscore. thes types of methods are called dunder methods
for i in x:
    print(i)
    
print(dir(x))  # all inbulit methods associated to x  or the methods associated to generator 
'''

class range_example:
    def __init__(self,end,step=1):
        self.current=0
        self.end=end
        self.step=step
        
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current>=self.end:
            raise StopIteration()
        else:
            return_val=self.current
            self.current+=self.step
            return return_val
            

'''
for i in range_example(5):
    print(i)

'''
x=range_example(5)
x.__next__()
next(x)

for i in x:
    print(i)