Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop

# Program:
x=int(input('Enter a number :'))
a=0
b=1
while a <= x:
    print(a)
    c=a+b
    a=b
    b=c



# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
# a=[10 , 20 , 15 , 18]
for i in a:
	print(i)
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
#str='Hyd'
for i in str:
	print(i)
How  to  print  each  element  of   range(5)  with  for  loop
#for in range(5):
	print(i)



# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # 10, 30, 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # 20, 40, 50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # (10,20),(30,40),(50,60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10
                   30
                   40




# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') 
# 10...20
30...40
50...60
for  x ,  y  in   a:
	print(x , y) # Error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')
# Error





# Identify  error  (Home  work)
for  x  in   123:

        print(x)  # Error




# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # () Nothig
for  x   in  []:
        print(x)  # [] Nothing
for  x   in   {}:
        print(x)  # Nothing
		
for  x   in   set():
        print(x) # Noting
for  x   in   '':
        print(x) # Nothing
for  x  in  range(10 , 10):
	print(x) # Nothing
for  x  in   range():
	print(x) # Error
for  x  in   (25):
	print(x) # Error






#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  # 
	print('Hello')                    
print('Bye')                             
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
                                        



# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

# a = [25 , 10.8 , 'Hyd' , True]
  for i in range(4):
    print(i,a[i])
  print(i)

# a = [25 , 10.8 , 'Hyd' , True]
   Not possible -- it connot track indexes
  

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

#a = [25 , 10.8 , 'Hyd' , True]
 for i in range(1,5) 
     print(a[-i])
#a = [25 , 10.8 , 'Hyd' , True]
 Not possible


Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)

Program:
a=[10 , 20 , 15 , 18]
b=[30 , 40 , 35 , 12 , 100 , 200 , 300]
c=[]
small=min(len(a),len(b))
for in range(small):
    c.append(a[i]=b[i])
print(c)



#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice 

Program:
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for i in range(2,5):
  print(a[i])


# Not Possible

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) #[11,21,16,19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)  #[10 , 20 , 15 , 18]






Write  a  program  to  print  full  pyramid
<4  spaces>*
<3  spaces>*
<2 spaces>***
<1  space>***
<0  spaces>***

Input  is  number  of  lines

Program:
n=int(input('How many line :'))
s=-1
for i in range(1,n+1):
 print(' '*s, end='')
 print('*'*(2*i-1))
 s-=1


(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop

Program:
print('First 20 even Numbers')
i=1
while i<=20:
 print(2*i)
 i+=1
print('Bye')


Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object
4) Use  while  loop

Program:

int('First 20 odd Numbers')
i=1
while i<=20:
 print(2*i-1)
 i+=1
print('Bye')




Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop





Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop




Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop

Program:
n=int(input('enter num :'))



Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop





Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''




Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop



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

# 1
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


# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec') # Error not using loop





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

# 1
  Sec
  Hello
  2
  Sec
  Hello
  3
  Outside loop
  


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break  # Error not using loop

	print('Sec')
