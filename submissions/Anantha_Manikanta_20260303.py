'''
1) Modify  following   program  with  walrus  operator
Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
'''
try:
    sum = ctr = 0
    while True:
        sum += (x := eval(input('Enter input  (ctrl + z  to  stop)  :  ')))
        ctr += 1
except EOFError:
    try:
        print(F'Average :   {sum / ctr}')
    except ZeroDivisionError:
        print('Enter  at  least  one  input')
except (NameError , TypeError):
    print('Input  can  not  be  string')
'''
2) Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number
'''
import sys
try:
    n = int(sys.argv[1])
    if n % 2 == 0:
        print('Even number')
    else:
        print('Odd number')
except (IndexError, ValueError):
    print('Pls send an integer input')
'''
3) Write  a  program  to  determine  average  of  command  line  inputs
'''
import sys
try:
    a = []
for x in sys.argv[1:]:
    a.append(eval(x))
    print('Average : ', sum(a) / len(a))
except (IndexError, TypeError, NameError):
    print('Pls send number inputs')
'''
4) Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order
'''
import sys
try:
    a = []
    for x in sys.argv[1:]:
        a.append(eval(x))
    print(sorted(a))
    print(sorted(a, reverse=True))
except IndexError:
    print('Pls send inputs')
except:
    print('Do not send number and string')