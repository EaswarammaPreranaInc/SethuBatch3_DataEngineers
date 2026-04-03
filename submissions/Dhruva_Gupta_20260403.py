Name-Dhruva Gupta
Roll Number-D238

1)
#  Tricky  program
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))

Output-
25
25
.
.

2)
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
g = f1()
for  x  in  g:
	print(x)
for  x  in  g:
	print(x)
for  x  in  g:
	print(x)

Output-
25
10.8
Hyd

3)
# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g)) 
for  x  in   g:
	print(x)
print()
for  x  in   f1():
	print(x)
print()
gen = f1()
print(next(gen))
for  x  in   f1():
	print(x)
print(next(gen))

Output-
25
10.8
Hyd

25
10.8
Hyd

25
25
10.8
Hyd
10.8

4)
0
Hello
1
Hello
4
Hello
9
Hello
16
Hello

5)
0
1
4
9
16
0
1
4
9
16

6)
0
1
4
9
16
True

7)
Memory Error

8)
0
1
4
9
16
25
36
...