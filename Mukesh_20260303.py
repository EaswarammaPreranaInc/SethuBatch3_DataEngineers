# '''
# Write  a  program  to  search  for  'x'  in  fibonacci  series

# 1) Let  input  be   10
#     What  is  the  output ? --->	Not  found

# 2) Let  input  be   21
#     What  is  the  output ? --->  Found

# 3) Do  not  generate  fibonacci  series'''
# Write  a  program  to  search  for  'x'  in  fibonacci  series

# n=int(input("ENter the number : "))
# a=0
# b=1
# x=[0,1]
# while(a<=n):
#     x.append(a)
#     c=a+b
#     a=b
#     b=c
# print(f"found : {n}")if n in x else print(F" Not Found  :{n}")


# 1) Let  input  be   10
#     What  is  the  output ? --->	Not  found

# 2) Let  input  be   21
#     What  is  the  output ? --->  Found

# 3) Do  not  generate  fibonacci  series
# '''
#  '''
# Modify  following   program  with  walrus  operator

# Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
# '''
# try:
# 	sum =  ctr = 0
# 	while  True:
# 	 sum +=( x:= eval(input('Enter input  (ctrl + z  to  stop)  :  ')));ctr +=1
# except  EOFError:
# 	try:
# 		print(F'Average :   {sum / ctr}')
# 	except  ZeroDivisionError:
# 		print('Enter  at  least  one  input')
# except  (NameError , TypeError):
# 	print('Input  can  not  be  string')
# '''
# Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

# 1) py  prog3.py  26
#     What  is  the  output ?  ---> Even  number

# 2) py  prog3.py  45
#     What  is  the  output ?  ---> Odd  number

# 3) py  prog3.py
#     What  is  the  output  ?  --->  Pls  send  an  integer  input

# 4) py  prog3.py  10.8
#     What  is  the  output ?  ---> Pls  send   an  integer  input

# 5) py  prog3.py  Ten
#     What  is  the  output  ?  ---> Pls  send   an  integer  input

# import sys

# num=int(sys.argv[1])
# if num%2==0:
#     print("even number")
# else :
#     print("odd number")    



# '''
#  '''
# Write  a  program  to  determine  average  of  command  line  inputs

# 1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
#     What  is  argv ?  --->  ['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
#     What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
# 	How  to  determine  sum  of  list  elements ?  ---> sum(a)
#     How  to  determine  number  of  list  elements ?  ---> len(a)

# import sys

# num=[eval(i) for i in sys.argv[1:]]
# avg=sum(num)/len(num)
# print("average number :",avg)



# 2) py   prog4.py
#     What  is  the  output ?  --->  Pls  send  number  inputs

# 3) py   prog4.py  25   'Ten'
#     What  is  the  output  ?  --->  Pls  send  number  inputs
# '''
# '''
# Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

# 1) py  prog5.py  10   20    15.8   5   12.6
#     What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
#     What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
#     How  to  sort  list  'a' ?  ---> sorted(a)
#     How  to  sort  list  'a'  in  descending  order  ?  ---> sorted(a , reverse = True)
import sys
num=[eval(i) for i in sys.argv[1:]]
print("ascending order",sorted(num))
print("descending order,",sorted(num,reverse=True))

# 2) py  prog5.py   25   'Ten'
#     What  is  the  output ?  ---> Do  not  send  number  and  string  
	
# 3) py  prog5.py  
#     What  is  the  output ?  --->  Pls  send  inputs
	
# 3) py  prog5.py    'Hyd'  'Sec'  'Cyb'
#     What  are  the  outputs ?  --->   ['Cyb' , 'Hyd' , 'Sec']
# 													   ['Sec' , 'Hyd' , 'Cyb']