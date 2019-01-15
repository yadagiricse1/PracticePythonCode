import csv
    
with open('C:/Users/yadag/Desktop/PythonProgrammingPractice/example.csv') as csvfile:
    readCSV= csv.reader(csvfile,delimiter=',')
    #print(readCSV) this will just give object
    dates=[]
    colors=[]
    for row in readCSV:
        color=row[3]
        date=row[0]
        dates.append(date)
        colors.append(color)
        
    print(dates)
    print(colors)
    try:
        whatColor=input('What color do you wish to know the date of? ')
        if whatColor in colors:
            coldexx=colors.index(whatColor.lower())
            theDate=dates[coldex]
            print('The day of ',whatColor,'is: ',theDate)
        else:
            print('color not found or is not a color')
    # The name error block will be executed if the defined word is not found ex. if coldex is missspelt and used in other place like coldexx        
    except NameError as e:
        print(e)         
    except Exception as e:
        print(e)
       
    print('continuing')
    
       
print(
'''
So it works like a multi-line
comment, but it will print out.

You can make kewl designs like this:

==============
|            |
|            |
|    BOX     |
|            |
|            |
==============
'''
    )