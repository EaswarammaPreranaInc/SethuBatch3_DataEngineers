a = [10 , 20 , 15 ,  18 , 12]
k = 3
Shift  right  list  'a'  for  'k'  times   --->  [15 , 18 , 12 , 10 , 20]

def rotate(list,k):
    n = len(a)
    k = k%n
    return list[k-1:] + list[:k-1]
a =eval(input("Enter list: "))
k = int(input("Enter number: "))
print(rotate(a,k))


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
#OUTPUTS:
25
10.8
(3+4j)
hyd



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
#nothing is printed


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

Output:
25
10.8
false
(3+4j)
Hyd
(25,)


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
disp(f1)#Nothing
f2 = filter(None  , list)
print('Filter  f2')
disp(f2)
#output
Filter  f1
Filter  f2
10
-25
(25,)
Hyd
10.8
[10, 20]
True



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


Rama Rao
Rajesh
Kiran
Manohar
Vamsi




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
#output
{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}


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
#Output
{'country' : 'USA' , 'sale' : 300.3}
{'country' : 'UK' , 'sale' : 210.4}
Filter  f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}


# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
print('Iterate  thru  filter  object  with   for  loop')
for x in f1:
	print(f1)
print('Unpack  filter  object :  ' ,  *f1)
print('filter  object  converted  to   list  :  ' ,  list(f1))


#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
'''
def odd(n):
	return n % 2 != 0
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
f = filter(odd,list)
while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
'''
string =  input("enter a string:")
vowels = "AEIOU"
f = filter(lambda  x  : x.upper() in vowels, string)
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


(10 , 'Rama' , 10000.0) 
(15 , 'Rajesh' , 15000.0)















