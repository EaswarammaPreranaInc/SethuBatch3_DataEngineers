n = int(input("Enter number of lines: "))

for i in range(1, n + 1):
    
    # Print spaces
    for s in range(n - i):
        print(" ", end=" ")
    
    # Print alphabets
    ch = 'A'
    for j in range(i):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)   # increment character
    
    print()   # move to next line

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




# Find  outputs  (Home  work)
for  i   in   range(1 , 8):  # 1 2 3  Outside
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')