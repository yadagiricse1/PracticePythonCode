import sqlite3

conn=sqlite3.connect('C:/Users/yadag/Desktop/PythonProgrammingPractice/tutorial_sqlite.db')

c=conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,keyword TEXT,value REAL)')


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1234333,'2017-12-12','Python',5)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()


    
    