from multiprocessing.dummy import Pool as ThreadPool
import time
import json
import os
try: #python3
    from urllib.request import urlopen
except: #python2
    from urllib2 import urlopen

alpha = ['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def fetchdata(ticker):
    #print('Fetching data')
    filename = 'data/';
    filename+=ticker;
    #print(filename);
    if not os.path.exists(filename):
        url = 'https://api.iextrading.com/1.0/stock/';#/stock/aapl/news
        url+=ticker;
        url+='/chart/5y';
        try:
            info = urlopen(url).read();
            j = json.loads(info)
            if j[len(j)-1]['close']:
                #print(j[len(j)-1]['close'])
                filename = 'data/';
                filename+=ticker;
                f = open(filename,'w');
                f.write(info.decode())
                print(ticker);
        except:
            info = '';
            #print("DNE, skipping")


tickers = list();
for l in alpha:
    for m in alpha:
        for n in alpha:
            for o in alpha:
                t = l;
                t += m;
                t += n;
                t += o;
                tickers.append(t);

pool = ThreadPool(10);
pool.map(fetchdata,tickers)

#_thread.start_new_thread(fetchdata, ('meme','a',));
#for l in alpha:
    #fetchdata(l);
    #_thread.start_new_thread(fetchdata, (l,));
