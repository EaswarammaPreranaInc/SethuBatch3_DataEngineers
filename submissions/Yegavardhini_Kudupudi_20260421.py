a = [10 , 20 , 15 ,  18 , 12]
k = 3
Shift  right  list  'a'  for  'k'  times   --->  [15 , 18 , 12 , 10 , 20]




def   rotate(a):  #  'a'  is  list
	shift   right  only  once
	[10 , 20 , 15 , 18 , 12]   --->  [12 , 10 , 20 , 15 , 18]
#  End  of  the  function	
Read  list   'a'
Read  'k' 
call  rotate()  'k'  times
k = 3
After  1st  call   -->  [12 , 10 , 20 , 15 , 18]
After  2nd   call   -->  [18 , 12 , 10 , 20 , 15]
After  3rd   call   -->  [15 , 18 , 12 , 10 , 20]



def rotate(nums ,k):
        
    n=len(nums)
    k=k%n
    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    return nums
def reverse(nums,start,end):
    while start<end:
        temp=nums[start]
        nums[start]=nums[end]
        nums[end]=temp
        start=start+1
        end=end-1

nums=list(eval(input()))
k=int(input())
print(rotate(nums,k))


# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   list)
while  True:
	try:
		print(next(f)) # 25 <nextline> 10.8 <nextline> 3+4j <nextline> Hyd <nextline>False
		time . sleep(1)
	except:
		break


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


# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda  x : x , list)
while  True:
	try:
		print(next(f)) # 25 <nextline> 10.8   <nextline> 3+4j <nextline> Hyd <nextline> (25,)
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
print('Filter  f1') # Filter  f1
disp(f1)
f2 = filter(None  , list)
print('Filter  f2') # Filter  f2
disp(f2) #10 <nextline> -25 <nextline> (25,) <nextline> Hyd <nextline> 10.8 <nextline> [10,20] <nextline> Trrue


# Find outputs  (Home  work)
import  time
list = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , list)
while   True:
	try:
		print(next(f)) # Rama Rao <nextline> Rajesh <nextline> Kiran <nextline> Manohar <nextline>Vamsi
		time . sleep(1)
	except:
		break


# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda  x : x[1]  >=  12 , list)
while   True:
	try:
		print(next(f)) #('B' , 20) <nextline> ('C' , 15) <nextline>  ('E' , 18)
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
		print(next(f)) #{'Roll Num' :  10 , 'Stud Name' : 'Rama Rao' , 'Marks' : 75}
                               # {'Roll Num'  :  15 , 'Stud Name' : 'Kiran' , 'Marks' : 65} 
                                # {'Roll Num' :  5 , 'Stud Name' : 'Rajesh' , 'Marks' : 82}
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
print('Filter  f1') # Filter  f1
disp(f1) # {'country' : 'USA' , 'sale' : 300.3} <nextline>  {'country' : 'UK' , 'sale' : 210.4} 
f2 = filter(lambda  x  :  x['sale']  >=  200  , list)
print('Filter  f2') # Filter  f2
disp(f2) # {'country' : 'china' , 'sale' : 200.2}  <nextline> {'country' : 'USA' , 'sale' : 300.3}  <nextline> {'country' : 'UK' , 'sale' : 210.4}


# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
while  True:
		try:
			print(next(f1))
			time . sleep(1)
		except:
			break
print('Iterate  thru  filter  object  with   for  loop')
for x in f1:
    print(x)
    time.sleep(1)
f2 = filter(lambda x: x % 2 == 0, a)
print('Unpack  filter  object :  ' ,  *f2)
f3 = filter(lambda x: x % 2 == 0, a)
print('filter  object  converted  to   list  :  ' ,  list(f3))


#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator

f = filter(lambda x: x % 2 != 0,  range(1, 21))
for n in f:
    print(n, end=" ")


'''
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
'''

s = input("Enter mixed case string: ")
vowels = set(filter(lambda x: x.lower() in 'aeiou', s))
print("Distinct vowels:", vowels)


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
		print(next(f)) # (10 , 'Rama' , 10000.0) <nextline> (15 , 'Rajesh' , 15000.0)
		time .  sleep(1)
	except:
		break