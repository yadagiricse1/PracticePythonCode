import bs4 as bs
import urllib.request
import pandas as pd
'''
source=urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# the above code will give all the source code of HTML

soup=bs.BeautifulSoup(source,'lxml') # we can use any parser like HTML

#table=soup.table  # both lines will give same output table=soup.find('table')

table=soup.find('table')

table_rows=table.find_all('tr')

for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text for i in td]
    print(row)
    
'''


''''
dfs=pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0) # header =0 makes first row as header

for df in dfs:
    print(df) # we can convert this to list if we want df.values.list
    
'''

source=urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
# the above code will give all the source code of HTML

soup=bs.BeautifulSoup(source,'xml') # we can use any parser like HTML

#print(soup)

for url in soup.find_all('loc'):
    print(url.text)





