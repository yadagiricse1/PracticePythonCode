x = [1,2,3,4]
y = [7,8,3,2]
z = ['a','b','c','d']

for d,e in zip(x,y):
    print(d,e)
    
for d,e,f in zip(x,y,z):
    print(d,e,f)
       
print(zip(x,y,z))  # it will give a zip object
 
new_dict=dict(zip(x,y))
print(new_dict)

# the below code will show in tuples
for i in zip(x,y,z):
    print(i)

new_list=list(zip(x,y))
print(new_list)

# very challenging thing below with list comprehension

[print(x,y) for x,y in zip(x,y)] # in the list comprehension the variables (x,y ) are temp variables its value will be local to it
print(x)
# try to replicate the above scenario by normal for loop
for x,y in zip(x,y):
    print(x,y)
print('This is a puzzling case . remember it',x)       # here we get the o/p as 4 instead of list [1,2,3,4]
x = [1,2,3,4]
y = [7,8,3,2]
# tried above scenario with a , b temp variables
[print(a,b) for a,b in zip(x,y)] # in the list comprehension the variables (x,y ) are temp variables its value will be local to it
#print(a) #it will throw error as :NameError: name 'a' is not defined 

# if we replicate the above scenario with general for loop

for a,b in zip(x,y):
    print(a,b)
print('This is a puzzling case . remember it',a)   # the local variable in for loop can be used outside 

