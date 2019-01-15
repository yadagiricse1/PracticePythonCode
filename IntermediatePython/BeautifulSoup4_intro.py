import bs4 as bs
import urllib.request

source=urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# the above code will give all the source code of HTML

soup=bs.BeautifulSoup(source,'lxml') # we can use any parser like HTML

#print(source) #this gives same content as print(soup) but little messy
#print(soup)
#print(soup.title.name) #print(soup.title.string)
#print(soup.title.text)
#print(soup.p) # to get first paragraph
#print(soup.find_all('p'))
'''
for paragraph in soup.find_all('p'):
    print(paragraph) 
    #print(paragraph.string) ##print(paragraph.text) .text is better than .string while printing content from paragraph .string wont work if the paragraph has child tags
    
'''
#print(soup.get_text())
# finding all the links 

for url in soup.find_all('a'):
    print(url.get('href'))  # url.text wont give the urls