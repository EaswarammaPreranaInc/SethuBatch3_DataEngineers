try:
    total_sum = ctr = 0
    while True:
        # Combined lines 8 and 9 using the walrus operator
        total_sum += (x := eval(input('Enter input (ctrl + z to stop) : ')))
        ctr += 1
except EOFError:
    try:
        print(f'Average : {total_sum / ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')
except (NameError, TypeError):
    print('Input can not be string')

'''
output
Enter input (ctrl + z to stop) : 4  
Enter input (ctrl + z to stop) : ^Z
Average : 4.0
'''


from sys import argv

if len(argv) < 2:
    print("Pls send an integer input")
else:
    try:
        number = int(argv[1])
        if number % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    except ValueError:
        print("Pls send an integer input")

'''
output
py fn.py 1 
Odd number
py fn.py 4
Even number
'''

from sys import argv
if len(argv) < 2:
    print("Pls send number inputs")
else:
    try:
        a = [float(x) for x in argv[1:]]
        result = sum(a) / len(a)
        print(f"Average: {result}")
    except ValueError:
        print("Pls send number inputs")

'''
output
py fn.py 1 2 3 4 
Average: 2.5
'''

from sys import argv

if len(argv) < 2:
    print("Pls send inputs")
else:
    try:
        a = [eval(x) for x in argv[1:]]
        print(sorted(a))
        print(sorted(a, reverse=True))
    except (NameError, SyntaxError):
        a = argv[1:]
        print(sorted(a))
        print(sorted(a, reverse=True))
    except TypeError:
        print("Do not send number and string")
		
'''
output
py fn.py 1 4 3 2
[1, 2, 3, 4]
[4, 3, 2, 1]
py fn.py 'Hyd' 'Cyb' 'Sec'
['Cyb', 'Hyd', 'Sec']
['Sec', 'Hyd', 'Cyb']
'''

