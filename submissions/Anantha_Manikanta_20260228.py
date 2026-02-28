'''
1) Write  a  program  to  print
       A
      A B
     A B C
    A B C D
   A B C D E
'''
n = int(input("Enter number of lines: "))
for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end="")
    ch = 'A'
    # Print characters
    for j in range(i):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)

'''
2) # Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop') # 1 <nextline> Sec <nextline> Hello <nextline> 2 <nextline> Sec <nextline> Hello <nextline >3 <nextline> Hyd <nextline> Hello <nextline> 4 <nextline> Sec <nextline> Hello <nextline> 5 <nextline> Sec <nextline> Hello <nextline> 6 <nextline> Hyd <nextline> Hello<nextline> 7 <nextline> Sec <nextline> Hello <nextline> Outside loop

'''
'''
3) Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop') # 1 <nextline> Sec <nextline> Hello <nextline> 2 <nextline> Sec <nextline> Hello <nextline >3 

'''