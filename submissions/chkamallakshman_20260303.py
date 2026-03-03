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
x=int(input("Enter a Input value:")
a=0
b=1
while (b<x):
  a,b=b,a+b
if (b==x):
  print("Found")
else:
  print("Not Found")
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
def oddOrEven():
    try:
        n=eval(sys.argv[1])
        if(n%2==0):
            print(f'{n} it is an even Number')
        else:
            print(f'{n} it is an Odd number')
    except:
        print("enter integer number")
#oddOrEven()

def sorting():
    try:
        l=[]
        if len(sys.argv)==1:
            print("pls enter the values")
        else:
             for i in sys.argv[1:]:
                  l.append(eval(i))
             l.sort()
             print(l)
             l.sort(reverse=True)
             print(l)
    except:
        print("enter valid inputs")
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
def average():
    try:
        l=[]
        if len(sys.argv)==1:
            print("pls give inputs")
        else:
             for i in sys.argv[1:]:
                  if(type(n:=eval(i)) in(int,float,bool)):
                       l.append(n)
                  else:
                       print("give integer number")
             print(sum(l))
    except:
        print("enter integer values only")


