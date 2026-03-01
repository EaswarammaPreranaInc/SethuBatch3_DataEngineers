n = int(input("Number of lines: "))
i = 1
a =ord('A')

while i <= n:
    print(" " * (n - i), end="")
    j = 0
    while j < i:
        print(chr(a + j), end=" ")
        j = j + 1
    print()
    i = i + 1
----------------------------------------

for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')  

# 1
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

----------------------------------
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

#1
Sec
Hello
2
Sec
Hello
3