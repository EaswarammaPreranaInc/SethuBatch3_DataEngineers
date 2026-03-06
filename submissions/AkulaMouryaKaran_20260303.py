import math
x=int(input('Enter a number:'))

def is_perfect_square(n):
    s=int(math.sqrt(n))
    return s*s==n
if is_perfect_square(5*x*x+4) or is_perfect_square(5*x*x-4):
    print('Found')
else:
    print('Not found')
##############################################################
try:
    sum=ctr=0
    while True:
        sum+=(x:=eval(input('Enter input (Ctrl+Z to stop):')))
        ctr+=1
except EOFError:
    try:
        print(f'Average: {sum/ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')
except (NameError,TypeError):
    print('Input can not be string')
###############################################################
from sys import argv

if len(argv)!=2:
    print('Pls send an integer input')
else:
    try:
        n=int((argv[1]))

        if n%2==0:
            print('Even number')
        else:
            print('Odd number')
    except ValueError:
        print('Pls send an integer input')
#################################################################
from sys import argv

if len(argv)==1:
    print('Pls send number inputs')
else:
    try:
        a=[]
        for x in argv[1:]:
            a.append(eval(x))

        avg=sum(a)/len(a)
        print('Average:',avg)
    except (NameError,TypeError):
        print('Pls send number inputs')
###################################################################
from sys import argv

if len(argv)==1:
    print('Pls send inputs')
else:
    try:
        a=[]

        for x in argv[1:]:
            a.append(eval(x))
        
        first_type=type(a[0])

        for item in a:
            if type(item)!=first_type:
                raise TypeError
        
        print(sorted(a))
        print(sorted(a,reverse=True))
    except:
        print('Do not send number and string')
