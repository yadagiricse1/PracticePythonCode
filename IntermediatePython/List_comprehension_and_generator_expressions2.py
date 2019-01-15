'''
big list comprehensions will run out of memory where as big generators will run out of time

ex:
   ([[i,ii] for ii in range(500000000000000)] for i in range(500000000000000)) 
    (((i,ii) for ii in range(500000000000000)) for i in range(500000000000000))
'''

#[[print(i,ii) for ii in range(5)] for i in range(5)]

# the above code is same as below for loop inside a for loop

'''
[print(i,ii) for ii in range(5)] inner loop 
the outer loop for i in range(5)

'''
'''
for i in range(5):
    for ii in range(5):
        print(i,ii)
        
'''
# saving data in the form of touples in xyz
xyz=[[(i,ii) for ii in range(5)] for i in range(5)]
print(xyz)

# saving data in the form of list in xyz
xyz=[[[i,ii] for ii in range(5)] for i in range(5)]
print(xyz)

# for the above list we can create generator expression by changing outer brackets. Then iterate the generator 
xyz=([[i,ii] for ii in range(5)] for i in range(5))
print(xyz)
# iterate generator
#print([i for i in xyz])

for i in xyz:
    print(i)
    
# below is the interesting thing generator inside a generator
xyz=(((i,ii) for ii in range(5)) for i in range(5))

for i in xyz:
    print(i)
    
for i in xyz:
    for ii in i:
        print(ii)
