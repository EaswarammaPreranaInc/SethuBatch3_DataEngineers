'''
Write  a  program  to  print
	   A
      A B
     A B C
   A B C D
  A B C D E



n = int(input('value: '))
for i in range(1, n+1):
    print(' '*(n-i), end='')
    for j in range(1, i+1):
        print(chr(64+j) + ' ', end='')
    print()




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

Output:
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

Output:
1
Sec
Hello
2
Sec
Hello
3