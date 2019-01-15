names=['Giri','Ravi','Anusha','Shilpa']

'''for name in names:
    #print('Hello There ,'+name)
    print(''.join(['Hello There ,',name]))'''
 
    
 # compaared to above 2 ways in forloop the below join is more feasible and low processing         
#print(','.join(names))



#print(''.join(names))

'''
import os    
location_of_files = 'C:/Users/yadag/Desktop/PythonProgrammingPractice'
file_name = 'examplefile.txt'

print(location_of_files+'/'+file_name)
# in the below code python itself takes care of concating the strings with slashes 
with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())
    '''
who='Gary'
how_many=12

print(who ,'bought',how_many,'apples today')

print('{} bought {} apples today!'.format(who, how_many)) # this is the corect way of formating strings than the previous one

#print('{0} bought {1} apples today!'.format(who, how_many)) # this is in python 2


























