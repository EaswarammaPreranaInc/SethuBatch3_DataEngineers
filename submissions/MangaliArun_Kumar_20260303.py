# Modify  following   program  with  walrus  operator

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

from sys import argv
try:
	for i in range(1,len(argv)):
		num = int(argv[i])
		if num != 0:
		    if num % 2 == 0:
			    print("Even number")
		    else:
			    print("Odd number")
	    else:
			print("Pls send a positive num")
except:
	print("Pls send an integer input")
	
# Write  a  program  to  determine  average  of  command  line  inputs

from sys import argv
ttl = 0
try:
	for i in range(1,len(argv)):
		num = eval(argv[i])
		ttl += num
	avg = ttl/(len(argv)-1)
	print(F"average :{avg}")
except:
	print("Pls send an integer input")

# Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

from sys import argv
try:
    if len(argv) == 1:
        print("Pls send inputs")
    else:
        a = []
        for i in argv[1:]:
            a.append(eval(i))
        if all(type(x) == type(a[0]) for x in a):
            print(sorted(a))
            print(sorted(a, reverse=True))
        else:
            print("Do not send number and string")
except:
    print("Do not send number and string")
