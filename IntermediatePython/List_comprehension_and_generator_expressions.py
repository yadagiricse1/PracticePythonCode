
xyz=[i for i in range(5)]
xyz1=(i for i in range(5))

print(xyz1)
abc=[]
for i in range(5):
    abc.append(i)
    
for i in xyz1:
    print(i)

'''
what is the difference between those 3 lines of code the first code is list comprehension it stores all theelements in the list xyz similarly for abc .
where as for xyz1 it stores the generator object instead of list we can use that list and iterate the generator object (it is just object )
'''


print(xyz)
print(abc)
    

# from below 2 statements the first one takes more memory and processing time
xyz = [i for i in range(50000000)]
print('done')
xyz =(i for i in range(50000000))
print(xyz)