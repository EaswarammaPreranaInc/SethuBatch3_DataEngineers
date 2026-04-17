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
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye')

a :  10
b :  20
c :  30

a :  11
b :  40
c :  31

a :  50
b :  22
c :  32
Bye




# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a) -->20
	a += 1
#End  of  the  function
a = 10
print(a) --> 10
a += 1
f1()
print(a) --> 11




# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a) --> 20
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40 --> 40
#  End  of  f1()  function
a = 10
print(a) -- > 10
a += 1
f1()
print(a) --> 11




# Find  outputs (Home  work)
x = 10
def   f1():
	print(x) --> 10
	print(globals()['x']) --> 10
# end of the function
f1() 



# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x) --> 20
	print(globals()['x']) --> there is no global variable called 'x'
# End  of  the  function
f1()



# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c) --> 40 50 60
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c']) --> 10 20 30
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
	---> 100 200 300
def  f2():
	print(a , b , c)
# End  of  f2  function
a = 10
b = 20
c = 30

f1()
f2()




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
	global   x  --> error
#  End  of  the  functions
x = 10
print(x) --> 10
x += 1
f1()
print(x) ->20
f2()--> 11
print(x) --> 30
x += 1 --> 31
f3() --> 40
print(y) --> 41
f4()
print(x) --> 32         




# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a) --> 20
	print(globals()['a']) --> 30
	a = 30
# End of the function
a = 10
print(a) --> 10
f1()
print(a) --> 20



# Find  outputs(Home  work)
def  f1():
	global  a
	print(a) --> error
	a = 10
	print(globals()['a']) --> 10
	a = 20
	print(a) --> 20
	a = 30
def  f2():
	print(a)
# End  of   f2   function
f1()
f2()
print(a) --> 30




# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a) --> 10
	a = 20
def  f2():
	global  a
	print(a) --> 20
	a = 30
def  f3():
	print(a) --> 30
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a) --> 40




#  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a --> error (a is alrady declared as local variable)
        print(a) --> 10
        global  b
        b = 20
# End  of  f1()  function
f1()
print(a) --> error
print(b) --> 20



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
print(a) --> 10
a += 1
f1() --> 11
print(a) --> 12
a += 1
f2() --> 13
print(a) --> 14


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




#  Find   outputs
def   f1():
	x = x + 5
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10 --> 10
f1() --> error
f2()
print(x) --> 15










