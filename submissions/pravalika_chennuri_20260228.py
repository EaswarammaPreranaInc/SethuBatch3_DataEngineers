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
n = int(input("enter a number : "))
s = n-1
for i in range(1,n+1):
    print(" "*s,end="")
    for j in range(i):
        print(chr(65 + j), end=" ")
    s-=1
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
print('Outside loop') # 1 <nextline> Sec <nextline> Hello 2 \n Sec \n Hello \n 3 \n Hyd \n Hello \n 4 \n Sec \n........outside loop

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit() # stops execution
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
