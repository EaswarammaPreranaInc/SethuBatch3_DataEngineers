#1
'''
Shift the list  'a'  for  'k'  times towards given side.
For example:
a = [10 , 20 , 15 ,  18 , 12]
k = 3
Right --->  [15 , 18 , 12 , 10 , 20]
'''
def rleft(a , k):
    print(a[k:] + a[:k])

def rright(a , k):
    print(a[-k:] + a[:-k])
    
a = eval(input('Enter the list:'))
k = int(input('Enter the times it needs to be rotated:'))
s = input('Left or Right:')

if s.lower() == 'left':
    rleft(a , k)
elif s.lower() == 'right':
    rright(a , k)
else:
    print('Enter a valid side.')



# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
25
10.8
3 + 4j
'Hyd'
'''



#  Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''

'''



# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda  x : x , list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
25
10.8
3 + 4j
'Hyd'
(25 ,)
'''



# Find outputs
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [10 , 0 ,  -25 , () , (25,) , 'Hyd', '' , [] , 10.8 , 0.0 , [10 , 20] , True , False]
f1 = filter(lambda  x : None  , list)
print('Filter  f1')
disp(f1)
f2 = filter(None  , list)
print('Filter  f2')
disp(f2)
'''
Filter  f1
Filter  f2
10
-25
(25 ,)
Hyd
10.8
[10 , 20]
True
'''



# Find outputs  (Home  work)
import  time
list = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
Rama Rao
Rajesh
Kiran
Manohar
Vamsi
'''



# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda  x : x[1]  >=  12 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
('B' , 20)
('C' , 15)
('E' , 18)
'''


# Find  outputs (Home  work)
import   time
list = [{'Roll Num' :  10 , 'Stud Name' : 'Rama Rao' , 'Marks' : 75} ,
          {'Roll Num' :  20 , 'Stud Name' : 'Sita' , 'Marks' : 52} ,
          {'Roll Num'  :  15 , 'Stud Name' : 'Kiran' , 'Marks' : 65} ,
          {'Roll Num'  :  18 , 'Stud Name' : 'Amar' ,  'Marks' : 48} ,
          {'Roll Num' :  5 , 'Stud Name' : 'Rajesh' , 'Marks' : 82}]  
f = filter(lambda  x :  x['Marks'] >= 60 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
{'Roll Num' :  10 , 'Stud Name' : 'Rama Rao' , 'Marks' : 75}
{'Roll Num'  :  15 , 'Stud Name' : 'Kiran' , 'Marks' : 65}
{'Roll Num' :  5 , 'Stud Name' : 'Rajesh' , 'Marks' : 82}
'''

# Find  outputs (Home  work)
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [{'country' : 'India' , 'sale' : 150.5} ,
          {'country' : 'china' , 'sale' : 200.2} ,
          {'country' : 'USA' , 'sale' : 300.3} ,
          {'country' : 'UK' , 'sale' : 210.4} ]
f1 = filter(lambda  x  :   x['country'] . startswith('U') , list)
print('Filter  f1')
disp(f1)
f2 = filter(lambda  x  :  x['sale']  >=  200  , list)
print('Filter  f2')
disp(f2)
'''
Filter f1
{'country' : 'USA' , 'sale' : 300.3}
{'country' : 'UK' , 'sale' : 210.4}

Filter f2
{'country' : 'china' , 'sale' : 200.2}
{'country' : 'USA' , 'sale' : 300.3}
{'country' : 'UK' , 'sale' : 210.4}
'''



# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
while True:
    try:
        print(next(f1))
        time . sleep(0.5)
    except StopIteration:
        break

f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   for  loop')
for x in f1:
    print(x)
    time . sleep(0.5)

f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Unpack  filter  object :  ' ,  *f1)

f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('filter  object  converted  to   list  :  ' ,  list(f1))



#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
import time
a = range(1 , 21)
f = filter(lambda x : x % 2 != 0 , a)

while True:
    try:
        print(next(f))
        time . sleep(0.5)
    except StopIteration:
        break


        
#2
'''
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
'''
import time
s = input('Enter Mixed Case String:')
s = s.upper()
f = filter(lambda x : x in 'AEIOU' , s)

print(set(f))
    


# Nested  filter  i.e.  filter  on  filter
import   time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda  x :  x[1] . startswith('R')  , filter(lambda  x :  x[2] >= 10000 , list))
while   True:
	try:
		print(next(f))
		time .  sleep(1)
	except:
		break
'''
(10 , 'Rama' , 10000.0)
(15 , 'Rajesh' , 15000.0)
'''
