# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)#10
a += 1
f1()#20
print(a)#11
################################################################################################
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
print(a)#10
a += 1#11
f1()#20 40
print(a)#11
################################################################################################
 # Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# end of the function
f1()#10 10
################################################################################################
# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)
	print(globals()['x'])#error
# End  of  the  function
f1()#20 
################################################################################################
 # Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)#40 50 60 
	dict = globals()#{a:10 ,b:20,c:30}
	print(dict['a'] , dict['b'] , dict['c'])#10 20 30
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)#100 200 300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()
################################################################################################
 # global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)#20
def   f2():
	global  x
	x = 30
	print(x)#30
	x += 1#31
def   f3():
	global  y
	y = 40
	print(y)
	y += 1
def   f4():
	x = 50
	global   x
#  End  of  the  functions
x = 10
print(x)#10
x += 1
f1()#20
print(x)#11
f2()#30 
print(x)#31
x += 1#32
f3()#40
print(y)#41
f4()#error
print(x)32
################################################################################################
# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)#20
	print(globals()['a'])
	a = 30
# End of the function
a = 10
print(a)#10 20
f1()#20 
print(a)#30
################################################################################################
# Find  outputs(Home  work)
def  f1():
	global  a
	print(a)#error
	a = 10
	print(globals()['a'])
	a = 20
	print(a)
	a = 30
def  f2():
	print(a)
# End  of   f2   function
f1()#  10 20 
f2()#30
print(a)#30
################################################################################################
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
f1()#10
f2()#20
f3()#30 40
print(a)#40
################################################################################################
# Find outputs (Home  work)
def  f1():
	global a
	a = 10
	print(a)
	a = 20
def  f2():
	#print(a)
	a = 30
	print(a)
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()#10
f2()#error 30
f3()#20 
print(a)#40
################################################################################################
#  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()#10
print(a)#error
print(b)#20
################################################################################################
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
print(a)#10 
a += 1 #12
f1()#11
print(a)#12
a += 1#13
f2()#12
print(a)#14
################################################################################################
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
def  f2():
	print(a)
	a += 1
# End of the function
a = 10
print(a)#10
f1()#20
a += 1#11
f2()#error
print(a)#11
################################################################################################
 # Find outputs (Home  work)
def  f1():
	a = 20
	global   a
	print(a)
	print(globals()['a'])#error
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)#10
a += 1#11
f1()#20 10 
print(a)#
################################################################################################
 #  Find   outputs
def   f1():
	x = x + 5
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
f1()#error
f2()#15
print(x)#10