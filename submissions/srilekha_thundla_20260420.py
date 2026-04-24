# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
# import   time
# a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
# b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
# z1 = zip(a , b)
# print(type(z1))
# print(z1)
# # How  to  iterate  zip  object  in  differenet  ways  (Home  work)
# import   time
# a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
# b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
# z1 = zip(a , b)
# print(type(z1))
# print(z1)
# print('Iterate  thru  zip  object  with   next()   function')
# How  to   iterate  thru  zip  object  with  next()  function
# print('Iterate  thru  zip  object  with  __next__()  method')
# How  to   iterate  thru  zip  object  with  __next__()  method
# print('Iterate  thru  zip  object  with   for  loop')
# How  to   iterate  thru  zip  object  with  for  loop
# print('Elements  of  each  tuple  in  zip  object')
# How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
# print('Unpacks  zip  object  with   *  operator  :  ' , ???)
# print()
# print('zip   object  in  the  form  of   list  :  ' ,  ???)
# print()
# print('zip   object  in  the  form  of   dictionary :  ' ,  ???)
# How  to   iterate  thru  zip  object  with  next()  function
# print('Iterate  thru  zip  object  with  __next__()  method')
# How  to   iterate  thru  zip  object  with  __next__()  method
# print('Iterate  thru  zip  object  with   for  loop')
# How  to   iterate  thru  zip  object  with  for  loop
# print('Elements  of  each  tuple  in  zip  object')
# How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
# print('Unpacks  zip  object  with   *  operator  :  ' , ???)
# print()
# print('zip   object  in  the  form  of   list  :  ' ,  ???)
# print()
# print('zip   object  in  the  form  of   dictionary :  ' ,  ???)


#  Find  outputs  (Home  work)
# import   time
# a = [ 'Empno' , 'Emp Name' , 'Salary']
# b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
# z = zip(a , b)
# while   True:
# 	try:
# 		print(next(z))
# 		time . sleep(1)
# 	except  StopIteration:
# 		break
# #op
# # ('Empno', 25)
# # ('Emp Name', 'Rama  Rao')
# # ('Salary', 10000.0)


#  Find  outputs  (Home  work)
# import   time
# a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
# b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
# c = [50000000   , 70000000 , 60000000 , 30000000]
# for   x   in   zip(a , b , c):
# 	print(x)
# 	time . sleep(1)
	
#op
# ('Telangana','Hyderabad',50000000)
# ('Andhra  Pradesh','Amaravathi',70000000)
# ('Karnataka''Banglore',60000000)
# ('TamilNadu','Chennai',30000000)

# Find  outputs   (Home  work)
# import   time
# a = [1 , 2 , 3]
# b = [4 , 5 , 6 , 7 , 8]
# for  x , y  in   zip(a , b):
# 	print(x + y)  
# 	time . sleep(1)
#op
#5
#7
#9

# Find outputs  (Home  work)
# import   time
# def   disp(z):
# 	while   True:
# 		try:
# 			print(next(z))
# 			time . sleep(1)
# 		except:
# 			break
# 	print()
# a = [10 , 20 ,  30]
# b = {1 : 2 , 3 : 4 , 5 : 6}
# z1 = zip(a , b . keys())
# disp(z1)
# #(10,1)
# #(20,3)
# #(30,5)
# z2 = zip(a , b . values())
# disp(z2)
# #(10,2)
# #(20,4)
# #(30,6)
# z3 = zip(a , b . items())
# disp(z3)
# #(10,(1,2))
# #(20,(3,4))
# #(30,(5,6))
# z4 = zip(a , b)
# disp(z4)
# # (10, 1)
# # (20, 3)
# # (30, 5)
# z5 = zip(a)
# disp(z5)
# #(10,)
# # (20,)
# # (30,)
# z6 = zip(b)
# disp(z6)
# #(1,)
# # (3,)
# # (5,)
# z7 = zip()
# disp(z7)
# #SI




# Find  outputs  (Home  work)
# z = zip(range(5) , range(20 , 25))
# a = [ [x , y]  for  x , y   in   z]  
# print(a)
# #[[0,20],[1,21],[2,22],[3,23],[4,24]]


#  How  to  print  reversed  object  in  different  ways  (Home  work)
# import   time
# a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
# r1 = reversed(a)
# print(type(r1))
# print(r1)
# print(next(r1))
# print(next(r1))
# print(next(r1))
# print(next(r1))
# r1 = reversed(a)
# print(r1.__next__())
# print(r1.__next__())
# print(r1.__next__())
# print(r1.__next__())
# r1 = reversed(a)
# for i in r1:
#     print(i)
    

# print('Unpack  reversed  object  : ' ,  *reversed(a))
# print('List  of  chars  in  reverse  order  :  ' ,  list(reversed(a)))
# print('Reverse  string   :   ' ,''.join(reversed(a)))

# Find  outputs (Home  work)
# a = 'HYD'
# b = reversed(a)
# print(type(b))#<class 'reversed'>
# print(b)#
# print(id(b))#address
# print(*b)#D Y H
# print(b[0])#error
# print(b[1 : 3])#error
# print(b * 2)#error
# print(len(b))#error has len()

# Can  tuple  be  reversed ?   (Home  work)
# import   time
# a = (25 , 10.8 , 'Hyd' , True)
# b = reversed(a)
# print(type(b))#<class 'reversed'>
# for  x  in   b:
# 	print(x)
# 	time . sleep(1)
# #op
# #True
# #Hyd
# #10.8
# #25

