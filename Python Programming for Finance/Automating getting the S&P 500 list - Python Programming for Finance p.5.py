import bs4 as bs
import requests
import pickle


def save_sp500_tickers():
    resp=requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup=bs.BeautifulSoup(resp.text,'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers=[]
    for row in table.findAll('tr')[1:]:
        ticker=row.findAll('td')[0].text
        tickers.append(ticker)
    with open('C:/Users/yadag/Desktop/PythonProgrammingPractice/Python Programming for Finance/sp500tickers.pickle','wb') as f:
        pickle.dump(tickers,f)
    print(tickers)
    return tickers
    
     
    
save_sp500_tickers()
