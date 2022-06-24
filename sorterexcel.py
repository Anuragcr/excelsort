# sort an excel file and save it to another file


from pandas import Series,DataFrame
import pandas as pd
import openpyxl
pd.set_option('display.max_columns',None)

#source info
file = input('Enter location/name of file')
sheet=input('Enter sheet name you wish to sort')
file2=pd.read_excel(file,sheet,index_col=0,na_values=['NA'])

#Sort Info
sorter=[]
style=[]
sortq=int(input('please enter number of cols to sort:'))
for x in range(sortq):
     sorter.append(input(('Name of columns you wish to sort by' )))
     style.append(input(('Type True for Ascending, False for Descending sort ' )))
sort1=file2.sort(sorter,ascending=(style))


#destination info
dest=input('enter detination and filename to store as')
sort1.to_excel(dest,sheet_nmae='Sheet1')
