'''
1) #Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)  # a :  10
	print('b : ' , b)  # b :  20
	print('c : ' , c)  # c :  30
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)  # a :  11
	print('b : ' , b)  # b :  40
	print('c : ' , c)  # c :  31
# End  of  f2()  function
c = 30
print('a : ' , a)  # a :  50
print('b : ' , b)  # b :  22
print('c : ' , c)  # c :  32
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye')  # Bye
'''
'''
2) # Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)  # 10
	a += 1
#End  of  the  function
a = 10
print(a)  # 20
a += 1
f1()
print(a)  # 11
'''
'''
3) # Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)  # 10
	dict = globals()
	print(dict['a'])  # 20
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)  # 11
a += 1
f1()
print(a)  # 40
'''
'''
4) # Find  outputs (Home  work)
x = 10
def   f1():
	print(x)  # 10
	print(globals()['x'])  # 10
# end of the function
f1()
'''
'''
5) # Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)  # 20
	print(globals()['x'])  # Error
# End  of  the  function
f1()
'''
'''
6) # Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)  # 40 50 60
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])  # 10 20 30
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)  # 100 200 300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()
'''
'''
7) # global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)  # 10
def   f2():
	global  x
	x = 30
	print(x)  # 20
	x += 1
def   f3():
	global  y
	y = 40
	print(y)  # 11
	y += 1
def   f4():
	x = 50
	global   x  # 30
#  End  of  the  functions
x = 10
print(x)  # 31
x += 1
f1()
print(x)  # 32
f2()
print(x)  # 40
x += 1
f3()
print(y)  # 41
f4()
print(x)  # 50
'''
'''
8) # Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)  # 10
	a = 20
def  f2():
	global  a
	print(a)  # 20
	a = 30
def  f3():
	print(a)  # 30
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)  # 40
'''
'''
9) # Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a) # 10
	a = 20
def  f2():
	print(a)
	a = 30
	print(a)
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)
'''
'''
10) #  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()
print(a)  # Error because a is assigned to global
print(b)
'''
'''
11) # Find outputs (Home  work)
def  f1():
        global  a
        print(a)  # 10
        a += 1
def  f2():
        global  a
        print(a)  # 11
        a += 1
# End  of  the  function
a = 10
print(a)  # 12
a += 1
f1()
print(a)  # 13
a += 1
f2()
print(a)  # 14
'''
'''
12) # Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)  # 10
def  f2():
	print(a)  # 20
	a += 1
# End of the function
a = 10
print(a)  #  Error
f1()
a += 1
f2()
print(a)  #  Error
'''
'''
13) # Find outputs (Home  work)
def  f1():
	a = 20
	global   a
	print(a)  #  10
	print(globals()['a'])  #  11
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)  # 11
a += 1
f1()
print(a)  # 40
'''
'''
14) #  Find   outputs
def   f1():
	x = x + 5
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)  # 1
# End of f2  function
x = 10
f1()
f2()
print(x)  # Error