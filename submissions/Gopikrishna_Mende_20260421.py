a = [10 , 20 , 15 ,  18 , 12]
k = 3
n = len(a)
 
 



def   rotate(a):  
    temp = a[n-1]  
    for i in range(n-1, 0, -1):  
        a[i] = a[i-1]  
    a[0] = temp  
    
#  End  of  the  function	

for i in range(k):  
    rotate(a)  
    print(f"After  {i+1}st  call   -->  {a}")  

# After  1st  call   -->  [12 , 10 , 20 , 15 , 18]
# After  2nd   call   -->  [18 , 12 , 10 , 20 , 15]
# After  3rd   call   -->  [15 , 18 , 12 , 10 , 20]

# ========================================================================  

# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   list)
while  True:
	try:
		print(next(f)) # 25 <next line> 10.8 <next line> (3+4j) <next line> 'Hyd' <next line> False 
		time . sleep(1)
	except:
		break

# =======================================================================

#  Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  list)
while  True:
	try:
		print(next(f)) #No output
		time . sleep(1)
	except:
		break


=======================================================================

# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda  x : x , list)
while  True:
	try:
		print(next(f)) # 25 <next line> 10.8 <next line> (3+4j) <next line> 'Hyd' <next line> (25,)
		time . sleep(1)
	except:
		break

# =======================================================================

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
print('Filter  f1') # Filtr f1
disp(f1) # No output
f2 = filter(None  , list)
print('Filter  f2')  # Filter f2
disp(f2)# 10 <next line>-25 <next line> (25,) <next line> 'Hyd' <next line> 10.8 <next line> [10 , 20] <next line> True



# =======================================================================   

# Find outputs  (Home  work)
import  time
list = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , list)
while   True:
	try:
		print(next(f)) # 'Rama Rao' <next line>  'Rajesh' <next line> 'Manohar' <next line> 'Vamsi'
		time . sleep(1)
	except:
		break

# =======================================================================

# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda  x : x[1]  >=  12 , list)
while   True:
	try:
		print(next(f)) #  ('B' , 20) <next line> ('C' , 15) <next line> ('E' , 18)
		time . sleep(1)
	except:
		break 


# =======================================================================

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
		print(next(f)) # {'Roll Num' :  10 , 'Stud Name' : 'Rama Rao' , 'Marks' : 75} <next line> {'Roll Num'  :  15 , 'Stud Name' : 'Kiran' , 'Marks' : 65} <next line> {'Roll Num' :  5 , 'Stud Name' : 'Rajesh' , 'Marks' : 82}      
		time . sleep(1)
	except:
		break

# =======================================================================

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

# =======================================================================

# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
# How  to  iterate  thru  filter  object  with  next()  function
while   True:
    try:
        print(next(f1)) # 10 <next line> 20 <next line> 18 <next line> 26
        time . sleep(1)
    except :
        break

print('Iterate  thru  filter  object  with   for  loop')
# How  to  iterate  thru  filter  object  with  for  loop
for i in f1:
    print(i) # No output

print('Unpack  filter  object :  ' ,  *f1)
print('filter  object  converted  to   list  :  ' ,  list(f1))

# =======================================================================

#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
import  time
a = list(range(1 , 21))
f = filter(lambda  x : x  %  2  !=  0 , a)
while  True:  
	try:
		print(next(f)) # 1 <next line> 3 <next line> 5 <next line> 7 <next line> 9 <next line> 11 <next line> 13 <next line> 15 <next line> 17 <next line> 19                   
		time . sleep(1)
	except:     
		break

# =======================================================================

'''
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
'''
import  time
s=  'Python Programming'
vowels = 'AEIOUaeiou'
f = filter(lambda  x : x  in  vowels , s)   
print('Distinct  vowels  in  the  string  :  ' , set(f)) # Distinct  vowels  in  the  string  :  {'o' , 'a' , 'i'}

# ========================================================================

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
		print(next(f)) # (10 , 'Rama' , 10000.0) <next line> (15 , 'Rajesh' , 15000.0)      
		time .  sleep(1)
	except:
		break
