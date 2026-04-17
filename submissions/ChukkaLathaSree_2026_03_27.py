#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a) # 10 , 10
	print('b : ' , b) # 40 , 40
	print('c : ' , c) # error no L.V
	print() #Error
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a) # 50 , 50
	print('b : ' , b)# 20 , 20
	print('c : ' , c) # Error
# End  of  f2()  function
c = 30
print('a : ' , a)# 10 , 10
print('b : ' , b)# 20 , 20
print('c : ' , c) # 30 ,30
print()
a +=  1 
b +=  1
c +=  1
f1() # 10,10
       40 , 40
       
a +=  1
b +=  1
c +=  1
f2() #50,50
      20 , 20
print('Bye') # Bye
_______________________________________________________________________________

# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a) # 20
	a += 1
#End  of  the  function
a = 10
print(a) # 20
a += 1
f1() 
print(a)# 20
_________________________________________________________________________________

# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a) # 20
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a) # 20
a += 1
f1() # 20
       {30:40}
print(a) # 30
____________________________________________________________________________________


# Find  outputs (Home  work)
x = 10
def   f1():
	print(x) # 10
	print(globals()['x'])
# end of the function
f1() #10
_________________________________________________________________________________________

# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x) # 20
	print(globals()['x'])
# End  of  the  function
f1() # 20
________________________________________________________________________________________________

# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c) # 40 , 50 , 60
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
f1() # 40 ,50 ,60
       {40:100 , 50:200 ,60:300}
f2() #error
___________________________________________________________________________________________

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
print(x) # 10
x += 1
f1() 
print(x)# 20
f2()
print(x) #30
x += 1
f3()
print(y) #40
f4()
print(x) #50
_________________________________________________________________________________

# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
# End of the function
a = 10
print(a) #10
f1() 
print(a)#30
__________________________________________________________________________________________________

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
f1() #10
     #20
     #30
f2() #30
print(a) #30

___________________________________________________________________________________


# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a) # 10
	a = 20
def  f2():
	global  a 
	print(a) #20
	a = 30
def  f3():
	print(a) # 30
	globals()['a'] = 40 # {30:40}
# End  of  the  function
f1()# 10
f2()#20
f3()#30
print(a) # 30

_____________________________________________________________________________________

# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a) # 10
	a = 20
def  f2():
	print(a) # 20
	a = 30
	print(a) # 30
def  f3():
	print(a) #30
	globals()['a'] = 40 #{30:40}
# End  of  the  function
f1() # 10
f2() # 20
f3() # 30
print(a) # 30
________________________________________________________________________________________________

#  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1() # 10
print(a) #10
print(b)# 20

________________________________________________________________________________________________

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
f1() # 10
print(a) #10
a += 1
f2() #10
print(a) #10
_______________________________________________________________________________________________

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
f1() # 20
a += 1
f2() #21
print(a) #21
______________________________________________________________________________________________________


# Find outputs (Home  work)
def  f1():
	a = 20
	global   a
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40 #{30:40}
#  End  of  f1()   function
a = 10
print(a) 10
a += 1
f1() #20
print(a)  # 30 
_______________________________________________________________________________________________________

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
f2() # 20
print(x) # 20



