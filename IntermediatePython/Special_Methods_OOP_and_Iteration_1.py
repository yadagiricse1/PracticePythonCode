def range_gen(end):
    current=0;
    while current<end:
        yield current
        current+=1
    

for i in range_gen(5):
    print(i)
    

x=range_gen(5)


for i in x:
    print(i)
    

print(dir(x))

print(dir(range_gen))

print(dir(range_gen(5)))
print('for range------------')
print(dir(range))
print(dir(range(5)))
print(dir( i for i in range(5)))

# compare the above 3 dirs of range. in irst 2 we have __iter__ where as in third we also have __next__

# compare 