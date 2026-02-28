'''
Write  a  program  to  print
	  A          7
     A B         6
    A B C        5
   A B C D       3
  A B C D E      2

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

n=int(input('Enter number of lines: '))
for i in range(1,n+1):
    code=ord('A')
    print(' '*(2*n-i),end="")
    for j in range(i):
        print(chr(code+j),end=" ")
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
'''
1
sec
Hello
2
sec
Hello
3
Hyd
Hello
4
sec
Hello
5
sec
Hello
6
Hyd
Hello
7
sec
Hello
Outside loop'''

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

'''
1
sec
Hello
2
sec
Hello
3
'''