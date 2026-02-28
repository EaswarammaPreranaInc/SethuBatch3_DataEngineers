'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''


x = int(input('Enter the value of x : '))
print('Fibonacci squence ')
a = 0
b = 1
while a <= x:
    print(a)
    c = a + b
    a = b
    b = c


# Find  outputs  (Home  work)
#How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
a = [10 , 20 , 15 , 18]
for x in a:
    print(x)
print()
#How  to  print  each  character  of   string  'Hyd'  with  for  loop
a = 'Hyd'
for x in a :
    print(x)
print()
#How  to  print  each  element  of   range(5)  with  for  loop
a = range(5)
for x in a :
    print(x)


# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) #10 <nextline> 30 <nextline> 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) #20 <nextline> 40 <nextline> 60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items(): #list(tuple(items))
	print(x) #(10,20) <nextline> (30,40) <nextline> (50,60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) #10 <nextline> 30 <nextline> 50


# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') #10...20 <nextline> 30...40 <nextline> 50...60
#for  x ,  y  in   a:
	#print(x , y ) # Error 
#for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	#print(x , y , sep = '...') #Error 

# Identify  error  (Home  work)
#for  x  in   123: #Error we can't iterate through non squence 
        #print(x)


# Find  outputs  (Home  work)
for  x   in   ():
        print(x) #nothing is printed 
for  x   in  []:
        print(x) #nothing is printed 
for  x   in   {}:
        print(x) #nothing is printed 
for  x   in   set(): 
        print(x) #nothing is printed 
for  x   in   '':
        print(x) #nothing is printed because there is nothing to iterate 
#for  x  in  range(10 , 10):
	print(x) #Error
#for  x  in   range():
	print(x) #Error atleast one  argument need to be provided 
#for  x  in   (25): 
	print(x) #Error we can't iterate through the non squence 


#  Nested  Loop  demo  program
for  i  in  range(1 , 4): #1 2 3
#	for  j  in  range(1 , 5): 1 2 3 4 
			#print(i ,  j)  #Error because there is 3 elements in i and 4 elements in j
	print('Hello') #Hello <nextline> Hello <nextline>
print('Bye') #Bye


# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
#How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
for i in range(len(a)): #0 1 2 3 
    print(i,a[i]) #a[0] = 25 , a[1] = 10.8 , a[3] = 'Hyd' , a[4] = True
print('For each loop')
#How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
for x in a:
    print(x)


#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
#How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(1,len(a)+1): # 1 2 3 4
    print(a[-(i)])
#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
for x in reversed(a) :
    print(x)


'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
for i in range(len(a)):
    c.append(a[i]+b[i])
print('3rd  list : ' , c)
#How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)



#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
b = (a[2:5])
for i in range(len(b)):
    print(b[i])
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
c = 0
for x in a :
    if c >= 2 and c <= 5:
        print(x)
    c +=1


#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)): #0 1 2 3
	a[i] +=  1 # 10 = 10+1
print('a :  ' , a) #[11,21,16,19]
b = [10 , 20 , 15 , 18]
for  x  in   b: #[10,20,15,18]
	x += 1 # increments x, but not the list element because x is a copy of value but not a reference
print('b :  ' ,  b)


'''
Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>***
<2 spaces>*****
<1  space>*******
<0  spaces>*********

Input  is  number  of  lines
'''

a = int(input('Enter any integer(1-10) : ')) #5
for i in range(1,a+1) : # 1 2 3 4 5 
    print(' '*(a-i) + '*'*(2*i - 1 )) #2*1 - 1 = 1*'*' = * ,2*2 -1 = 3*
    


'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''

count = 1
even = 2
print('first 20 even numbers ')
while count <= 20:
    print(even)
    even += 2
    count += 1
    


'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''

count = 1
odd = 1
print('First 20 odd numbers ')
while count <= 20:
    print(odd)
    odd+=2
    count +=1


'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''

a = int(input('Enter value of n : '))
count = 1
n = 1
print('Natural Numbers ')
while count <= a:
    print(n)
    n += 1
    count += 1

    

'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
a =int(input('Enter value of n : '))

while a >= 1:
    print(a)
    a-=1


'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''
n = int(input('Enter any number : '))
sum = 0
for i in range(1,n+1):
    sum += 1.1 * i
print(f'{sum = }')


'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''
sum = 0
for i in range(1,21):
    sum += 2 * i
print(f'sum of first 20 even numbers is : {sum}')


'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''


sum = 0
for i in range(1,21):
    sum+= 2*i-1
print(f'sum of first 20 odd numbers is : {sum}')



'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''

n = int(input('How many terms would you like to add  : '))
sum = 0
for i in range(1,n+1):
    sum+=i
print(f'sum of first {n} terms is : {sum}')


# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i) # 1 
	if  i % 3  == 0: #i = 3 --> 3 == 3 then it moves to next iteration 
			continue
	else:
			print('Sec') #Sec
	print('Hello') #Hello
# End of loop
print('Outside loop') #outside of loop 



# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue #without for or while loop we can't use continue 
	print('Sec')


# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop') 
#1 <nextline> Sec <nextline> Hello <nextline> 2 <nextline> Sec <nextline> Hello <nextline> 3 <nextline> Outside loop



# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break #we can't use continue or break without for or while loop
	print('Sec')

