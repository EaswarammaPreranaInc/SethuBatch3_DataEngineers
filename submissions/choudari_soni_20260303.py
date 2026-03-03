    # Write  a  program  to  search  for  'x'  in  fibonacci  series

    # 1) Let  input  be   10
    #     What  is  the  output ? --->	Not  found

    # 2) Let  input  be   21
    #     What  is  the  output ? --->  Found

    # 3) Do  not  generate  fibonacci  series'''
    # Write  a  program  to  search  for  'x'  in  fibonacci  series

    # 1) Let  input  be   10
    #     What  is  the  output ? --->	Not  found

    # 2) Let  input  be   21
    #     What  is  the  output ? --->  Found

    # 3) Do  not  generate  fibonacci  series



n=int(input('Enter any number :'))
a=0
b=1
c=a+b
for i in range(n+1):
    if(a==n):
        print('Found')
        break
    a=b
    b=c
    c=a+b   
else:
        print('Not found')


# ______________________________________
# Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number


from sys import argv
a=[]
for i in range(1,(len(argv)+1)):
    a.append=eval(a[i])
    if(i%2==0):
        print('Even number')
    else:
        print('odd number')

# ____________________________________________

# '''
# Modify  following   program  with  walrus  operator

# Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
# '''
try:
	sum =  ctr = 0
	while(x := eval(input('Enter input  (ctrl + z  to  stop):'))):
	
		sum += x
		ctr +=1
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string') 

# ______________________________________________________________

 
# Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

# 1) py  prog5.py  10   20    15.8   5   12.6
#     What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
#     What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
#     How  to  sort  list  'a' ?  ---> sorted(a)
#     How  to  sort  list  'a'  in  descending  order  ?  ---> sorted(a , reverse = True)

# 2) py  prog5.py   25   'Ten'
#     What  is  the  output ?  ---> Do  not  send  number  and  string  
	
# 3) py  prog5.py  
#     What  is  the  output ?  --->  Pls  send  inputs
	
# 3) py  prog5.py    'Hyd'  'Sec'  'Cyb'
#     What  are  the  outputs ?  --->   ['Cyb' , 'Hyd' , 'Sec']
# 													   ['Sec' , 'Hyd' , 'Cyb']

from sys import argv 
a=[]
for i in (argv[1:]):
    a.append(eval(i))
    print(sorted(a))
    print(sorted(a,reverse=True))


