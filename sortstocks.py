# Parameters to sort stocks by
days = 365*3; # Sort based on


from multiprocessing.dummy import Pool as ThreadPool
import _thread
import time
import json
import os

stocks = list()

for filename in os.listdir('data'):
    #print(filename)
    fn = 'data/';
    fn+=filename;
    f = open(fn,'r');
    j = json.loads(f.read())

    end = len(j)-1;
    if (len(j)-1) < days:
        start = 0;
    else:
        start = end-days;
    stock = [filename,((j[end]['close']-j[start]['close'])/j[start]['close'])];
    #if(int(j[end]['close']) < 100):
    stocks.append(stock);
    #print(j[len(j)-1]['close']-j[0]['close'])

print('done')


def insertionSort(alist):
   for index in range(1,len(alist)):

     currentticker = alist[index][0]
     currentvalue = alist[index][1]
     position = index

     while position>0 and alist[position-1][1]>currentvalue:
         alist[position][0]=alist[position-1][0]
         alist[position][1]=alist[position-1][1]
         position = position-1

     alist[position][0]=currentticker
     alist[position][1]=currentvalue

insertionSort(stocks);

for stock in stocks:
    output = stock[0];
    output += " - ";
    output += str(stock[1]);
    print(output);
