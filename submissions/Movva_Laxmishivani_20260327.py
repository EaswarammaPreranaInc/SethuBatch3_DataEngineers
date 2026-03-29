#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a) # a:11
	print('b : ' , b) #  b:40
	print('c : ' , c) # c:31
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a) # a : 50
	print('b : ' , b) # b : 22
	print('c : ' , c) # c : 32
# End  of  f2()  function
c = 30
print('a : ' , a) # a : 10
print('b : ' , b) # b : 20
print('c : ' , c) # c : 30
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye') # Bye

# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a) #20
	a += 1
#End  of  the  function
a = 10
print(a) # 10
a += 1
f1()
print(a) # 11

# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a) # 20
	dict = globals()
	print(dict['a']) # 11
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a) #10
a += 1
f1()
print(a) # 40

# Find  outputs (Home  work)
x = 10
def   f1():
	print(x) # 10
	print(globals()['x']) # 10
# end of the function
f1()

# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x) # 20
	print(globals()['x']) # Error 
# End  of  the  function
f1()

# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c) # 40 50 60
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c']) # 10 20 30
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c) # 100 200 300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()

# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x) # 20
def   f2():
	global  x
	x = 30
	print(x) # 30
	x += 1
def   f3():
	global  y
	y = 40
	print(y) # 40
	y += 1
def   f4():
	x = 50
	global   x # Error because x is not defined after global x.
#  End  of  the  functions
x = 10
print(x) # 10
x += 1
f1()
print(x) # 11
f2()
print(x) # 31
x += 1
f3()
print(y) # 41
f4() # Error
print(x) # Not executed

# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a) # 20
	print(globals()['a']) # 20
	a = 30
# End of the function
a = 10
print(a) # 10
f1()
print(a) # 30

# Find  outputs(Home  work)
def  f1():
	global  a
	print(a) # Error
	a = 10
	print(globals()['a']) # Not executed
	a = 20
	print(a) # Not executed
	a = 30
def  f2():
	print(a) # Not executed
# End  of   f2   function
f1()
f2()
print(a)

# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a) # 20
	a = 20
def  f2():
	global  a
	print(a) # 30
	a = 30
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a) # 40

# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a) #10
	a = 20
def  f2():
	print(a) # Error
	a = 30
	print(a) # Error
def  f3():
	print(a) # Error
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)

#  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a # Error because a is assigned to another global declaration
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()
print(a)
print(b)

# Find outputs (Home  work)
def  f1():
        global  a
        print(a) # 11
        a += 1
def  f2():
        global  a
        print(a) #13
        a += 1
# End  of  the  function
a = 10
print(a) # 10
a += 1
f1()
print(a) # 12
a += 1
f2()
print(a) # 14

# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a) # 20
def  f2():
	print(a) #Error
	a += 1
# End of the function
a = 10
print(a) # 10
f1()
a += 1
f2()
print(a) # Not executed
