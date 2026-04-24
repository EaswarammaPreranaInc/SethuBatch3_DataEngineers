#  Find  outputs  (Home  work)
from  itertools  import  zip_longest
import   time
def  disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
# End  of  the  function
list = [10 , 20 , 30 , 40]
z1  =  zip(range(7) , list)
print(type(z1))
disp(z1)
z2 = zip_longest(range(7) , list)
print(type(z2))
disp(z2)
'''
<class 'zip'>
(0 , 10)
(1 , 20)
(2 , 30)
(3 , 40)
<class 'zip_longest'>
(0 , 10)
(1 , 20)
(2 , 30)
(3 , 40)
(5 , None)
(6 , None)
'''


#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))
while   True:
	print(next(c))
	time . sleep(1)
'''
<class 'cycle'>
10
20
30
40
10
20
30
40
infinite cycle'''


#  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object')
while   True:
	try:
		print(next(r))
		time . sleep(1)
	except:
		break
print('2nd  repeat  object')
r  =  repeat('Hyd')
while   True:
	print(next(r))
	time . sleep(1)
'''
1st repeat object
25
25
25
2nd repeat object
Hyd
Hyd
Hyd
infinite times'''


# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
'''
0
1
4
9
16
25
36
49
64
81
0
1
4
9
16
25
36
49
64
81
'''



# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
'''
0
'''



# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
'''
0
1
'''



# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , repeat(2) ,  range(10))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break



#  Find  outputs (Home  work)
import  time
def  disp(itr):
	while  True:
		try:
			print(next(itr))
			time . sleep(1)
		except:
			break
from  itertools  import  combinations,permutations
list = ['A' , 'B' , 'C' , 'D']
c = combinations(list , 3)
print('Different  Combinations')
disp(c)
print('Different   Permutations')
p = permutations(list , 3)
disp(p)
'''
Different  Combinations
('A' , 'B' , 'C')
('A' , 'B' , 'D')
('A' , 'C' , 'D')
('B' , 'C' , 'D')
Different   Permutations
('A' , 'B' , 'C')
('A' , 'B' , 'D')
('A' , 'C' , 'B')
('A' , 'C' , 'D')
('A' , 'D' , 'B')
('A' , 'D' , 'C')
('B' , 'A' , 'C')
('B' , 'A' , 'D')
('B' , 'C' , 'A')
('B' , 'C' , 'D')
('B' , 'D' , 'A')
('B' , 'D' , 'C')
('C' , 'A' , 'B')
('C' , 'A' , 'D')
('C' , 'B' , 'A')
('C' , 'B' , 'D')
('C' , 'D' , 'A')
('C' , 'D' , 'B')
('D' , 'A' , 'B')
('D' , 'A' , 'C')
('D' , 'B' , 'A')
('D' , 'B' , 'C')
('D' , 'C' , 'A')
('D' , 'C' , 'B')
'''