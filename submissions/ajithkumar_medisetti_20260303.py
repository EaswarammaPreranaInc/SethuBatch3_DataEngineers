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
x = int(input("Enter number: "))

a = 0
b = 1
found = False

while a <= x:
    if a == x:
        found = True
        break
    c = a + b
    a = b
    b = c

if found:
    print("Found")
else:
    print("Not Found")
#Output:
Enter number: 10
Not Found
Enter number: 21
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
'''
#Program:

try:
    sum = ctr = 0
    while True:
        sum += (x := eval(input('Enter input (ctrl + z to stop): ')))
        ctr += 1

except EOFError:
    try:
        print(f'Average : {sum / ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')

except (NameError, TypeError):
    print('Input can not be string')

Output:

Enter input : 10
Enter input : 20
Enter input : 30
Ctrl+Z
Average : 20.0

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

Program:

import sys
if len(sys.argv) != 2:
    print("Pls send an integer input")
else:
    try:
        n = int(sys.argv[1])

        if n % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

    except ValueError:
        print("Pls send an integer input")
#Output:

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

Program:

import sys

if len(sys.argv) == 1:
    print("Pls send number inputs")
else:
    try:
        a = [eval(x) for x in sys.argv[1:]]

        for i in a:
            if not isinstance(i, (int, float, bool)):
                raise ValueError

        avg = sum(a) / len(a)
        print("Average :", avg)

    except:
        print("Pls send number inputs")
#Output:
Case:1
py prog4.py 10.8 25 True 14.6 19 False 7.4
['prog4.py','10.8','25','True','14.6','19','False','7.4']
[10.8, 25, True, 14.6, 19, False, 7.4]
Average : 11.4

Case:2
py prog4.py
Pls send number inputs

Case:3
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

#program:

import sys

if len(sys.argv) == 1:
    print("Pls send inputs")

else:
    try:
        a = [eval(x) for x in sys.argv[1:]]

        num_flag = any(isinstance(i, (int, float, bool)) for i in a)
        str_flag = any(isinstance(i, str) for i in a)

        if num_flag and str_flag:
            print("Do not send number and string")
        else:
            print(sorted(a))                     # ascending
            print(sorted(a, reverse=True))      # descending

    except:
        print("Pls send inputs")

#Output:

#py prog5.py 10 20 15.8 5 12.6

#argv   ['prog5.py','10','20','15.8','5','12.6']

#list a   [10, 20, 15.8, 5, 12.6]

#Final Output
[5, 10, 12.6, 15.8, 20]
[20, 15.8, 12.6, 10, 5]