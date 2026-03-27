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
print(a)
a += 1
f1()
print(a)

''' Output:
10
20
11
40
'''

# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# end of the function
f1()

''' Output:
10
10
'''
# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)
	print(globals()['x']) # Error because x is not there in the globals() dictionary
# End  of  the  function
f1()

''' Output:
20
Error because x is not there in the globals() dictionary
'''
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
f1()
f2()

''' Output:
40 50 60
10 20 30
100 200 300
'''

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
def   f4():
	x = 50
	global   x # Error because cannot change locaal variable to global
#  End  of  the  functions
x = 10
print(x)
x += 1
f1()
print(x)
f2()
print(x)
x += 1
f3()
print(y)
f4()
print(x)

''' Output:
10
20
11
30
31
40
41
Error because cannot change locaal variable to global
32
'''

# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
# End of the function
a = 10
print(a)
f1()
print(a)

''' Output:
10
20
20
30
'''
# Find  outputs(Home  work)
def  f1():
	global  a  
	print(a) # Error name a is not defined
	a = 10
	print(globals()['a'])
	a = 20
	print(a)
	a = 30
def  f2():
	print(a)
# End  of   f2   function
f1()
f2()
print(a)

''' Output:
10
20
30
30
'''

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
f1()
f2()
f3()
print(a)

''' Output:
10
20
30
40
'''

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
f1()
f2()
f3()
print(a)

''' Output:
10
20
30
30
40
'''

#  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a  # Error because cannot cahnge local variable a to global variable
        print(a) # 10
        global  b
        b = 20
# End  of  f1()  function
f1()
print(a) # 10
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
print(a)
a += 1
f1()
print(a)
a += 1
f2()
print(a)

''' Output:
10
11
12
13
14
'''
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
def  f2():
	print(a) 
	a += 1
# End of the function
a = 10
print(a)
f1()
a += 1
f2()
print(a)

''' Output:
10
20
11
12
'''

# Find outputs (Home  work)
def  f1():
	a = 20
	global   a  # Error cannot change local variable a to global variable
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)
a += 1
f1()
print(a)

''' Output:
10
20
20
40
'''

#  Find   outputs
def   f1():
	x = x + 5  # Error because cannot access local variable x without declaring
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x) # 15
# End of f2  function
x = 10
f1()
f2()
print(x) # 10
