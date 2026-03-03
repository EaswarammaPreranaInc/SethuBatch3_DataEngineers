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


# output : try:
	sum =  ctr = 0
	while  True:
		sum += (x := eval(input('Enter input  (ctrl + z  to  stop)  :  ')))
		ctr +=1
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string')


# 2 . Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

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


# output : import sys

try:
    # Check if argument is given
    if len(sys.argv) != 2:
        raise IndexError

    n = int(sys.argv[1])

    if n % 2 == 0:
        print("Even  number")
    else:
        print("Odd  number")

except (IndexError, ValueError):
    print("Pls  send  an  integer  input")


# 3 . Write  a  program  to  determine  average  of  command  line  inputs

1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
    What  is  argv ?  --->  ['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
    What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
	How  to  determine  sum  of  list  elements ?  ---> sum(a)
    How  to  determine  number  of  list  elements ?  ---> len(a)

2) py   prog4.py
    What  is  the  output ?  --->  Pls  send  number  inputs

3) py   prog4.py  25   'Ten'
    What  is  the  output  ?  --->  Pls  send  number  inputs


# output : import sys

try:
    if len(sys.argv) == 1:
        raise IndexError

    total = 0
    count = 0

    for i in sys.argv[1:]:
        n = eval(i)
        total += n
        count += 1

    print("Average :", total / count)

except:
    print("Pls  send  number  inputs")


# 4 . Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

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


# output : import sys

try:
    if len(sys.argv) == 1:
        print("Pls  send  inputs")
    else:
        a = []

        for i in sys.argv[1:]:
            a.append(eval(i))

        print(sorted(a))
        print(sorted(a, reverse=True))

except:
    print("Do  not  send  number  and  string")

# 5 . Write  a  program  to  search  for  'x'  in  fibonacci  series

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


# output : import math

x = int(input("Enter a number : "))

a = 5*x*x + 4
b = 5*x*x - 4

r1 = int(math.sqrt(a))
r2 = int(math.sqrt(b))

if r1*r1 == a or r2*r2 == b:
    print("Found")
else:
    print("Not found")