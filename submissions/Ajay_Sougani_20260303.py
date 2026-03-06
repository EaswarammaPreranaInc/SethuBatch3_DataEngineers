
n = int(input("Enter the no. of elements to be printed: "));
x = int(input("Enter the value to be searched: "));
if n == 0:
    print("0");
else:
    a = 0;
    b = 1;
    c = a+b;
    for i in range(n):
        if a == x:
            print(x, "found");
            break;
        a = b;
        b = c;
        c = a+b;
    else:
        print("not found");


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




import sys

if len(sys.argv) < 2:
    print("Please provide a number as command line argument")
else:
    num = int(sys.argv[1])

    if num % 2 == 0:
        print(num, "is Even number")
    else:
        print(num, "is Odd number")

#average of command line inputs

import sys

if len(sys.argv)<2:
    print("provide inputs as command line arguments");
else:
    sum=0
    ctr = 0
    for i in range(1, len(sys.argv)):
        sum+=float(sys.argv[i]);
        ctr += 1
        avg = sum/ctr;
    print(F'Average: {avg:.2f}')

#arranging elements ascending or descending using command line argument 

import sys

if len(sys.argv)<2:
    print("provide inputs as command line arguments");
else:
    a = [int(i) for i in sys.argv[1:]];
    asc = sorted(a);
    print(asc)
    desc = sorted(a, reverse=True)
    print(desc)

        






        