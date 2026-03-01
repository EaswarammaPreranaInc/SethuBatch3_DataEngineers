# Write  a  program  to  print pyramid alphabets
n = int(input())
for i in range(1,n+1):
    for s in range(n-i):
         print(" ",end="")
    for ch in range(i):
         print(chr(65+ch),end=" ")
    print()

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd') # Hyd Hyd
	else:
		print('Sec')
	print('Hello') Hello Hello
# End  of  the  loop
print('Outside loop')

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello') Hello 
# End  of  the  loop
print('Outside loop')