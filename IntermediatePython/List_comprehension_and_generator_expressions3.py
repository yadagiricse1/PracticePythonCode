'''
why onlyone is working while execuiting
xyz=(((i,ii) for ii in range(5)) for i in range(5))

for i in xyz:
    print(i)
    
for i in xyz:
    for ii in i:
        print(ii)
        
'''      
(print(i) for i in range(5))  # wont print as this is generator
# the above doesnt work for generator .noting will be printed if i make list comprehension it will work what if we asign generator to some variable?
[print(i) for i in range(5)]  # will print as this is list comprehension

print('done')
xyz=(print(i) for i in range(5))
# interesting thing below we didnt write print menthod in the below for loop but we will get output why because in the generator  each i =print(i)
for i in xyz:
     i

