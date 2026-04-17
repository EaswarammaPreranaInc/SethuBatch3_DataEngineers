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


a = int(input("Enter number of lines: "))
for i in range(1, a+1):
    print(" "*(a-i), end="")
    ch = 65
    for j in range(2*i-1):
        print(chr(ch), end="")
        ch += 1
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
print('Outside loop') #1<nextline>  sec <nextline> Hello <nextline>  2 <nextline> Sec <nextline> Hello <nextline> 3 <nextline> Hyd <nextline> Hello  <nextline> 4<nextline> Sec <nextline> Hello <nextline> 5 <nextline>  Sec <nextline> Hello <nextline> 6 <nextline>  Hyd <nextline> Hello <nextline> 7 <nextline>  Sec <nextline> Hello <nextline> Outside loop


# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop #1<nextline>  sec <nextline> Hello <nextline>  2 <nextline> Sec <nextline> Hello <nextline> 3
print('Outside loop') 