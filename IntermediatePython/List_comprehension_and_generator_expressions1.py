input_list = [5,6,20,2,1,15,6,7,10,12]

def dev_by_five(i):
    if i%5==0:
        return True
    else:
        return False
xyz=[i for i in input_list if dev_by_five(i)]  # list comprehension

print(xyz)
# the above code is list comprehension in a single line. it generally takes multiple liens of code
'''
xyz=[]
for i in input_list:
    if dev_by_five(i):
        xyz.append(i)        
print(xyz)
'''

xyz=(i for i in input_list if dev_by_five(i))  # generator
print(xyz) # here xyz is generator we get the results we should pass this in forloop
'''
for i in xyz:
    print(i)    
    '''
[print(i) for i in xyz] # the simplest way of writing above commented code one liner  . we are retirving from generator instead of list it saves meory generally it is slower

