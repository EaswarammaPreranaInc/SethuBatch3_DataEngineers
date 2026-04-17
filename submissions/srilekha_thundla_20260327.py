#Find  outputs (Home  work)
# a = 10
# def   f1():
# 	b = 40
# 	print('a : ' , a)
# 	print('b : ' , b)
# 	print('c : ' , c)
# 	print()
# # End  of  f1()  function
# b = 20
# def    f2():
# 	a = 50
# 	print('a : ' , a)
# 	print('b : ' , b)
# 	print('c : ' , c)
# # End  of  f2()  function
# c = 30
# print('a : ' , a)#1.   a : 10
# print('b : ' , b)#2.   b : 20
# print('c : ' , c)#3.   c : 30
# print()#4. <space>
# a +=  1
# b +=  1
# c +=  1
# f1()
# a +=  1
# b +=  1
# c +=  1
# f2()
# print('Bye')
#5. a : 11
#6. b : 40
#7. c : 31

#5. a : 50
#6. b : 22
#7. c : 32
#8. Bye

# Find  outputs (Home  work)
# def   f1():
# 	a = 20
# 	print(a)
# 	a += 1
# #End  of  the  function
# a = 10
# print(a)#10
# a += 1
# f1() #20
# print(a)#11

# Find  outputs  (Home  work)
# def   f1():
# 	a = 20
# 	print(a)
# 	dict = globals()
# 	print(dict['a'])
# 	a = 30
# 	dict['a'] = 40
# #  End  of  f1()  function
# a = 10
# print(a)#10
# a += 1
# f1()#20
# #11
# #40
# print(a)

# Find  outputs (Home  work)
# x = 10
# def   f1():
# 	print(x)#10
# 	print(globals()['x'])#10
# # end of the function
# f1()

# Find  outputs (Home  work)

# Find  outputs (Home  work)
# def  f1():
# 	x = 20
# 	print(x)#20
# 	print(globals()['x'])#error because there is no blobal variable x
# # End  of  the  function
# f1()

# Find outputs (Home  work)
# def  f1():
# 	a = 40
# 	b = 50
# 	c = 60
# 	print(a , b , c) # 40 50 60
# 	dict = globals()
# 	print(dict['a'] , dict['b'] , dict['c'])
# 	dict['a'] = 100
# 	dict['b'] = 200
# 	dict['c'] = 300
# def  f2():
# 	print(a , b , c) # 10 20 30
# # End  of  f2  function
# a = 10
# b = 20
# c = 30
# f1()
# f2()
# # 100 200 300

# global  keyword  demo  program (Home  work)
# def    f1():
# 	x = 20
# 	print(x)#2. 20
# def   f2():
# 	global  x
# 	x = 30
# 	print(x)#4. 30
# 	x += 1
# def   f3():
# 	global  y
# 	y = 40
	# print(y)#6. 40
	# y += 1
# def   f4():
# 	x = 50 
# 	global   x
#  End  of  the  functions
# x = 10
# print(x)#1. 10
# x += 1
# f1()
# print(x)#3. 11
# f2()
# print(x)#5. 31
# x += 1
# f3()
# print(y)#7. 41
# f4()#error
# print(x)#last 32

# Find outputs (Home  work)
# def  f1():
# 	global  a
# 	a = 20
# 	print(a)#2. 20
# 	print(globals()['a'])#3. 20
# 	a = 30
# # End of the function
# a = 10
# print(a)#1. 10
# f1()
# print(a)#4. 30

# Find  outputs(Home  work)

# def  f1():
# 	global  a
# 	# print(a)#1.error
# 	a = 10
# 	print(globals()['a'])#2. 10
# 	a = 20
# 	print(a)#3. 20
# 	a = 30
# def  f2():
# 	print(a)#4. 30
# # End  of   f2   function
# f1()
# f2()
# print(a)#5. 30

# Find outputs (Home  work)
# def  f1():
# 	global   a
# 	a = 10
# 	print(a)#1.  10
# 	a = 20
# def  f2():
# 	global  a
# 	print(a)#2.  20
# 	a = 30
# def  f3():
# 	print(a)#3. 30
# 	globals()['a'] = 40
# # End  of  the  function
# f1()
# f2()
# f3()
# print(a)#4. 40


#  Find  outputs (Home  work)
# def  f1():
#         a = 10
#         global  a
#         print(a)#2. 10
#         global  b
#         b = 20
# # End  of  f1()  function
# f1()
# print(a)#error
# print(b)#3. 20

# Find outputs (Home  work)
# def  f1():
#         global  a
#         print(a)#2. 11
#         a += 1
# def  f2():
#         global  a
#         print(a)#4. 13
#         a += 1
# # End  of  the  function
# a = 10
# print(a)#1. 10
# a += 1
# f1()
# print(a)#3. 12
# a += 1
# f2()
# print(a)#5. 14

# Find  outputs (Home  work)
# def   f1():
# 	a = 20
# 	print(a)#2. 20
# def  f2():
# 	print(a)#3. error
# 	a += 1
# End of the function
# a = 10
# print(a)#1. 10
# f1()
# a += 1
# f2()
# print(a)#4. 11

# Find outputs (Home  work)
# def  f1():
# 	a = 20
# 	# global   a
# 	print(a)#2. 20
# 	print(globals()['a'])#3. 11
# 	a = 30
# 	globals()['a'] 
# #  End  of  f1()   function
# a = 10
# print(a)#1. 10
# a += 1
# f1()
# print(a)#4. 11