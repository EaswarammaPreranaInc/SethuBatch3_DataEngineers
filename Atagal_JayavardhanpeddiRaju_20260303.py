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

x = int(input("Enter a number: "))

a = 0
b = 1

for i in range(x-1):
    if a == x:
        print("Found")
        break
    a = b
    b = a + b
else:
    print("Not Found")


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
[1:14 pm, 03/03/2026] +91 99482 50500: '''
Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

1) py  prog3.py  26
    What  is  the  output ?  ---> Even  number

2) py  prog3.py  45

import sys

try:
    num = int(sys.argv[1])  

    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

except :
    print("should be an integer")


Write  a  program  to  determine  average  of  command  line  inputs

1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
    What  is  argv ?  --->  ['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
    What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
	How  to  determine  sum  of  list  elements ?  ---> sum(a)
    How  to  determine  number  of  list  elements ?  ---> len(a)

2) py   prog4.py
    What  is  the  output ?  --->  Pls  send  number  inputs

3) py   prog4.py  25   'Ten'

argv: ['prog4.py', '10.8', '25', 'True', '14.6', '19', 'False', '7.4']
List a: [10.8, 25.0, True, 14.6, 19.0, False, 7.4]
Sum: 76.8
Number of elements: 7

Ascending order: [7.4, 10.8, 14.6, 19.0, 25.0]
Descending order: [25.0, 19.0, 14.6, 10.8, 7.4]