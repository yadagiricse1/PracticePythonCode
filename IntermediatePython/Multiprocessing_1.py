import multiprocessing
 # not executing
 
 #https://pythonprogramming.net/multiprocessing-python-intermediate-python-tutorial/
def spawn(num, num2):
    print('Spawn # {} {}'.format(num, num2))

if __name__=='__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn, args=(i, i+1))
        p.start()
        #p.join() if we use join if there are multiple processes running they will try to complete in one after the other in minimal threads else there will be many threads
        