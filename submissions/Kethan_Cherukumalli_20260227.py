u = int(input('Enter  units :   '))   #   175
match  u // 100:
	case  0:   #   units  between  0  and  99
				cost = u * 3.00
	case  1:  #  units  between  100 and  199
				cost =  100 * 3.00 + (u-100) * 3.50
	case  2 | 3:
				cost = 100*3 + 100 * 3.50 + (u-200)*4
	case  4 | 5 | 6:
				cost = 100*3 + 100 * 3.50 + 200*4 + (u-300)*4.50
	case  _:				
				cost = 100*3 + 100*3.50 + 200*4 + 300*4.50 + (u-700)*5
print('Bill  amount  :  ' , cost)
----------------------------------------------------------------------------------------


----------------------------------------------------------------------------------------

# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop   

# for x in [10 , 20 , 15 , 18]:
	print (x)

How  to  print  each  character  of   string  'Hyd'  with  for  loop

# for x in 'Hyd':
	print (x)

How  to  print  each  element  of   range(5)  with  for  loop

# for x in range(5):
	print (x)
----------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)  # 10 <nl> 30 <nl> 50 
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)  # 20 <nl> 40 <nl> 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)  # (10, 20)
		    (30, 40)
		    (50, 60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)  # 10 <nl> 30 <nl> 50 

----------------------------------------------------------------------------------------
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')  # 10...20 nl 30...40 nl ... 50...60
for  x ,  y  in   a:
	print(x , y) #error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')  #error
----------------------------------------------------------------------------------------

# Identify  error  (Home  work)
for  x  in   123:
        print(x)  #error
----------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
for  x   in   ():
        print(x)  #
for  x   in  []:
        print(x)  #
for  x   in   {}:
        print(x)  #
for  x   in   set():
        print(x)  #
for  x   in   '':
        print(x)  #
for  x  in  range(10 , 10):
	print(x)  #
for  x  in   range():
	print(x)  #error
for  x  in   (25):
	print(x)  #error
----------------------------------------------------------------------------------------
#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  
	print('Hello')
print('Bye')

#1 1
1 2
1 3
1 4
Hello
2 1
2 2
2 3
2 4
Hello
3 1
3 2
3 3
3 4
Hello
Bye		
----------------------------------------------------------------------------------------
	
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')


#a = [25 , 10.8 , 'Hyd' , True]
for i in range(len([25 , 10.8 , 'Hyd' , True])):
	print (i, a[i], sep = '-->')



----------------------------------------------------------------------------------------

How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop


a = [25 , 10.8 , 'Hyd' , True]
for i in range(len([25 , 10.8 , 'Hyd' , True])):
	print (a[::-1])
	break
----------------------------------------------------------------------------------------

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)  # a : 11 nl a : 21 nl  a : 16 nl a : 19
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)  # [10 , 20 , 15 , 18]
----------------------------------------------------------------------------------------
n = int(input('How many lines ?: '))
for x in range(n):
    print(' '*(n-x-1)+'*'*(2*x+1))
----------------------------------------------------------------------------------------
print('first  20  even  numbers ')
a=1
while a<21:
    print(2*a)
    a=a+1
    
print('Bye')
----------------------------------------------------------------------------------------
print('first  20  odd  numbers ')
a=0
while a<20:
    print(2*a+1)
    a=a+1
    
print('Bye')
----------------------------------------------------------------------------------------
n = int(input('enter value of n: '))
print('natural numbers ')
a=1
while a<=n:
    print(a)
    a=a+1
----------------------------------------------------------------------------------------

print('numbers from 10 to 1 in steps of -1')
a=10
while a>=1:
    print(a)
    a=a-1
----------------------------------------------------------------------------------------
n = int(input('how many no.of terms would you like to add '))
for x in range(n+1):
    a= 1.1*x
    a =+a
    print(a)
----------------------------------------------------------------------------------------

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

#Sec Sec 3 Sec Sec 6 Sec Sec Hello Outside loop

----------------------------------------------------------------------------------------
# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')  #error
----------------------------------------------------------------------------------------
# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')  #error

----------------------------------------------------------------------------------------
