'''Write  a  program  to  print
       A
      A B
     A B C
   A B C D
  A B C D E

Input  is  number  of  lines'''


n=int(input("Enter number of lines:"))
for i in range(1,n + 1 ):
  print(" " * (n-i), end=" ")

for j in range(i):
  print(chr(65 + j), end=" ")
print()  
      


# Find Outputs

for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass()
	else:
		print('Sec')    # 1, 2,4,5,7,8                 3,6
	print('Hello')          Sec                    ouside loop
# End  of  the  loop            Hyd
print('Outside loop')           outside loop     after 3 it passes the loop





# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')     # exits the program and print Outside loop
	print('Hello')
# End  of  the  loop
print('Outside loop')







