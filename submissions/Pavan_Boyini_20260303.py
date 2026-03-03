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
 '''

output:
n = int(input("Enter any number: "))
a = 0
b = 1
i = 0
while i < n:
    if b == n:
        print("found")
        break
    a, b = b, a+b
    i+=1
else:
    print("Not found")


Modify  following   program  with  walrus  operator

Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
'''
try:
	sum =  ctr = 0
	while  True:
		x = eval(input('Enter input  (ctrl + z  to  stop)  :  '))
		sum += (x:=eval(input('Enter input  (ctrl + z  to  stop)  :  '))  # here walrus operator used to combine lines

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

output:

import sys

if len(sys.argv) != 2:
    print("Pls send an integer input")

else:
    x = sys.argv[1]

    if x.isdigit():   # Only checks positive integers
        n = int(x)

        if n % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    else:
        print("Pls send an integer input")



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

output:

import sys

# Check if user gave inputs
if len(sys.argv) == 1:
    print("Pls send number inputs")

else:
    a = []

    # Convert string inputs into numbers
    for x in sys.argv[1:]:
        if x.replace('.', '', 1).isdigit():
            a.append(float(x))
        elif x == "True":
            a.append(True)
        elif x == "False":
            a.append(False)
        else:
            print("Pls send number inputs")
            break
    else:
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
	
3) py  prog5.py    'Hyd'  'Sec'  'Cyb'
    What  are  the  outputs ?  --->   ['Cyb' , 'Hyd' , 'Sec']


output:
from sys import argv
try:
	a = []  #   Empty  list
	for  x  in  argv[1:]:  #   'x'  is  each   command  line  input  of   argv  list
		a . append(eval(x))
                print(sorted(a))
                print(sorted(a, reverse = True))

<========or =======>

from sys import argv

if len(argv) == 1:
    print("Pls send inputs")

else:
    a = [eval(x) for x in argv[1:]]

    if all(isinstance(i, (int, float)) for i in a):
        print(sorted(a))
        print(sorted(a, reverse=True))

    elif all(isinstance(i, str) for i in a):
        print(sorted(a))

    else:
        print("Do not send number and string")

													   ['Sec' , 'Hyd' , 'Cyb']