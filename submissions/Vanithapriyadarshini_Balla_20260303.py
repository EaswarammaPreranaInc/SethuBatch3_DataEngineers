# Write  a  program  to  search  for  'x'  in  fibonacci  series

x=int(input("Search element : "))
f1=0
f2=1
f3=f1+f2
if x==0:
    print("Found")
elif x==1:
    print("Found")
else:
    while f3<x:
        f3=f1+f2
        f1=f2
        f2=f3
    if f3==x:
        print("Found")
    else:
        print("Not found")
print()

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

# Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

try:
    while True:
        x=int(input("Enter integer input : "))
        break;
    if x%2==0:
        print("Even number")
    else:
        print("Odd Number")
except:
    print("Please send an integer input")

# Write  a  program  to  determine  average  of  command  line  inputs

try:
	sum= ctr = 0
	print("Enter inputs(use ctrl+z for EOI):" ,end='')
	while True:
		x=eval(input( ))
		sum+=x
		ctr+=1
except EOFError:
	print(f'Average is {sum/ctr}')

# Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

 




 