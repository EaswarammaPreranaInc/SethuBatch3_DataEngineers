n=int(input("Enter the no. of elements: "))

x=int(input("Enter element to find: "))

a=0
b=1
d=[]
for i in range(0,n):
    d.append(a)
    c=a+b
    a=b
    b=c
    
for i in range(0,n):
    if(d[i] == x):
        print(f"Found at: {i}")
        break
else:
    print("Not found")




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
        print("Pls send an integer input")




import sys
if len(sys.argv) < 2:
    print("Pls send number inputs")
else:
    try:
        # Convert all command line inputs to float
        a = [float(x) for x in sys.argv[1:]]
        average = sum(a) / len(a)
        print("Average:", average)
    except ValueError:
        print("Pls send number inputs")



import sys
if len(sys.argv) < 2:
    print("Pls send inputs")
else:
    inputs = sys.argv[1:]
    try:
        a = [float(x) for x in inputs]
        print("Ascending  :", sorted(a))
        print("Descending :", sorted(a, reverse=True))
    except ValueError:
        if all(not x.replace('.', '', 1).isdigit() for x in inputs):
            print("Ascending  :", sorted(inputs))
            print("Descending :", sorted(inputs, reverse=True))
        else:
            print("Do not send number and string")

