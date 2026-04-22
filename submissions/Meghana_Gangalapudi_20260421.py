
import   time
s=input("enter string").upper()
v="AEIOU"
se=set()
f2=filter(lambda x:x in v,s)
for i in f2:
	se.add(i)
print(se)

r=range(1,21)
f1=filter(lambda x:not(x%2==0),r)
for i in f1:
	print(i)
	time.sleep(1)
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
while   True:
	try:
		print(next(f1))
		time . sleep(1)
	except:
		break
f2=filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   for  loop')
for i in f2:
	print(i)
f3=filter(lambda  x  :  x  %  2  ==  0 , a)
print('Unpack  filter  object :  ' ,*f3)
f4=filter(lambda  x  :  x  %  2  ==  0 , a)
print('filter  object  converted  to   list  :  ' ,list(f4))








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
{'country' : 'USA' , 'sale' : 300.3}
{'country' : 'UK' , 'sale' : 210.4}
{'country' : 'china' , 'sale' : 200.2}
{'country' : 'USA' , 'sale' : 300.3}
{'country' : 'UK' , 'sale' : 210.4}
'''






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
25 10.8 3+4j hyd False
'''





list = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
"""
empty
"""





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
25 10.8 False 3+4j  Hyd (25,)
'''





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
disp(f1) # empty
f2 = filter(None  , list)
print('Filter  f2')
disp(f2)

"""
Filter1
Filter2
10 -25 (25,) Hyd 10.8 [10,20] True
"""


