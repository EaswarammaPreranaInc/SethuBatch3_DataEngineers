#Modify Homework #1
'''
Modify  following   program  with  walrus  operator

Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
'''
'''
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
	sum =  ctr = 0
	while (x := eval(input('Enter input  (ctrl + z  to  stop)  :  '))):
		sum += x
		ctr +=1
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string')




#Programming Homework #1
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
	a = []

	for  i  in  argv[1:]:
		a.append(eval(a[i]))
		if a[i] % 2 == 0:
			print(f'{a} is an Even Number')
		else:
			print(f'{a} is an Odd Number')

except ValueError:
	print('Please send one input.')
except TypeError:
	print('Please enter either an integer or float number.')



#Programming Homework #2
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
try:
	a = []

	for  x  in  argv[1:]:
		a.append(eval(x))
		
	for i in range(len(a)):
		sum += a[i]
		ctr +=1
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input cannot be a string.')



#Programming Homework #3
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
	a = []

	for  x  in  argv[1:]:
		a.append(eval(x))
		
	print('Ascending Order:' , sorted(a))
	print('Descending Order:' , sorted(a, reverse = True))
	
except ValueError:
	print('Please send one input.')
except:
	print('Do not send integer and a string.')
