'''
1) import  os
list = ['a' , 'b']
print(list)
for   x  in  list:  #   'x'  is  
	list . append(x)  #   ['a' , 'b', 'a' , 'b' , 'a' , 'b' , 'a' , 'b'........................]
	print(list)	
	os . system('pause')
'''

'''
2) # Write  a  program  to  print  csv  file
import  csv
def  disp(f):
	How  to  itertae  thru  csv  file  using  reader  object
# End  of  function
try:
	How  to  read  the  filename
	How  to  open  the  file
	How  to  print  the  file
	How  to  close  the  file	
except  FileNotFoundError:
	print(F'File  {fname}  does  not  exist')
'''
import csv
def disp(f):
    r = csv.reader(f)
    for row in r:
        for col in row:
            print(col, end='\t\t')
        print()
try:
    fname = input('Enter file name : ')
    f = open(fname, 'r')
    disp(f)
    f.close()
except FileNotFoundError:
    print(f'File {fname} does not exist')