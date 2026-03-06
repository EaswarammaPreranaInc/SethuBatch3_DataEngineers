'''

Modify  following   program  with  walrus  operator

Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator

try:
	sum =  ctr = 0
	while  True:
		x = eval(input('Enter input  (ctrl + z  to  stop)  :  '))
		sum += x
		ctr +=1
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string')

'''

try:
	sum = ctr = 0
	while  True:
		sum += (x := eval(input('Enter input  (ctrl + z  to  stop)  :  ')))
		ctr += 1
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}') # Average :   15.0  (example)
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string')

# ---------------------------------------------------------------------------

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

import sys

try:
	if len(sys.argv) != 2:
		raise ValueError
	
	n = int(sys.argv[1])
	
	if n % 2 == 0:
		print('Even  number') # Even  number  (if 26)
	else:
		print('Odd  number') # Odd  number  (if 45)

except:
	print('Pls  send  an  integer  input') # For  no input / float / string

# ---------------------------------------------------------------------------

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

import sys

try:
	if len(sys.argv) == 1:
		raise ValueError
	
	a = [eval(x) for x in sys.argv[1:]]
	
	print('Average  :  ', sum(a) / len(a)) # Average  :   12.828571428571429  (example)

except:
	print('Pls  send  number  inputs')

# ---------------------------------------------------------------------------

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

import sys

try:
	if len(sys.argv) == 1:
		raise ValueError
	
	a = [eval(x) for x in sys.argv[1:]]
	
	print(sorted(a)) # [5, 10, 12.6, 15.8, 20]
	print(sorted(a , reverse = True)) # [20, 15.8, 12.6, 10, 5]

except:
	if len(sys.argv) == 1:
		print('Pls  send  inputs')
	else:
		print('Do  not  send  number  and  string')
