'''Find  outputs (Home  work)'''
# a = 10
# def   f1():
# 	b = 40
# 	print('a : ' , a)# a:10
# 	print('b : ' , b)# b:40
# 	print('c : ' , c)# c:30
# 	print()
# # End  of  f1()  function
# b = 20
# def    f2():
# 	a = 50
# 	print('a : ' , a)#a:11
# 	print('b : ' , b)#b:40
# 	print('c : ' , c)#c:31
# # End  of  f2()  function
# c = 30
# print('a : ' , a)#a:50
# print('b : ' , b)#b:22
# print('c : ' , c)#c:32
# print()
# a +=  1
# b +=  1
# c +=  1
# f1()
# a +=  1
# b +=  1
# c +=  1
# f2()
# print('Bye')#Bye
''' Find  outputs (Home  work)'''
# def   f1():
# 	a = 20
# 	print(a)
# 	a += 1
# #End  of  the  function
# a = 10
# print(a)
# a += 1
# f1()
# print(a)
'''outpt'''
# 10
# 20
# 11
''' Find  outputs  (Home  work)'''
# def   f1():
# 	a = 20
# 	print(a)
# 	dict = globals()
# 	print(dict['a'])
# 	a = 30
# 	dict['a'] = 40
# #  End  of  f1()  function
# a = 10
# print(a)
# a += 1
# f1()
# print(a)
'''output'''
# 10
# 20
# 11
# 40
'''# Find  outputs (Home  work)'''
# x = 10
# def   f1():
# 	print(x)
# 	print(globals()['x'])
# # end of the function
# f1()
'''outpt'''
# 10
# 10
''' Find  outputs (Home  work)'''
# def  f1():
# 	x = 20
# 	print(x)#20
# 	print(globals()['x'])#Error
# # End  of  the  function
# f1()
'''Find outputs (Home work)'''
# def  f1():
# 	a = 40
# 	b = 50
# 	c = 60
# 	print(a , b , c)
# 	dict = globals()
# 	print(dict['a'] , dict['b'] , dict['c'])
# 	dict['a'] = 100
# 	dict['b'] = 200
# 	dict['c'] = 300
# def  f2():
# 	print(a , b , c)
# # End  of  f2  function
# a = 10
# b = 20
# c = 30
# f1()
# f2()
'''output'''
# 40 50 60
# 10 20 30
# 100 200 300
'''global  keyword  demo  program (Home  work)'''
# def    f1():
# 	x = 20
# 	print(x)
# def   f2():
# 	global  x
# 	x = 30
# 	print(x)
# 	x += 1
# def   f3():
# 	global  y
# 	y = 40
# 	print(y)
# 	y += 1
# def   f4():
#	x = 50
#	global x #Error---already local variable is created
#  End  of  the  functions
# x = 10
# print(x)
# x += 1
# f1()
# print(x)
# f2()
# print(x)
# x += 1
# f3()
# print(y)
# f4()
# print(x)
'''output'''
# 10
# 20
# 11
# 30
# 31
# 40
# 41
# 32
'''Find outputs (Home  work)'''
# def  f1():
# 	global  a
# 	a = 20
# 	print(a)
# 	print(globals()['a'])
# 	a = 30
# # End of the function
# a = 10
# print(a)
# f1()
# print(a)
'''output'''
# 10
# 20
# 20
# 30
'''Find  outputs(Home  work)'''
# def  f1():
# 	global  a
# 	a = 10#error--value of a not given
# 	print(globals()['a'])#10
# 	a = 20
# 	print(a)#20
# 	a = 30
# def  f2():
# 	print(a)#30
# # End  of   f2   function
# f1()
# f2()
# print(a)#30
'''Find outputs (Home  work)'''
# def  f1():
# 	global   a
# 	a = 10
# 	print(a) #10
# 	a = 20
# def  f2():
# 	global  a
# 	print(a)  #20
# 	a = 30
# def  f3():
# 	print(a)  #30
# 	globals()['a'] = 40
# # End  of  the  function
# f1()
# f2()
# f3()
# print(a)  #40
'''Find outputs (Home  work)'''
# def  f1():
# 	global   a
# 	a = 10
# 	print(a)  #10
# 	a = 20
# def  f2():
# 	print(a)  #20
# 	a = 30
# 	print(a)  #30
# def  f3():
# 	print(a)  #30
# 	globals()['a'] = 40
# # End  of  the  function
# f1()
# f2()
# f3()
# print(a)  #40
'''Find  outputs (Home  work)'''
# def  f1():
#         a = 10
#         global a  #Error--it is defined after local is created
#         print(a)#10
#         global  b
#         b = 20
# # End  of  f1()  function
# f1()
# print(a)#10
# print(b)#20
''' Find outputs (Home  work)'''
# def  f1():
#         global  a
#         print(a)
#         a += 1
# def  f2():
#         global  a
#         print(a)
#         a += 1
# # End  of  the  function
# a = 10
# print(a)
# a += 1
# f1()
# print(a)
# a += 1
# f2()
# print(a)
'''output'''
# 10
# 11
# 12
# 13
# 14
'''Find  outputs (Home  work)'''
# def   f1():
# 	a = 20
# 	print(a)
# def  f2():
# 	print(a)
# 	a += 1
# # End of the function
# a = 10
# print(a)
# f1()
# a += 1
# f2()
# print(a)
'''output'''
# 10
# 20
# 21
# 22
''' Find outputs (Home  work)'''
#def  f1():
# 	a = 20
# 	#global   a #Error
# 	print(a)
# 	print(globals()['a'])
# 	a = 30
# 	globals()['a'] = 40
# #  End  of  f1()   function
# a = 10
# print(a)
# a += 1
# f1()
# print(a)
'''output'''
# 10
# 20
# 11
# 40
'''Find   outputs'''
# def   f1():
# 	x = x + 5  
# # End  of  f1  function
# def  f2():
# 	x = globals()['x'] + 5 
# 	print(x)
# # End of f2  function
# x = 10
# f1()
# f2()
# print(x)
'''output'''
# 15
# 20
# 20
# 20

















