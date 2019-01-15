import matplotlib.pyplot as plt

def graph_operation(x,y):
    print('function that graphs {} and {}'.format(str(x),str(y)))
    plt.plot(x,y)
    plt.show()

x1=[1,2,3]
y1=[2,3,6]
#graph_operation(x1,y1)
# we can also call like below
graph_me=[x1,y1]
print('be care full while passing argument we need to keep *-----------')
graph_operation(*graph_me)


