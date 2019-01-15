import statistics as s
from  statistics import stdev ,mode
from  statistics import variance as v
# to import every thing from statistics import *
x=input('what is ur name?')
print('Hello '+x)

example_list=[2,3,5,7,4,8,3,6,4,3,7,4,8,3,7,8]
x=s.mean(example_list)
print('Mean ',x)
x=s.median(example_list)
print('median ',x)
x=mode(example_list)
print('mode ',x)
x=v(example_list)
print('variance ',x)
x=stdev(example_list)
print('stdev ',x)
