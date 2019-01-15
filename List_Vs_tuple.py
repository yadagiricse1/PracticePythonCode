# touple vs list tuple is immutable where as list ismutable we can change values
x= 5,6,7,8
x= (5,6,7,8)
y=[5,6,7,8]
print(x[1])
print(y[2])
print(x)
print(y)

def exampleFun():
    return 15,6
    
x,y=exampleFun()

z=exampleFun()
print(x)
print(y)
print(z)