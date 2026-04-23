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
print(type(z1)) # <class 'zip'>
disp(z1) # returns (0,10) (1,20) (2,30) (3,40) 
z2 = zip_longest(range(7) , list)
print(type(z2)) # <class 'zip_longest'>
disp(z2) # returns (0, 10)  (1, 20) (2, 30) (3, 40) (4, None) (5, None) (6, None)
--------------------------------------------------------------
#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c)) # <class 'itertools.cycle'>
while   True:
	print(next(c)) # 10 20 30 40 10 20 30 ......
	time . sleep(1)
-------------------------------------------------------------
#  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object') # 1st  repeat  object
while   True:
	try:
		print(next(r)) # 25 25 25
		time . sleep(1)
	except:
		break
print('2nd  repeat  object') # 2nd  repeat  object
r  =  repeat('Hyd')
while   True:
	print(next(r)) # Hyd Hyd .....
	time . sleep(1)
-------------------------------------------------------------
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
-------------------------------------------------------------
# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))
while   True:
	try:
		print(next(m)) # 0 1 4 9 16 25 36 49 64 81
		time . sleep(1)
	except:
		break
        
        
# range(10) --> 0 1 2 3 4 5 6 7 8 9
# range(2 , 3) ---> 2


        
-------------------------------------------------------------
        
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
        
# range(10) --> 0 1 2 3 4 5 6 7 8 9
# range(2) ---> 0 1
   
-------------------------------------------------------------
            
        
# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , repeat(2) ,  range(10))
while   True:
	try:
		print(next(m)) # 1 2 4 8 16 25 ...512
		time . sleep(1)
	except:
		break


# repeat(2) --- 2 2 2 2 ...
# range(10) ---- 0 1 2 3 4 5 6 7 8 9
        
-------------------------------------------------------------      
        
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
list = ['A' , 'B' , 'C' , 'D'] # Different  Combinations
c = combinations(list , 3)
print('Different  Combinations')
disp(c)
print('Different   Permutations')
p = permutations(list , 3)
disp(p)




'''
c returns --- > ('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'D')
('B', 'C', 'D')


p returns ----> ('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'B')
('A', 'C', 'D')
('A', 'D', 'B')
('A', 'D', 'C')
('B', 'A', 'C')
('B', 'A', 'D')
('B', 'C', 'A')
('B', 'C', 'D')
('B', 'D', 'A')
('B', 'D', 'C')....'''

