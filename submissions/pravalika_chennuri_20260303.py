'''
Modify  following   program  with  walrus  operator

Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
'''

try:
	sum =  ctr = 0
	while  True:
		x = eval(input('Enter input  (ctrl + z  to  stop)  :  '))
		sum+=x
		ctr +=1
except  EOFError:
	try:
		print(Average := sum / ctr)
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string')

'''
Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

1) py  prog3.py  26
    What  is  the  output ?  ---> Even  number

2) py  prog3.py  45
    What  is  the  output ?  ---> Odd  number

3) py  prog3.py
    What  is  the  output  ?  --->  Pls  send  an  integer  input

4) py  prog3.py  10.8
    What  is  the  output ?  ---> Pls  send   an  integer  input

5) py  prog3.py  Ten
    What  is  the  output  ?  ---> Pls  send   an  integer  input
'''

from sys import argv
try:
    a = int(argv[1:])
    if a%2==0:
        print("Even number")
    else:
        print("Odd number")
except(NameError,TypeError):
    print("please send an integer input")

'''
Write  a  program  to  determine  average  of  command  line  inputs

1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
    What  is  argv ?  --->  ['prog4.py' , 25' , ''10.8' , 'True' , '14.6' , '19' , 'False' , '7.4']
    What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
	How  to  determine  sum  of  list  elements ?  ---> sum(a)
    How  to  determine  number  of  list  elements ?  ---> len(a)

2) py   prog4.py
    What  is  the  output ?  --->  Pls  send  number  inputs

3) py   prog4.py  25   'Ten'
    What  is  the  output  ?  --->  Pls  send  number  inputs
'''
from sys import argv
try :
    a = argv[1:]
    sum=0
    for i in a:
        sum += float(i)
    avg = sum/len(a)
    print(avg)
except(NameError,ZeroDivisionError,ValueError):
    print("please send number inputs")

'''
Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  ---> sorted(a)
    How  to  sort  list  'a'  in  descending  order  ?  ---> sorted(a , reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  ---> Do  not  send  number  and  string  
	
3) py  prog5.py  
    What  is  the  output ?  --->  Pls  send  inputs
	
3) py  prog5.py    'Hyd'  'Sec'  'Cyb'
    What  are  the  outputs ?  --->   ['Cyb' , 'Hyd' , 'Sec']
													   ['Sec' , 'Hyd' , 'Cyb']
'''
from sys import argv
try:
    a = argv[1:]
    b = sorted(a)
    print(b)
except(TypeError,ValueError,NameError):
    print("Do  not  send  number  and  string")