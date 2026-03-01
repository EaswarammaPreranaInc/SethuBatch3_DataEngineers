'''
Write  a  program  to  print  fibonacci  series  upto   x
Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 
1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term
2) What  are  the  first  two  terms ?  --->  0  and  1
3) Hint:  Use  while  loop
'''
x = int(input('Enter  value  of  x  :  '))  #  
if  x < 0:
	print('Invalid  input')
elif  x == 0:
	print('Fibonacci  series')
	print(0)
else:
	a = 0
	b = 1
	print('Fibonacci  Series')
	print(a)
	print(b)
	c = a + b  
	while  c <= x:  #  3 <= 10
		print(c)
		a = b
		b = c
		c = a + b


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
n = int(input('Enter number of lines: '))
for i in range(1, n + 1):
    for s in range(n - i): # Print spaces
        print(" ", end="")
    ch = 'A'   # Starting character
    for j in range(1, i + 1): # Print alphabets
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)   # Increment character properly
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
#Answer
'''
1<nextline>Sec<nextline>Hello<nextline>2<nextline>Sec<nextline>Hello<nextline>3<nextline>Hyd<nextline>Hello<nextline>4<nextline>Sec
Hello<nextline>5<nextline>Sec<nextline>Hello<nextline>6<nextline>Hyd<nextline>Hello<nextline>7<nextline>Sec<nextline>Hello<nextline>Outside loop
'''
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
#Answer
'''
1<nextline>Sec<nextline>Hello<nextline>2<nextline>Sec<nextline>Hello<nextline>3
'''