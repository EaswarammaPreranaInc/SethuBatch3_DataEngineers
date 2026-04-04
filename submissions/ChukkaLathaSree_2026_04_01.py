# Find  outputs
def  f1():
	a = 3
	if  a:
		print(a)
		a = a - 1
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
# End  of  the  function
a = 3
f1()
print('End') 


# 
3
2
1
0
Hello
Hi
0
Bye
None
End


# Toh:
def toh(n,p1,p2,p3):
 if n>0:
  toh(n-1,p1,p2,p3):
   for n>0:
    print(f'{p1} ---> {p3}')
     toh(n-1 , p1 , p2 , p3 )
       n = int(input('How many disks? :'))
       toh(n,1,2,3)


