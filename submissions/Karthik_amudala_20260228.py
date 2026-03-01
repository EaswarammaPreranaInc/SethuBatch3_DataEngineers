Q) Write  a  program  to  print


       A
      A B
     A B C
   A B C D
  A B C D E

Input  is  number  of  lines

1)  ord('A') = 65
    ord('B') = 66
    ord('C') = 67
    .....
    ord('Z') = 90
	
2)  chr(65) = 'A'
    chr(66) = 'B'
    chr(67) = 'C'
    .....
    chr(90) = 'Z'
	
3)  ch = 'A'
    ch += 1
	 Is  the  statement  valid ?  ---> No	 becoz  operand2  should  be  a  sequence  when  operand1  is  a  sequence

4)  ch = 'A'
    How  to  increment  variable  ch  by  1 ?  --->  ch = chr(ord(ch) + 1)

#  n=int(input('How many lines : '))
   ch='A'
   for i in range(0,n):
       print(" " * (n-i),end='')
       for j in range(0,i+1):
           print(ch, end=' ')
           ch = chr(ord(ch) + 1)
       ch='A'
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

# 1
  Sec
  Hello
  2
  Sec
  Hello
  3
  Outside loop