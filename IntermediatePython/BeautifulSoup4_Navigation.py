import bs4 as bs
import urllib.request

source=urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# the above code will give all the source code of HTML

soup=bs.BeautifulSoup(source,'lxml') # we can use any parser like HTML

nav=soup.nav

#print(nav)
'''
for url in nav.find_all('a'):
    print(url.get('href'))  # url.text wont give the urls
'''   
body=soup.body
'''
for paragraph in body.find_all('p'):
    print(paragraph.text)  
'''   
for div in body.find_all('div',class_='body'):  #for div in body.find_all('div'):
    print(div.text)  