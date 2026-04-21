# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   list)
while  True:
	try:
		print(next(f))#25 <nextiteration with 1 sec pause> 10.8 <nextiteration with 1 sec pause> 3 + 4j <nextiteration with 1 sec pause>  Hyd <nextiteration with 1 sec pause> False
		time . sleep(1)
	except:
		break
		
	
#  Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  list)
while  True:
	try:
		print(next(f))#Empty
		time . sleep(1)
	except:
		break
		
		
# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda  x : x , list)
while  True:
	try:
		print(next(f))#25 <nextiteration with 1 sec pause> 10.8 <nextiteration with 1 sec pause> 3 + 4j <nextiteration with 1 sec pause>  Hyd <nextiteration with 1 sec pause> (25,)
		time . sleep(1)
	except:
		break


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
print('Filter  f1')#Filter  f1
disp(f1)# 10 <nextiteration with 1 sec pause> -25 <nextiteration with 1 sec pause> (25,) <nextiteration with 1 sec pause> Hyd <nextiteration with 1 sec pause> 10.8 <nextiteration with 1 sec pause> [10 , 20] <nextiteration with 1 sec pause> True
f2 = filter(None  , list)
print('Filter  f2')#Filter  f2
disp(f2)#Empty


# Find outputs  (Home  work)
import  time
list = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , list)
while   True:
	try:
		print(next(f))#Rama Rao <nextiteration with 1 sec pause> Rajesh <nextiteration with 1 sec pause> Kiran <nextiteration with 1 sec pause> Manohar <nextiteration with 1 sec pause> Vamsi
		time . sleep(1)
	except:
		break
		
		
# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda  x : x[1]  >=  12 , list)
while   True:
	try:
		print(next(f))#('B',20) <nextiteration with 1 sec pause> ('C',20) <nextiteration with 1 sec pause> ('E',18)
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
		print(next(f))#{'Roll Num' :  10 , 'Stud Name' : 'Rama Rao' , 'Marks' : 75} <nextiteration with 1 sec pause> {'Roll Num'  :  15 , 'Stud Name' : 'Kiran' , 'Marks' : 65} <nextiteration with 1 sec pause> {'Roll Num' :  5 , 'Stud Name' : 'Rajesh' , 'Marks' : 82}
		time . sleep(1)
	except:
		break
		
		
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
print('Filter  f1')#Filter f1
disp(f1)#{'country' : 'USA' , 'sale' : 300.3} <nextiteration with 1 sec pause> {'country' : 'UK' , 'sale' : 210.4} ]
f2 = filter(lambda  x  :  x['sale']  >=  200  , list)
print('Filter  f2')#Filter f2
disp(f2)#{'country' : 'china' , 'sale' : 200.2} <nextiteration with 1 sec pause> {'country' : 'USA' , 'sale' : 300.3} <nextiteration with 1 sec pause> {'country' : 'UK' , 'sale' : 210.4}


# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
while True:
	try:
		print(next(f1))
		time.sleep(1)
	except:
		break
print('Iterate  thru  filter  object  with   for  loop')
f2 = filter(lambda  x  :  x  %  2  ==  0 , a)
for i in f2:
	print(i)
	time.sleep(1)
f3= filter(lambda  x  :  x  %  2  ==  0 , a)
print('Unpack  filter  object :  ' ,  *f3)
f4 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('filter  object  converted  to   list  :  ' ,  list(f4))


#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
import time
def odd(n):
    return n % 2 != 0
range(1, 21)
odd_iterator = filter(odd, range(1, 21))
print("Odd numbers between 1 and 20")
while True:
    try:
        print(odd_iterator.__next__())
        time.sleep(1)
    except:
        break
	

'''
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
'''
def is_vowel(char):
    vowels = 'AEIOU'
    return char in vowels
n = input("Enter Mixed case String : ").upper()
filtered_iterator = filter(is_vowel, n)
distinct_vowels = set(filtered_iterator)
print(distinct_vowels)


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
		print(next(f))#(10 , 'Rama' , 10000.0) <nextiteration with 1 sec pause> (15 , 'Rajesh' , 15000.0)
		time .  sleep(1)
	except:
		break
		
		
