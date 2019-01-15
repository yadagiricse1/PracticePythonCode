import sys
import logging

def error_handling():
    return '{}. {}, line: {}'.format(sys.exc_info()[0],
                                         sys.exc_info()[1],
                                         sys.exc_info()[2].tb_lineno)

'''
try:
    a+b
except Exception as e:
    print(str(e))
    
in the above code we are able to handle exception but dont knwo where it occure 
if we are writing big applications it will be good if we have details like which class which line etc
'''
try:
    a+b
except Exception as e:
    #print(error_handling())
    logging.error(error_handling())
    #print(sys.exc_info()) # with this we get come info like type of exception and tracible object  # output looks like this :(<class 'NameError'>, NameError("name 'a' is not defined",), <traceback object at 0x0000020F3685D688>)
'''
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2].tb_lineno) # tb_lineno is traceback linenumber
    print('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                         sys.exc_info()[1],
                                         sys.exc_info()[2].tb_lineno))'''
    
                             
    
    
    