from functools import wraps



def add_wrapping_with_style(style):
    def add_wrapping(item):
        @wraps(item)
        def wrapped_item():
            return 'a {} wrapped up box of {}'.format(style,str(item()))
        return wrapped_item
    return add_wrapping
    
@add_wrapping_with_style('horribly')  
@add_wrapping_with_style('beautifully')
def new_gpu():
    return 'a new Tesla P100 GPU'
    
print(new_gpu())
print(new_gpu.__name__)


'''
# multiple wrapping
def add_wrapping(item):
    @wraps(item)
    def wrapped_item():
        return 'a wrapped up box of {}'.format(str(item()))
    return wrapped_item
@add_wrapping    
@add_wrapping
def new_gpu():
    return 'a new Tesla P100 GPU'
    
print(new_gpu())
print(new_gpu.__name__) # if we use the wrapper it generally gives the output as wrapped_item if there is no wrapper it will give o/p as new_gpu
# if i want my method name even if a wrapper is added  import functools as wraps and add a line of code in your wrapper @wrap(item)

'''


'''
def add_wrapping(item):
    def wrapped_item():
        return 'a wrapped up box of {}'.format(str(item()))
    return wrapped_item
 
@add_wrapping # try with single wrapper and double wrappers       
@add_wrapping # if we writhe @add_wrapping 2 times we are wripping it 2 times with same wrapper
def new_gpu():
    return 'a new Tesla P100 GPU'
 

@add_wrapping
def new_bicycle():
    return 'a new bicycle'    
    
print(new_gpu())
print(new_bicycle())
'''