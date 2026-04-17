
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

# Find  outputs  (Home  work)
# How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
# l = [10 , 20 , 15 , 18]
# for i in l:
#     print(i)

# How  to  print  each  character  of   string  'Hyd'  with  for  loop
# string = 'Hyd'
# for i in string:
#     print(i)
# How  to  print  each  element  of   range(5)  with  for  loop
# for i in range(5):
#     print(i)

# Find  outputs  (Home  work)
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
# 	print(x) 10 <next line> 30 <next line> 50
# print()
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
# 	print(x)20 <next line> 40 <next line> 60
# print()
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
# 	print(x) (10,20) <next line> (30,40) <next line> (50,60)
# print()
# for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
# 	print(x)  10 <next line> 30 <next line> 50 

# # Find outputs  (Home  work)
# a = {10 : 20 , 30 : 40 , 50 : 60}
# for  x , y  in   a . items():
# 	print(x , y , sep = '...') #(10...20)<next line>(30...40)<next line>(50...60)
# for  x ,  y  in   a:
# 	print(x , y) # error 
# for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
# 	print(x , y , sep = '...')# error


# Identify  error  (Home  work)
# for  x  in   123:
        # print(x) # for loo can't use for non-sequence objects
    
# Find  outputs  (Home  work)
# for  x   in   ():
#         print(x) # nothing will be printed
# for  x   in  []:
#         print(x) # nothing will be printed
# for  x   in   {}:
#         print(x) # nothing will be printed
# for  x   in   set():
#         print(x) # nothing will be printed
# for  x   in   '':
#         print(x) # nothing will be printed
# for  x  in  range(10 , 10):
# 	print(x) # nothing will be printed
# for  x  in   range():
# 	print(x) # error
# for  x  in   (25):
# 	print(x) # error can't iterate non- sequence objects

#  Nested  Loop  demo  program
# for  i  in  range(1 , 4):
# 	for  j  in  range(1 , 5):
# 			print(i ,  j)  #
# 	print('Hello')
# print('Bye')

# How  to  print  each  element  and  the  corresponding  index
'''
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
'''
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(i,a[i])
for i  in a:
   
    print(len(a),i)
'''   
#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

    '''
a = [25 , 10.8 , 'Hyd' , True]
a.reverse()
for i in range(len(a)):
    print(a[i])


'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''



 
# a = eval(input('Enter  1st  list  :  '))
# b = eval(input('Enter  2nd  list  :  '))
# c = []
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
# print('3rd  list : ' , c)
# How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)



# Identify Error  (Home  work)
# if(10 , 20 , 30):
# 	print('Hyd')
# 	break #error brerak should be used in loops only
# 	print('Sec')  

# Find outputs (Home  work)
# for  i   in   range(1 , 8):
# 	print(i) # 1 2 3
# 	if   i % 3 == 0:
# 		break
# 	else:
# 		print('Sec') # Sec Sec
# 	print('Hello')  # Hello Hello 
# # End  of  the  loop
# print('Outside loop') # Outside loop

# Identify Error  (Home  work)
# if ():
# 	print('Hyd')
# 	continue #Error
# 	print('Sec')

'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''

x  =  eval(input('How many times would you like to add : '))
sum = 0
for i in range(x+1):
    sum = sum + i
print(sum)

'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + (2 * 1 - 1) +  (2 * 2 - 1) + (2 * 3 - 1) + ...  (2 * 20 - 1)

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

x  =  eval(input('sum of given odd numbers: '))
sum = 0
for i in range(1,x+1,2):
    sum = sum + i
print(sum)

'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? --->  2 * i   where 'i'  varies  from   1  to  20

3) Use  for  loop
'''

x  =  eval(input('sum of given even numbers: '))
sum = 0
for i in range(2,x+1,2):
    sum = sum + i
print(sum)

'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''
x  =  eval(input('sum of given float numbers: '))
sum = 0
for i in range(x+1):
    sum = sum  + 1.1*i
print(sum)

'''
Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  10  downto  1  in  steps  of  -1

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
z = eval(input('enter a number : '))


while z>=1:
    print(z)
    z -=1

'''
Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'

What  is  printed  in  general ?  --->  'i'  where  'i'  varies  from  1  to  n

1) Hint:  Do  not  use  range  object

2) Use  while  loop
'''
x = eval(input('enter a number : '))
print('Natural Numbers')
natural_num = 1
while x>=natural_num:
    print(natural_num)
    natural_num +=1

'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->  1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->  2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
x = eval(input("enter a number : "))
i = 1
while i<= x:
    print(2 * i  - 1)
    i+=1

#  Tricky  program
#  Find  outputs  (Home  work)
# a = [10 , 20 , 15 , 18]
# for  i  in  range(len(a)):
# 	a[i] +=  1 
# print('a :  ' , a) #a : [11,21,16,19]
# b = [10 , 20 , 15 , 18]
# for  x  in   b:
# 	x += 1
# print('b :  ' ,  b)#b : [11,21,16,19]