'''
Modify  following  porgram  such  that
1) Use  regular  function  instead  of  lambda  function
2) Use  for  loop  instead  of  while  loop
'''
# import  time
# list = [10 , 20 , 15 , 18 , 5]
# m = map(lambda  x :  x  *  x ,  list)
# print(type(m))
# print(m)
# while   True:
# 	try:
# 		print(next(m))
# 		time . sleep(1)
# 	except  StopIteration:
# 		break
# 	time . sleep(1)
# import time
# list = [10 , 20 , 15 , 18 , 5]
# def seq(x):
#     return x*x
# m = map(seq,list)
# print(m)
# for i in m:
#     print(i)
#     time.sleep(1)

# Find  outputs (Home  work)
# import  time
# a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
# m = map(lambda   x  :  x[1]  ,  a)
# while  True:
# 	try:
# 		print(next(m))#10 \n 20 \n 15 \n 5 \n 18
# 		time . sleep(1)
# 	except  StopIteration:
# 		break

# Find  outputs (Home  work)
# import   time
# def  disp(m):
# 	while   True:
# 		try:
# 			print(next(m))
# 			time . sleep(1)
# 		except  StopIteration:
# 			break
# #  End  of  the  function
# list = [ { 'country' : 'India' , 'sale' : 150.5} ,
#            { 'country' : 'China' , 'sale' : 200.2} ,
#            { 'country' : 'USA' , 'sale' : 300.3} ,
#            { 'country' : 'UK' , 'sale' : 210.4} ]
# m1 = map(lambda  x  :  x['country'] , list)
# print('Map   m1')#Map  m1
# disp(m1)#India \n China \n USA \n UK 
# m2 = map(lambda  x  :  x['sale']  , list)
# print('Map   m2')#Map m2
# disp(m2)#150.5 \n 200.2 \n 300.3 \n 210.4

'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->  1.8 * celsius-temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''

# import time
# l =eval(input("enter  list of celsius temperatures  : "))
# m = map(lambda x:1.8*x+32,l)
# print("Equivalent fahrenhiet temperatures ")
# while True:
#     try:
     
#         print(next(m))
#         time.sleep(1)
#     except StopIteration:
#         break
#     time.sleep(1)

# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   iterator (Home  work)
# import time
# from itertools import count 
# m = map(lambda x:2**x,count())
# x = 0
# while True:
#     try:
#         if x<10:
#             print(next(m))
#             x+=1
#             time.sleep(1)
#     except StopIteration:
#         break
#     time.sleep(1)

'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  3.14159 * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
'''
# l = eval(input("enter list of radii : "))
# m = map(lambda r: 3.14159*r*r,l)
# print("area of each radius in the list")
# for x in m:
#     print(x)

'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
# t1 = eval(input("enter first tuple : "))
# t2 = eval(input("enter second tuple : "))
# m = map(lambda x ,y:x+y,t1,t2 )
# t =[]
# for i in m:
#     t.append(i)
# print("Addition tupple : ",tuple(t))

'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''
# l1 = eval(input("enter first list: "))
# l2 = eval(input("enter second list : "))
# m = map(lambda x ,y:x*y,l1,l2 )
# l =[]
# for i in m:
#     l.append(i)
# print(l)

# filter  inside  map
# import  time
# a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
# m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
# while   True:
# 	try:
# 		print(next(m))#40 \n 30 \n 36 \n 50 \n 34
# 		time . sleep(1)
# 	except:
# 		break

# map  inside  filter (Home  work)
# import   time
# a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
# f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
# while   True:
# 	try:
# 		print(next(f))#100 \n 400 \n 144 \n 324 \n 196
# 		time . sleep(1)
# 	except:
# 		break

'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function
'''
# from functools import reduce

# lst = [10, 20, 15, 30, 25, 40, 35]

# largest = reduce(lambda a, b: a if a > b else b, lst)

# print("Largest element:", largest)

# from functools import reduce

# def find_max(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# lst = [10, 20, 15, 30, 25, 40, 35]

# largest = reduce(find_max, lst)

# print("Largest element:", largest)

# Find  outputs  (Home  work)
# from  functools  import  reduce
# a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
# ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
# print(ans)#1574

# Find   outputs (Home  work)
# from  itertools  import  count
# c1 = count()
# print('While  loop')#While loop
# while   True:
#         x = next(c1)# 0 --- 9
#         if   x > 9:
#                 break
#         print(x)
# print('For  loop')#For loop
# c2 = count()
# for  x  in  c2:
# 	if  x  >  20: 
# 		break
# 	print(x)#0---20
# # End  of  for  loop
# c3 = count()
# print('Element :  ' , next(c3))#Element : 0
# c4 = count()
# print(*c4) 

#  Find  outputs (Home  work)
# from  itertools  import  count
# def  disp(cnt):
#         for  i  in   range(4):
#                 print(next(cnt) , end = '\t')
#         print()
# # End  of  the  function
# a = count(start = 10)
# disp(a)#10 \t 11 \t 12 \t 13
# b = count(start = 10 , step = 5)
# disp(b)#10 \t 15 \t 20 \t 25
# c = count(start = 10 , step = -2.5)
# disp(c)#10 \t 7.5 \t 5.0 \t 2.5
# d = count()
# disp(d)#0 \t 1 \t 2 \t 3