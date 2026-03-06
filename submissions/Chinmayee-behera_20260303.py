import sys

'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series'''
'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''
try:
    n=int(input("check number is present in fibonnaci series: "))
    a=0
    b=1
    c=0
    if(n==0 or n==1):
        print("Found")
        exit()
    while(c<=n):
        c=a+b
        if(c==n):
            print("Found")
            break
        a,b=b,c
    else:
        print("Not Found")
except:
    print("exited from function")


        


'''
Modify  following   program  with  walrus  operator

Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
'''
try:
	sum =  ctr = 0
	while  x := eval(input('Enter input  (ctrl + z  to  stop)  :  ')):
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
    a=eval(sys.argv[1])
    ans='even' if a%2==0 else "odd"
    print(f'{ans} number')
except:
    print("please send an integer")

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
try:
    a=sys.argv[1:]
    s=0
    c=0
    for i in a:
        s+=eval(i)
        c+=1
    print(f'average of array is {(s/c):.2f}')
except:
    print("please enter integer only ")

    


try:
    a=sys.argv[1:]
    arr=[]
    for i in a:
        arr.append(eval(i))
    arr=sorted(arr)
    print(f'sorted array is : {arr}')
    arr=sorted(arr,reverse=True)
    print(f'reversed sorted array is :{arr}')
except:
    print('please enter integer or string only not both')