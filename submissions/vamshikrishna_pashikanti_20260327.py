#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a) 
	print('b : ' , b) 
	print('c : ' , c) 
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a) 
	print('b : ' , b) 
	print('c : ' , c) 
# End  of  f2()  function
c = 30
print('a : ' , a) # 10
print('b : ' , b) # 20
print('c : ' , c) # 30
print()
a +=  1
b +=  1
c +=  1
f1()  # 11 # 40 # 31
a +=  1
b +=  1
c +=  1
f2() # 50 # 22 # 32
print('Bye') # Bye

# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a) # 10
a += 1
f1() #  20
print(a) # 11


# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a) # 10
a += 1 # 11
f1() # 20 # 11 
print(a) # 40


# Find  outputs (Home  work)
x = 10
def   f1():
	print(x) # 10
	print(globals()['x']) # 10
# end of the function
f1() # 10, 10


# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x) 
	print(globals()['x'])
# End  of  the  function
f1() # 20, 20


# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)
# End  of  f2  function
a = 10
b = 20
c = 30
f1() # 40, 50, 60 / 10, 20, 30 
f2() # 100, 200, 300


# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)
def   f2():
	global  x
	x = 30
	print(x)
	x += 1
def   f3():
	global  y
	y = 40
	print(y)
	y += 1
# def   f4():
# 	x = 50
# 	global   x
#  End  of  the  functions
x = 10
print(x) # 10
x += 1
f1() # 20
print(x) #11
f2() # 30
print(x) # 31
x += 1 
f3() # 40
print(y) # 40
# f4() # error
# print(x)


# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
# End of the function
a = 10
print(a) # 10
f1() # 20, 20
print(a) # 30


# Find  outputs(Home  work)
def  f1():
	global  a
	#print(a)
	a = 10
	print(globals()['a'])
	a = 20
	print(a)
	a = 30
def  f2():
	print(a)
# End  of   f2   function
f1() # None, 10, 20
f2() # 30
print(a) # 30


# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	global  a
	print(a)
	a = 30
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1() # 10
f2() # 20
f3() # 30
print(a) # 40



# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	print(a)
	a = 30
	print(a)
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1() # 10
f2() # 20, 30
f3() # 30
print(a) # 40

#  Find  outputs (Home  work)
def  f1():
        a = 10
        #global  a
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1() # 10
print(a) # name error
print(b) # 20





# Find outputs (Home  work)
def  f1():
        global  a
        print(a)
        a += 1
def  f2():
        global  a
        print(a)
        a += 1
# End  of  the  function
a = 10
print(a) # 10
a += 1 # 11
f1() # 11
print(a) # 12
a += 1
f2() # 13
print(a) # 14





# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
def  f2():
	print(a)
	a += 1
# End of the function
a = 10
print(a) # 10
f1() # 20
a += 1 # 11
# f2() # 11
# print(a) # 12



# Find outputs (Home  work)
def  f1():
	a = 20
	global   a
	print(a)
	print(globals()['a']) # 11
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a) # 10
a += 1
f1() # error, 20, 11, 40
print(a) # 40


#  Find   outputs
def   f1():
	x = x + 5
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
f1() # 15
f2() # 15
print(x) # 10
