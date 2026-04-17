#Topic - 1
'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''


"""
n = abs(int(input("Enter an integer : ")))
a, b, c = 0,1,False
while n>=a:
    if(a==n):
        c = True
    a , b = b , a+b
if c:
    print("Found")    
else:
    print("Not Found")    
"""

#Topic - 2
'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What  is  ctrl + z ?  --->  End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Raises  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  --->  ctrl + d
'''

"""
try:
    a = 0
    ctr = 0
    while True:
        b = eval(input("Enter values (ctrl + z  to  stop): "))
        a+=b
        ctr +=1
except EOFError:
    try:
        print(F"Avg: {a/ctr :.2f}")
    except ZeroDivisionError:
        print("Enter at least one value")
except:
    print("Enter Numbers only")
"""
     
#Topic - 3

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

"""
try:
	sum =  ctr = 0
	while  x := eval(input('Enter input  (ctrl + z  to  stop)  :  ')):
		sum += x
		ctr +=1
except  EOFError:
	try:
		print(F'Average :   {sum / ctr:.2f}')
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string')
"""

#Topic - 4
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

"""
from sys import argv
try:
    c= int(argv[1])
    if c%2==0:
        print("Even number")
    else:
        print("Odd number")
except:
   print("Pls  send  an  integer  input")
"""

#Topic - 5

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

"""
try:
    from sys import argv
    if (len(argv)==1):
        print("Pls  send  number  inputs")
    else:
        x = 0
        for y in argv[1:]:
            x += eval((y))
        print(F"sum : {x:.2f}")
        print("Length : ",len(argv)-1)

except:
    print("Pls  send  number  inputs")
"""

#Topic - 6

"""
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
"""

"""
from sys import argv
if (len(argv) == 1):
    print("Pls  send  inputs")
else:
    a, b, c = [], False, False

    try:
        for x in argv[1:]:
            a.append(float(x))
            b = True
    except:
        for x in argv[1:]:
            a.append(x)
            c = True    

    if(b == c):
        print("Do  not  send  number  and  string")
    elif(b == True):
        print(sorted(a))
        print(sorted(a, reverse=True))
    else:
        print(sorted(a))
        print(sorted(a, reverse=True))
"""