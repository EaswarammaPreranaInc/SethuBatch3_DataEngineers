#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
	print()#<nextline>
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
# End  of  f2()  function
c = 30
print('a : ' , a)#10
print('b : ' , b)#20
print('c : ' , c)#30
print()#<nextline>
a +=  1
b +=  1
c +=  1
f1()#a : 11 <nextline> b : 40 <nextline> c : 31 
a +=  1
b +=  1
c +=  1
f2()#a : 50 <nextline> b : 22 <nextline> c :32
print('Bye')#Bye



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
a += 1
f1()#20 <nextline> 11 <nextline> 
print(a)40


# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# end of the function
f1()#10 <nextline> 10


# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)
	print(globals()['x'])
# End  of  the  function
f1()#20 <nextline> error


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
f1()#40 50 60 <nextline> 10 20 30 
f2()#100 200 300


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
	global   x
#  End  of  the  functions
x = 10
print(x)10
x += 1
f1()#20
print(x)#11
f2()#30
print(x)#31
x += 1
f3()#40
print(y)#41
f4()#error
print(x)#32


# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
# End of the function
a = 10
print(a)#10
f1()#20 <nextline> 20
print(a)#30


# Find  outputs(Home  work)
def  f1():
	global  a
	print(a)
	a = 10
	print(globals()['a'])
	a = 20
	print(a)
	a = 30
def  f2():
	print(a)
# End  of   f2   function
f1()#error due to print(a) before name a is defined if we that commented that print(a) line in f1 starting then 10 <nextline> 20
f2()#30
print(a)#30


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
f3()#30
print(a)#40


# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	print(a)#comment to get code run
	a = 30
	print(a)
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()#10
f2()#error a is local variable w.r.t f2() as it not assigned to a variable so error for print(a) i nf2 if we commented that print(a) statement then 30  
f3()#20
print(a)#40


#  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()#error a is assigned to before global declaration
print(a)#error due to f1() error 
print(b)#20


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
a += 1
f1()#11
print(a)#12
a += 1
f2()#13
print(a)#14


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
a += 1
f2()#error ( cannot access local variable 'a' where it is not associated with a value)
print(a)#11


# Find outputs (Home  work)
def  f1():
	a = 20
	global   a#comment
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)#10
a += 1
f1()#error and if global a commented then 20 <nextline> 11
print(a)#40


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
