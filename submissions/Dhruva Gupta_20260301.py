Name-Dhruva Gupta
Role Number-D238

1)
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

Output-
1
Sec
Hello
2
Sec
Hello
3

2)
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop’)

Output-
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

3)
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
        

4)
n = int(input("Enter the number rows you require: "))
for i in range(n):
    ch = 65   # Reset to 'A' for every row
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i + 1):
        print(f" {chr(ch)} ", end=" ")
        ch = ch + 1   # Increase ASCII value
    print()
