# Write  a  program  to  search  for  'x'  in  fibonacci  series
x = int(input("Enter a number : "))
a, b = 0, 1
if x == 0 or x == 1:
    print("Found")
else:
    while b < x:
        c = a + b
        a = b
        b = c
    if b == x:
        print("Found")
    else:
        print("Not found")

# Modify  following   program  with  walrus  operator
try:
    sum = ctr = 0
    while True:
        sum += (x := eval(input('Enter input (ctrl + z to stop) : ')))
        ctr += 1
except EOFError:
    try:
        print(f'Average : {sum / ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')
except (NameError, TypeError):
    print('Input can not be string')

# Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number
import sys
try:
    if len(sys.argv) != 2:
        raise IndexError
    n = int(sys.argv[1])
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
except (IndexError, ValueError):
    print("Pls send an integer input")

# Write  a  program  to  determine  average  of  command  line  inputs
import sys
try:
    if len(sys.argv) == 1:
        raise IndexError
    a = [eval(x) for x in sys.argv[1:]]
    for x in a:
        if not isinstance(x, (int, float, bool)):
            raise TypeError
    print("Average :", sum(a) / len(a))
except:
    print("Pls send number inputs")

# Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order
import sys
try:
    if len(sys.argv) == 1:
        raise IndexError
    a = [eval(x) for x in sys.argv[1:]]
    has_number = any(isinstance(x, (int, float, bool)) for x in a)
    has_string = any(isinstance(x, str) for x in a)
    if has_number and has_string:
        raise TypeError
    print(sorted(a))
    print(sorted(a, reverse=True))
except IndexError:
    print("Pls send inputs")
except:
    print("Do not send number and string")