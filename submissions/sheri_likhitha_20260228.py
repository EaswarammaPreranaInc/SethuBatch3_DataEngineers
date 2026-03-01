n=int(input("Enter lines: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print(chr(65+j),end="")
        print()



# Find  outputs  (Home  work)
for  i   in   range(1 , 8):        #1\nsec\nHello
	print(i)                        #2\nsec\nHello
	if   i % 3 == 0:                #4\nsec\nHello
		pass                        #5\nsec\nHello
		print('Hyd')                #6\nsec\nHello
	else:                           #7\nsec\nHello
		print('Sec')                
	print('Hello')
# End  of  the  loop
print('Outside loop')               #outside the loop


# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')            #1\nsec\nHello
	print('Hello')              #2\nsec\nHello
# End  of  the  loop            #3
print('Outside loop')