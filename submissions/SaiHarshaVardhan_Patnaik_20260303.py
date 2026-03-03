'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series'''

n = int(input("Enter number of terms: "))
x = int(input("Enter the number to search: "))

a, b = 0, 1
found = False

for i in range(n):
    if a == x:
        found = True
        break
    a, b = b, a + b

if found:
    print("Found")
else:
    print("Not found")

'''
Output:
Enter number of terms: 10
Enter the number to search: 5
Found
'''

'''
Modify  following   program  with  walrus  operator

Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
'''
try:
	sum =  ctr = 0
	while  True:
		 sum += (x:= eval(input('Enter input  (ctrl + z  to  stop)  :  ')))
		 ctr +=1
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string')

'''Output:
Enter input  (ctrl + z  to  stop)  :  1
Enter input  (ctrl + z  to  stop)  :  2
Enter input  (ctrl + z  to  stop)  :  3
Enter input  (ctrl + z  to  stop)  :  4
Enter input  (ctrl + z  to  stop)  :  ^Z
Average :   2.5'''

'''
Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number

1) py  prog3.py  26
    What  is  the  output ?  ---> Even  number

2) py  prog3.py  45
    What  is  the  output ?  ---> Odd  number

3) py  prog3.py
    What  is  the  output  ?  --->  Pls  send  an  integer  input

4) py  prog3.py  10.8
    What  is  the  output ?  ---> Pls  send   an  integer  input

5) py  prog3.py  Ten
    What  is  the  output  ?  ---> Pls  send   an  integer  input
'''
from sys import argv

# Check if exactly one argument is passed
if len(argv) != 2:
    print("Pls send an integer input")
else:
    try:
        num = int(argv[1])   # Convert input to integer

        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

    except ValueError:
        print("Pls send an integer input")

'''
Output:PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/Python/SaiHarshaVardhan_Patnaik_20260303.py" 26
Even number
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/Python/SaiHarshaVardhan_Patnaik_20260303.py"45
Odd number
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/Python/SaiHarshaVardhan_Patnaik_20260303.py"
Pls send an integer input
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/Python/SaiHarshaVardhan_Patnaik_20260303.py" 10.8
Pls send an integer input
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/Python/SaiHarshaVardhan_Patnaik_20260303.py" Ten 
Pls send an integer input'''

'''
Write  a  program  to  determine  average  of  command  line  inputs

1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
    What  is  argv ?  --->  ['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
    What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
	How  to  determine  sum  of  list  elements ?  ---> sum(a)
    How  to  determine  number  of  list  elements ?  ---> len(a)

2) py   prog4.py
    What  is  the  output ?  --->  Pls  send  number  inputs

3) py   prog4.py  25   'Ten'
    What  is  the  output  ?  --->  Pls  send  number  inputs
'''
from sys import argv

if len(argv) == 1:
    print("Pls send number inputs")
else:
    try:
        a = []
        for value in argv[1:]:
            a.append(eval(value))

        for item in a:
            if not isinstance(item, (int, float, bool)):
                raise ValueError

        avg = sum(a) / len(a)
        print("Average =", avg)

    except:
        print("Pls send number inputs")

'''Output: PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/Python/SaiHarshaVardhan_Patnaik_20260303.py" 10.8 25 True 14.6 19 False 7.4
Average = 11.114285714285714'''
