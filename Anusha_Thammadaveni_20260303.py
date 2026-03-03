'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''







x = int(input("Enter number: "))

a = 0
b = 1

if x == 0:
    print("Found")
else:
    while b <= x:
        if b == x:
            print("Found")
            break
        a, b = b, a + b
    else:
        print("Not found")








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







import sys

# If no inputs given
if len(sys.argv) == 1:
    print("Pls send inputs")
    sys.exit()

data = sys.argv[1:]   # Ignore file name
a = []

for item in data:
    try:
        if '.' in item:
            a.append(float(item))
        else:
            a.append(int(item))
    except:
        # If conversion fails, treat as string
        a.append(item)
else:
    print(sorted(a))                  
    print(sorted(a, reverse=True))       

