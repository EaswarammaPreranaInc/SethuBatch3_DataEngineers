'''
Modify  following   program  with  walrus  operator
Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
'''
import sys
try:
    sum =  ctr = 0
    while  True:
        sum += (x := eval(input('Enter input: ')))
        ctr +=1
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
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
if len(argv) != 2:
    raise ValueError
    num = int(argv[1])
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


'''
Write  a  program  to  determine  average  of  command  line  inputs

1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
    What  is  argv ?  --->  ['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
    What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
	How  to  determine  sum  of  list  elements ?  ---> sum(a)
    How  to  determine  number  of  list  elements ?  ---> len(a)
2) py   prog4.py
    What  is  the  output ?  --->  Pls  send  number  inputs
3) py   prog4.py  25   'Ten'
    What  is  the  output  ?  --->  Pls  send  number  inputs
'''
    from sys import argv
    if len(argv) == 1:
        raise ValueError
    a = []
    for x in argv[1:]:
        a.append(eval(x))
    print("Average :", sum(a) / len(a))

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
4) py  prog5.py    'Hyd'  'Sec'  'Cyb'
    What  are  the  outputs ?  --->   ['Cyb' , 'Hyd' , 'Sec']
				  ['Sec' , 'Hyd' , 'Cyb']
'''
from sys import argv
    if len(argv) == 1:
        raise ValueError
    a = []
    for x in argv[1:]:
        a.append(eval(x))
    print(sorted(a))
    print(sorted(a, reverse=True))