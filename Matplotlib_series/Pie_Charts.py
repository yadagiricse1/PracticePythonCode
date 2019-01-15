import matplotlib.pyplot as plt

slices=[2,5,7,9]
activities=['sleeping','eating','working','playing']
cols=['g','b','r','c']
#plt.pie(slices,labels=activities,colors=cols)

# if you compare above with below there are lot of parameters add which are not mandator and added based of the requirements
plt.pie(slices,
       labels=activities,
       colors=cols,
       startangle=90,
       shadow=True,
       explode=(0,0.1,0,0),
       autopct='%1.1f%%')
plt.title('Interesting graph \n Check it out')
#plt.legend()
plt.show()