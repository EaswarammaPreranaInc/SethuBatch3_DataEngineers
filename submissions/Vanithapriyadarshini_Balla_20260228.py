# Write  a  program  to  print  fibonacci  series  upto   x

x=int(input("Enter x value : "))
if x==0:
    print()
elif x==1:
    print(0)
else:
 f1=0
 f2=1
 f3=f1+f2
 print(f1)
 print(f2)
 while f3<x:
  f1=f2
  f2=f3
  print(f3)
  f3=f1+f2
print()

''' Write  a  program  to  print
       A
      A B
     A B C
   A B C D
  A B C D E '''

x=int(input("Enter x value : "))
ch=65
for i in range(1,x+1):
    print(' ' * (x-i),end='')
    for j in range(i):
        print(chr(ch+j),end=' ')
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

'''1<nl>Sec<nl>Hello<nl>2<nl>Sec<nl>Hello<nl>3<Hyd><nl><Hello><nl>4<nl>Sec<nl>Hello<nl>5<nl>Sec<nl>hello<nl>6<nl>Hyd<nl>Hello<nl>7<nl>Sec<nl>Hello
 Outside loop'''

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

''' 1<nl>Sec<nl>Hello<nl>2<nl>Sec<nl>Hello<nl>3




