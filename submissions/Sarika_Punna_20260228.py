'''
Write  a  program  to  print
       A
      A B
     A B C
    A B C D
   A B C D E

Input  is  number  of  lines

1) ord('A') = 65
    ord('B') =  66
    ord('C') = 67
	.....
	ord('Z') = 90
	
2) chr(65) = 'A'
    chr(66) =  'B'
    chr(67) = 'C'
	.....
	chr(90) = 'Z'
	
3) ch = 'A'
     ch += 1
	 Is  the  statement  valid ?  ---> No	 becoz  operand2  should  be  a  sequence  when  operand1  is  a  sequence

4) ch = 'A'
    How  to  increment  variable  ch  by  1 ?  --->  ch = chr(ord(ch) + 1)
'''
n=int(input())
for i in range(n):
    print(" "*(n-i-1),end="")
    for k in range(65,65+1+i):
        print(chr(k),end=" ")
    print(" "*(n-i-1),end="")
    print()

# Find  outputs  (Home  work)
for i in range(1 , 8):
    print(i)                 # 1  2  3  4  5  6  7
    if i % 3 == 0:
        pass
        print('Hyd')         # Hyd  (when i = 3, 6)
    else:
        print('Sec')         # Sec  (when i = 1, 2, 4, 5, 7)
    print('Hello')           # Hello (7 times)
print('Outside loop')        # Outside loop

'''
exact output
1
Sec
Hello
2
Sec
Hello
3
Hyd
Hello
4
Sec
Hello
5
Sec
Hello
6
Hyd
Hello
7
Sec
Hello
Outside loop
'''

# Find  outputs  (Home  work)
for i in range(1 , 8):
    print(i)                 # 1  2  3
    if i % 3 == 0:
        exit()               # Stops program when i = 3
    else:
        print('Sec')         # Sec (when i = 1, 2)
    print('Hello')           # Hello (when i = 1, 2)

print('Outside loop')        # Not executed
'''
exact output
1
Sec
Hello
2
Sec
Hello
3
'''
