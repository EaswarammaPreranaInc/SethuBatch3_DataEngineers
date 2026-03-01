'''Write  a  program  to  print
       A
      A B
     A B C
   A B C D
  A B C D E

Input  is  number  of  lines'''

n = int(input("Enter number of lines: "))

i = 1
while i <= n:
    
    space = n - i
    while space > 0:
        print(" ", end="")
        space -= 1

    k = 0
    while k < i:
        print(chr(65 + k), end=" ")
        k += 1

    print()
    i += 1



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
print('Outside loop')
#O/P:
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
Outside Loop





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
#O/P:
1
Sec
Hello
2
Sec
Hello
3
