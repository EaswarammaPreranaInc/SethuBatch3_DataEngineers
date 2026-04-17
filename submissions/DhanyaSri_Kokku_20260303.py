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
# Code :
try:
    n = int(input("Enter the value to be searched : "))
    if n < 0:
        print("Enter the integer input")
    elif n==0 or n==1:
        print("Found")
    else:
        a = 0
        b = 1
        c = a+b
        while c <= n:
            if c==n:
                print("Found")
                break
            c = a+b
            a = b
            b = c
        else:
            print("Not Found")
except:
    print("Enter the integer input")

''' Output:
Enter the value to be searched : 21
Found

Enter the value to be searched : 10
Not Found
'''
'''
Modify  following   program  with  walrus  operator

Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
'''
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

''' Output:
Enter input (ctrl + z to stop): 25
Enter input (ctrl + z to stop): 10.8
Enter input (ctrl + z to stop): ^Z
Average : 17.9

Enter input (ctrl + z to stop): ^Z
Enter at least one input
'''

''
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
# Code :
from sys import argv
try:
    n = int(argv[1])
    if n % 2==0:
        print("Even number")
    else:
        print("Odd number")
except:
    print("Pls  send  an  integer  input")

''' Output:
Program_2.py 26
Even number
Program_2.py 41
Odd number
Program_2.py 10.8
Pls  send  an  integer  input
'''
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
# Code :
from sys import argv
try:
    a = []
    for x in argv[1:]:
        a.append(eval(x))
    sum = sum(a)
    len = len(a)
    print(F"Average : {sum/len:.2f}")
    
except:
    print("Pls  send  an  number  input")

''' Output:
Program_2.py 10.8   25   True   14.6   19   False   7.4
Average : 11.11
Program_2.py                                           
Pls  send  an  number  input
Program_2.py 25 'Ten'
Pls  send  an  number  input
'''
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
# Code:

from sys import argv
a = []
if len(argv)==1:
    print("Pls  send  inputs")
else:
    try:
        for x in argv[1:]:
            a.append(eval(x))
        sort = sorted(a)
        sort_desc = sorted(a,reverse=True)
        print("Asending order : ",sort)
        print("Desending order : ",sort_desc)
    except:
        print("Do  not  send  number  and  string")

''' Output:
py Program_2.py 10   20    15.8   5   12.6
Asending order :  [5, 10, 12.6, 15.8, 20]
Desending order :  [20, 15.8, 12.6, 10, 5]

py Program_2.py      
Pls  send  inputs

py Program_2.py 25 'Ten'
Do  not  send  number  and  string

py Program_2.py 'Hyd'  'Sec'  'Cyb'
Asending order :  ['Cyb', 'Hyd', 'Sec']
Desending order :  ['Sec', 'Hyd', 'Cyb']
'''

