Name-Dhruva Gupta
Roll No-D238

1)
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
print(‘Bye')

Output-
A:10
B:20
C:30
A:11
B:40
C:31
A:50
B:22
C:32
Bye

2)
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a) #20
	a += 1
#End  of  the  function
a = 10
print(a) #10
a += 1
f1()
print(a) #11

3)
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

Output-
10
20
11
40

4)
# Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# end of the function
f1()

Output-
10
10

5)
# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)
	print(globals()[‘x']) #Error as no global variable exists
# End  of  the  function
f1()

Output-
20

6)
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

Output-
40 50 60
10 20 30 
100 200 300

7)
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
	global   x #GLOBAL MUST BE DECLARED BEFORE ASSIGNMENT
#  End  of  the  functions
x = 10
print(x)
x += 1
f1()
print(x)
f2()
print(x)
x += 1 #12
f3()
print(y)
f4()
print(x)

Output-
10
20
11
30
31
40
41
Error

8)
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

Output-
10
20
20
30

9)
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
f1()
f2()
print(a)

Output-
Error as a not defined

10)
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

Output-
10
20
30
40

11)
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

Output-
10
20
30
30
40

12)
#  Find  outputs (Home  work)
def  f1():
        a = 10
        global  a
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()
print(a)
print(b)

Output-
Error

13)
# Find outputs (Home  work)
def  f1():
        global  a
        print(a)
        a += 1 #12
def  f2():
        global  a
        print(a) 
        a += 1 
# End  of  the  function
a = 10
print(a)
a += 1 #11
f1()
print(a)
a += 1 #13
f2()
print(a)

Output-
10
11
12
13
14

14)
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
a += 1 #11
f2()
print(a)

Output-
10
20
Error

15)
# Find outputs (Home  work)
def  f1():
	a = 20
	global   a
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)
a += 1 #11
f1()
print(a)

Output-
Error

16)
#  Find   outputs
def   f1():
	x = x + 5 
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
f1()
f2()
print(x)

Output-
Error as f1 does not have any variable to perform its operation on.
