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
    if (len(j)-1) < 1825:
        start = 0;
    else:
        start = end-1825;
    stock = [filename,j[end]['close']-j[start]['close']];
    stocks.append(stock)
    #print(j[len(j)-1]['close']-j[0]['close'])

print('done')

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = int(alist[first][1]);
   print(pivotvalue);
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and int(alist[leftmark][1]) <= pivotvalue:
          #print(leftmark);
          leftmark = leftmark + 1;

       while alist[rightmark][1] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp1 = alist[leftmark][1]
           alist[leftmark][1] = alist[rightmark][1]
           alist[rightmark][1] = temp1
           temp0 = alist[leftmark][0]
           alist[leftmark][0] = alist[rightmark][0]
           alist[rightmark][0] = temp0

   temp1 = alist[first][1]
   alist[first][1] = alist[rightmark][1]
   alist[rightmark][1] = temp1
   temp0 = alist[leftmark][0]
   alist[leftmark][0] = alist[rightmark][0]
   alist[rightmark][0] = temp0
   return rightmark


quickSort(stocks)

for stock in stocks:
    output = stock[0];
    output += " - ";
    output += str(stock[1]);
    print(output);
