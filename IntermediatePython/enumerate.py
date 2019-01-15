example = ['left','right','up','down']
'''
for i in range(len(example)):
    print(i, example[i])
   ''' 
    
for i,j in enumerate(example):
    print(i,j)
    
new_dict=dict(enumerate(example))
print(new_dict)

example_dict = {'left':'<','right':'>','up':'^','down':'v',}
[print(i,j) for i,j in enumerate(example_dict)]  # this will give just keys is not effective or helpfull
