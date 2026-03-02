
x = int(input('Enter value of x : '))

if x < 0:
    print('Invalid input')

elif x == 0:
    print('Fibonacci Series')
    print(0)

else:
    a = 0
    b = 1
    print('Fibonacci Series')
    print(a)
    print(b)

    c = a + b
    while c <= x:
        print(c)
        a = b
        b = c
        c = a + b




n = int(input("Enter number of lines: "))

for i in range(1, n + 1):
    
    for space in range(n - i):		# print leading spaces
        print("  ", end="")
				    # Print alphabets
    ch = 'A'
    for j in range(i):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)		# Increment character
    
    print()   			# Move to next line




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



1
Sec
Hello
2
Sec
Hello
3