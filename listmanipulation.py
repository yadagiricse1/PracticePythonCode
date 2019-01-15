x=[2,3,6,2,6,5,9,3,8,3,6,0,5]
x.append(2)
x.insert(2,99)
x.remove(0)
x.remove(x[3])
print(x)
print(x[2])
print(x[2:8])
print(x[-1]) # to get last element print(x[-2]) gives last but one elemnt
print("the number exist at ",x.index(99)) # to get index value of 99 if we try to check index value of an element which is not there it will throw exception
print("the number of times it is repeated",x.count(2))
x.sort()
print(x)
y=['giri','Anusha','puppy','arjun','Ravi'] # it will sort capital letter words first then small letter words
y.sort()
print(y)
