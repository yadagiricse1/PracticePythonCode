import quandl
import pandas as pd
import pickle
api_key=open('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/quandlapikey.txt','r').read() 
# the above key we can get it from quandl website .after login click account settings and click API KEY
#print(api_key)

def states_list():
    fiddy_stats=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_stats[0][0][1:]


main_df=pd.DataFrame()

def grab_initial_state_data():
    main_df=pd.DataFrame()
    states=states_list()
    for abbv in states:
        query="FMAC/HPI_"+str(abbv)
        df=quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value':str(abbv)},inplace=True)
        if main_df.empty:
            main_df=df
        else:
            main_df=main_df.join(df)
    print(main_df.head())
    
    pickle_out=open('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/fiddy_states.pickle','wb') # wb stands for write bites
    pickle.dump(main_df,pickle_out)
    pickle_out.close()
#grab_initial_state_data()   # this method call will piclke data in the above location. We no need to call again to get data. Just use that pickle and get data
pickle_in=open('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/fiddy_states.pickle','rb') # rb stands for read bites
HPI_data=pickle.load(pickle_in)
#print(HPI_data)

''' There are 2 ways of pickling  1) open the file and pickle out and close. if we want that file. we have to open file and load the file.
the other method with pandas we can pickkle in/out with single line of code respectively'''
HPI_data.to_pickle('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/pickle.pickle')
HPI_data2=pd.read_pickle('C:/Users/yadag/Desktop/PythonProgrammingPractice/DataAnalysis_with_Python/pickle.pickle')
print(HPI_data2)
print('HPI_data')

     