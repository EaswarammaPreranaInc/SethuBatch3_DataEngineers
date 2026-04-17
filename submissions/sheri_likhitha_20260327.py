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
print('a : ' , a)	#a : 10
print('b : ' , b)	#b : 20
print('c : ' , c)	#c : 30
print()
a +=  1		#a : 11
b +=  1		#b : 40
c +=  1		#c : 31
f1()
a +=  1		#a :  50
b +=  1		#b :  22
c +=  1		#c :  32
f2()
print('Bye')	#Bye




# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)	#10
a += 1
f1()		#20
print(a)	#11





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
print(a)	#10
a += 1		#20
f1()		#11
print(a)	#40




# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# end of the function
f1()	#10 <next line> 10



# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)
	print(globals()['x'])	#error because there is no global variable
# End  of  the  function
f1()





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
c = 30		#40 50 60
f1()		#10 20 30
f2()		#100 200 300






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
	global   x	#error because x is not defined as local variable
#  End  of  the  functions
x = 10
print(x)
x += 1
f1()
print(x)	#10 <next line> 20
f2()
print(x)	#11 <next line> 30
x += 1
f3()		#31 <next line> 40
print(y)
f4()		#41 <next line> 32
print(x)







# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
# End of the function
a = 10
print(a)	#10
f1()
print(a)	#20 20 30



# Find  outputs(Home  work)
def  f1():
	global  a
	print(a)	#error a is not defined
	a = 10
	print(globals()['a'])
	a = 20
	print(a)
	a = 30
def  f2():
	print(a)	# a is not defined
# End  of   f2   function
f1()	#error
f2()	#error
print(a)






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
f1()	#10 <next line> 20
f2()	#30
f3()	#40
print(a)





# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	print(a)	#error a is not defined
	a = 30
	print(a)
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()	#10
f2()	#30
f3()	#20
print(a) #40
	






#  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a	#error 'a' is assigned to before global declaration
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()	#10
print(a) #error a is not defined
print(b)	#20





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
f1()	#10
print(a) #11
a += 1	#12
f2()	#13
print(a) #14





# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
def  f2():
	print(a)	#error a is not defined
	a += 1
# End of the function
a = 10
print(a)
f1()
a += 1	#10
f2()	#20
print(a) #11





# Find outputs (Home  work)
def  f1():
	a = 20
	global   a	#error 'a' is assigned to before global declaration
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a) #11
a += 1	#40
f1()	#10
print(a) #20



#  Find   outputs
def   f1():
	x = x + 5	#error cannot access local variable 'x' where it is not associated with a value
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
f1()
f2()	#15
print(x) #20