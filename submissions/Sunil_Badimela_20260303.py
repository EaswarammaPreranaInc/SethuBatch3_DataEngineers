'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''

x = int(input("Enter number to search: "))

a = 0
b = 1

while a <= x:
    if a == x:
        print("Found")
        break
    a, b = b, a + b
else:
    print("Not Found")

output
10
Not Found
21
Found



'''
Modify  following   program  with  walrus  operator

Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
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


try:
    sum = ctr = 0
    while True:
        sum += (x := eval(input('Enter input (ctrl + z to stop) : ')))
        ctr += 1

except EOFError:
    try:
        print(f'Average : {sum / ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')

except (NameError, TypeError):
    print('Input can not be string')



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
        raise IndexError

    num = int(sys.argv[1])

    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

except (IndexError, ValueError):
    print("Pls send an integer input")


output
py prog3.py 26
Even number
py prog3.py 45
Odd number
py prog3.py
Pls send an integer input
py prog3.py 10.8
Pls send an integer input
py prog3.py Ten
Pls send an integer input



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
        raise IndexError

        a = [eval(i) for i in sys.argv[1:]]

        for value in a:
        if not isinstance(value, (int, float, bool)):
            raise TypeError

    print("Average :", sum(a) / len(a))

except (IndexError, TypeError, NameError):
    print("Pls send number inputs")


output
['prog4.py', '10.8', '25', 'True', '14.6', '19', 'False', '7.4']
10.8 + 25 + 1 + 14.6 + 19 + 0 + 7.4 = 77.8
Average : 11.114285714285714

py prog4.py
Pls send number inputs

py prog4.py 25 'Ten'
Pls send number inputs






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
        raise IndexError

    
    a = [eval(i) for i in sys.argv[1:]]

    
    if any(isinstance(i, str) for i in a) and any(isinstance(i, (int, float, bool)) for i in a):
        raise TypeError

    print(sorted(a))
    print(sorted(a, reverse=True))

except IndexError:
    print("Pls send inputs")

except (NameError, TypeError):
    print("Do not send number and string")


output
['prog5.py', '10', '20', '15.8', '5', '12.6']

[5, 10, 12.6, 15.8, 20]
[20, 15.8, 12.6, 10, 5]


py prog5.py 25 'Ten'
Do not send number and string


