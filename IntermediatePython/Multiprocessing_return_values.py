from multiprocessing import Pool

def job(num):
    return num*2


if __name__ == '__main__':
    
    p=Pool(processes=20)
    data=p.map(job,range(20)) # data=p.map(job,[1,2,3,4]),data=p.map(job,[4])  even we can keep generator
    data2=p.map(job,[1,2,3,4]) 
    p.close()
    print(data)
    print(data2)