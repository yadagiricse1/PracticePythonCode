import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from  matplotlib import style
style.use('fivethirtyeight')

conn=sqlite3.connect('C:/Users/yadag/Desktop/PythonProgrammingPractice/tutorial_sqlite.db')

c=conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,keyword TEXT,value REAL)')


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1234333,'2017-12-12','Python',5)")
    conn.commit()
    c.close()
    conn.close()
    
    
    
    
def dynamic_data_entry():
    unix=time.time()
    date=str(datetime.datetime.fromtimestamp(unix).strftime('%y-%m-%d %H:%M:%S'))
    keyword='Python'
    value=random.randrange(0,10)
    c.execute("INSERT INTO  stuffToPlot(unix,datestamp,keyword,value) VALUES(?,?,?,?)",
    (unix,date,keyword,value))
    conn.commit()
    
def read_from_db():
    c.execute("SELECT * FROM stuffToPlot")   
    #c.execute("SELECT * FROM stuffToPlot WHERE value=3")
    # c.execute('SELECT * FROM stuffToPlot WHERE unix > 1452554972')
    #c.execute('SELECT value, datestamp,unix,keyword FROM stuffToPlot')
    #data=c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)
        #print(row[0]) # retrive firstcolumn unix stamp



def graph_data():
    c.execute('SELECT  unix,value FROM stuffToPlot')
    dates=[]
    values=[]
    for row in c.fetchall():
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    plt.plot_date(dates,values ,'-')
    plt.show()
    


def update():
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]
    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 3')
    conn.commit()
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]
def delete():
    c.execute('SELECT * FROM stuffToPlot ')
    data = c.fetchall()
    c.execute('SELECT * FROM stuffToPlot ')
    print(len(c.fetchall())) # check how many rows retrived
    [print(row) for row in data]
    c.execute('DELETE FROM stuffToPlot WHERE value = 99')
    conn.commit()
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]



#update()
delete()

#graph_data()
#read_from_db() 
#create_table()
#data_entry()
#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)
   
c.close()
conn.close()

    


    
    