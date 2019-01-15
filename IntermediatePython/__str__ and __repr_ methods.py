# __str__ is just like toString representation of object 

import datetime
print(datetime.datetime.now())  # this is nothing but __str__ representation of datetime.datetime.now()
print(str(datetime.datetime.now()))
print(repr(datetime.datetime.now()))