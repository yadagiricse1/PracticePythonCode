
'''
writing file 
'''

text='Sample text to save \nNew file'
saveFile=open('C:/Users/yadag/Desktop/PythonProgrammingPractice/examplefile.txt','w')
saveFile.write(text)
saveFile.close()
'''
append content  to file 
'''
appendMe='\nnew bit of information appended'
appendMeToo='\nExtra info appended'
appendFile=open('C:/Users/yadag/Desktop/PythonProgrammingPractice/examplefile.txt','a')
appendFile.write(appendMe)
appendFile.write(appendMeToo)
appendFile.close()
'''
read content from file
'''
readMe=open('C:/Users/yadag/Desktop/PythonProgrammingPractice/examplefile.txt','r').read()
print(readMe)

'''
read file in the form of list readlines() find difference between above lines and below lines output
'''
readMe=open('C:/Users/yadag/Desktop/PythonProgrammingPractice/examplefile.txt','r').readlines()
print(readMe)



