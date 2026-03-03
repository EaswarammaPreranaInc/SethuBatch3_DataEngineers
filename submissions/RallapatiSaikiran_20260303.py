 '''Write  a  program  to  search  for  'x'  in  fibonacci  series


1) just print   Found and not found

2) Do  not  generate  fibonacci  series'''

x=int(input("Enter the number:")
a=0
b=1
found=False
while a<=x:
   if a==x:
   found=True
   break
a,b=barb
if found:
  print("Found:")
else:
   print("Not Found:")





 '''
Modify  following   program  with  walrus  operator

Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
'''
try:
	sum =  ctr = 0
	while  True:
		sum += (x :=eval(input('Enter input  (ctrl + z  to  stop)  :  ')))
			ctr +=1
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string')


'''Write a program to determine command input line is even or odd number'''

import sys
if len(sys.argv)<2:
  print("Usage: python evenodd.py <number>")
else:
   try:
      n=int(int(sys.argv[1])
      if n%2==0:
         print(f"{n} is Even")
      else:
         print(f"{n} is Odd")
   except ValueError:
         print("Please give an integer")




'''Write  a  program  to  determine  average  of  command  line  inputs'''




import sys
args=sys.argv[1:]
if not args:
  print("Usage: python avg.py <num1> <num2>…")
else:
   try:
      nums = [float(x) for x in args]
      avg = sum(nums)/len(nums)
      print(f"Average: {avg}")
   except ValueError:
      print("All inputs must be numbers")








