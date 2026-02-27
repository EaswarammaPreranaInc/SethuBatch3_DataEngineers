''' 
Write  a  program  to  determine  bill  amount  and  input  is  units
Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)                    Rs. 3.00 / unit
Next  100  units(100 - 199)                 Rs. 3.50 / unit
Next  200  units(200 - 399)                 Rs. 4.00 / unit
Next  300  units(400 - 699)                 Rs. 4.50 / unit
Above  700  units(units >= 700)             Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ?
--->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
units = int(input('Enter  units :   '))   #   175
match  units // 100:
	case  0:   #   units  between  0  and  99
				cost = units * 3.00
	case  1:  #  units  between  100 and  199
				cost =  100 * 3.00 + (units - 100) * 3.50
	case  2:
				cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.0
	case  3:
				cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.0 + (units - 400) *4.5

	case  4:				
				cost =  100 * 3.00 + 100 * 3.50 + 200 * 4.0 + 300 *4.5 + (units - 700) * 5.0

print('Bill  amount  :  ' , cost)


#-----------------------------------------------------------------------------

x = int(input('Enter value of x :'))

a = 0
b = 1
c = a + b

print('Fibanocci series')
print(f'{a}')
print(f'{b}')

while c < x:
    print(f'{c}')
    a = b
    b = c
    c = a + b


#-------------------------------------------------------------------------------


a = eval(input('Enter any sequence with quotes on : '))
i = 0

while i <= len(a):
    print(a[i])
    i += 1
    if i == len(a):
        break


#-------------------------------------------------------------------------
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}.keys():
    print(x) # 10 <next line > 30 <next line> 50

print() # Empty

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}.values():
    print(x)  # 20 <next line > 40 <next line> 60

print() # Empty

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}.items():
    print(x) # (10,20) <next line > (30,40) <next line> (50,60)

print() # Empty


for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
    print(x)  # 10 <next line > 30 <next line> 50


#-------------------------------------------------------------------------

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')  ## 10...20 <next line > 30...40 <next line> 50...60
for  x ,  y  in   a:
	print(x , y  # Error because closing parentheses is missing
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # Error

#-------------------------------------------------------------------------------------

# Identify  error  (Home  work)
for  x  in   123:
        print(x) # error because 123 is an interger it can't separate like string



#--------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
for  x   in   ():
        print(x) #empty
for  x   in  []:
        print(x) #empty

for  x   in   {}:
        print(x) #empty
for  x   in   set():
        print(x) #empty
for  x   in   '': 
        print(x) #empty
for  x  in  range(10 , 10):
	print(x)
for  x  in   range(): 
	print(x)  # error because range can't be zero
for  x  in   (25): 
	print(x)  # error because range function is missing

#-----------------------------------------------------------------------------------

for  i  in  range(1 , 4):
    for  j  in  range(1 , 5):
        print(i ,  j)
    print('Hello')

print('Bye')

#----> output 
"""
1 1
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
"""

#-----------------------------------------------------------------------------------------------

a = eval(input('Enter a Sequence :'))  # 5

b = []

for x in a:
    print(x, end = ' ')
    b.append(x)
    print(len(b)-1)



for i in range(len(a)):
    print(i)
    print(a[i])



for x in enumerate(a):
    print(x)

#----------------------------------------------------------------------

a = eval(input('Enter a Sequence : '))

for i in range(-1,-len(a)-1, -1):
    print(a[i])

for x in reversed(a):
    print(x)

#---------------------------------------------------------------------------

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []

for x,y in zip(a,b):
    c.append(x+y)
    print('3rd  list : ' , c)
#----------------------------------------------------------------------


a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

print('Indexed for loop')

for i in range(len(a)):
    if i >=2 and i < 5:
        print(a[i])

#------------------------------------------------------------------------

for x in a:
    if 2 <= a.index(x) <= 4:
        print(x)

#----------------------------------------------------------------------

a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
    a[i] +=  1
print('a :  ' , a) # a :   [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]

for  x  in   b:
    x += 1
    print(x)
print('b :  ' ,  b) # b :   [10, 20, 15, 18]

#------------------------------------------------------

'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2 spaces>*****
<1  space>*******
<0  spaces>*********

Input  is  number  of  lines
'''
a=5
for i in range(1,a+1):
    space=" "
    b=((a-i)*space)+((i*2)-1) * "*"
    print(b)

#-----------------------------------------------------------

a = eval(input('Enter number of even numbers :  '))

i = 0
while i<=a:
    print(2*i)
    i+=1
print('Bye')

#-------------------------------------------------------

a = eval(input('Enter number of odd numbers :  '))

i = 1

while i<=a:
    print(2*i-1)
    i+=1

print('Bye')

#-----------------------------------------------------------

a = eval(input('Enter number of natural numbers :  '))

i = 0

while i<= a:
    print(i)
    i+=1

#----------------------------------------------------------------------

a = eval(input('Enter number of natural numbers to be reversed :  '))

i = a

while i > 0:
    print(i)
    i-=1

print('Bye')

#----------------------------------------------------------------------

a = int(input('How many terms would you like to add :  '))

sum = 0

for i in range(1,a+1):
    x = 1.1*i
    sum+=x

print(f'{sum:.1f}')

#----------------------------------------------------------------------

a = int(input('enter a integer :  '))

sum = 0

for i in range(0,a+1):
    x = 2*i
    sum = sum+x

print('Sum of first 20 even numbers :', sum)

#------------------------------------------------------------------------

a = int(input('enter a integer :  '))

sum = 0

for i in range(1,a+1):
    x = 2*i-1
    sum = sum+x

print('Sum of first 20 odd numbers :', sum)

#---------------------------------------------------------------------------

a = int(input('enter a integer :  '))

sum = 0

for i in range(1,a+1):
    x = i
    sum = sum+x

print('Sum of first numbers :', sum)

#---------------------------------------------------------------------------

for  i   in   range(1 , 8):

    print(i)

    if  i % 3  == 0:
        continue
    else:
        print('Sec')

    print('Hello')

print('Outside loop')

#----> output
1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
Outside loop
#----------------------------------------------------------------------------

if ():
    print('Hyd')
    continue 	# error
    print('Sec')

#--------------------------------------------------------------------------

for  i   in   range(1 , 8):
    print(i)# 1
    if   i % 3 == 0:
        break
    else:
        print('Sec')
    print('Hello')
print('Outside loop')

#-----> output
1
Sec
Hello
2
Sec
Hello
3
Outside loop

#---------------------------------------------------------------------------
if(10 , 20 , 30):
    print('Hyd')
    break	# error
    print('Sec')