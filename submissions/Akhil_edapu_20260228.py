# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i) # it prints from 1 ,2,3,4....8
	if   i % 3 == 0: 
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello') 
	
#1 
#sec
#hello
#2 
#sec
#hello
#3
#hyd
#hello
#4
#sec 
#hello
#5
#sec 
#hello
#6
#hyd 
#hello
#7
#sec 
#hello


# End  of  the  loop
print('Outside loop')


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

#1 
#sec
#hello
#2 
#sec
#hello
#3
#hyd
#hello
#outside loop



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

n = int(input("Enter a number :"))

ch='A'

for i in range(1,n+1):
    
    for j in range(n-i):
        print(' ' , end='')
        
        
    print(ch * (2*i-1))
    ch = chr(ord(ch)+1)
