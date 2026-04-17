Name-Dhruva Gupta
Roll Number-D238

1)
try:
    sum = ctr = 0
    while True:
        sum += (x := eval(input('Enter input (ctrl + z to stop): ')))
        ctr += 1
except EOFError:
    try:
        print(f'Average : {sum / ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')
except (NameError, TypeError):
    print('Input cannot be string’)

2)
import sys
if len(sys.argv) != 2:
    print("Pls send an integer input")
else:
    try:
        num = int(sys.argv[1])  
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

    except ValueError:
        print("Pls send an integer input”)

3)
import sys
if len(sys.argv) == 1:
    print("Pls send number inputs")
else:
    try:
        a = [eval(i) for i in sys.argv[1:]]
        print("Average :", sum(a) / len(a))
    except:
        print("Pls send number inputs”)

4)
import sys
if len(sys.argv) == 1:
    print("Pls send inputs")
else:
    try:
        a = [eval(i) for i in sys.argv[1:]]
        if type(a[0]) == type(a[-1]):
            print(sorted(a))
            print(sorted(a, reverse=True))
        else:
            print("Do not send number and string")

    except:
        print("Do not send number and string")