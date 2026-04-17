# Find  outputs  (Home  work)
for  i   in   range(1 , 8):	#1<\n>Sec<\n>Hello
	print(i)		#2<\n>Sec<\n>Hello
	if   i % 3 == 0:	#3<\n>Hyd<\n>Hello
		pass		#4<\n>Sec<\n>Hello
		print('Hyd')	#5<\n>Sec<\n>Hello
	else:			#6<\n>Hyd<\n>Hello
		print('Sec')	#7<\n>Sec<\n>Hello
	print('Hello')
# End  of  the  loop
print('Outside loop')

_____________________________________________

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):#1<\n>Sec<\n>Hello
	print(i)	   #2<\n>Sec<\n>Hello
	if   i % 3 == 0:    #Outside he loop
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

_______________________________________________
Write  a  program  to  print
       A
      A B
     A B C
   A B C D
  A B C D E

n=int(input('Enter any number:'))
for i in range(1,n+1):
    
    for space in range(n-i):
        print(' ',end=' ')     
    
    ch="A"
    for j in range(i):
        print(ch, end='')
        ch=chr(ord(ch)+1)
    
    print()