'''
Write  a  function  to  return  average  of  numbers  in  the  file

File
----
10
20.8
True
15
18.4
eof

sum = 0  + 10 + 20.8 + True + 15 + 18.4
ctr = 0  + 1 + 1 + 1 + 1 + 1
'''
def   avg(f):
	sum=0
	ctr=0
	for line in f:
		sum=sum+eval(line)
		ctr+=1
	return sum/ctr
#  End  of  the  function
filename=input('Enter filename: ')
f=open(filename,'r')
print(avg(f))
f.close()



'''
Write  a  program  to  merge  two  files  to  form  a  new  file

1st  file
---------
1st  line  of  1st  file
2nd  line  of  1st  file
3rd  line  of  1st  file
4th  line  of  1st  file

2nd  file
----------
1st  line  of  2nd  file
2nd  line  of  2nd  file
3rd  line  of  2nd  file

3rd  file
----------
1st  line  of  1st  file
2nd  line  of  1st  file
3rd  line  of  1st  file
4th  line  of  1st  file
1st  line  of  2nd  file
2nd  line  of  2nd  file
3rd  line  of  2nd  file


1) Let  1st  file  contain  10  lines  and   2nd  file  contain  7  lines
    What  does  3rd  file  contain ?  ---> 10 + 7 = 17  lines

2) What  action  to  be  made  when  both  the  files  are  existing ?  --->  Copy  all  the  lines  of  1st  file  to  3rd  file  and
																													then copy  all  the  lines  of  2nd  file  to  3rd  file

3) What  action  to  be  made  when  2nd  file  is  not  existing ?  ---> Copy  1st  file  to  3rd  file

4) What  action  to  be  made  when  1st  file  is  not  existing ?  ---> Copy  2nd  file  to  3rd  file

5) What  action  to  be  made  when  both  the  files  are  not  existing ?  ---> Print  a  message
'''
import  os
def  copy(file1 , file2):
	for line in file1:
        	file2.write(line)
#  End  of  the  function
fname1 = input("Enter 1st filename : ")
fname2 = input("Enter 2nd filename : ")
fname3 = input("Enter 3rd filename : ")
if os.path.isfile(fname1) and os.path.isfile(fname2):
	f1 = open(fname1, "r")
        f2 = open(fname2, "r")
        f3 = open(fname3, "w")
	copy(f1, f3)
        copy(f2, f3)
	f1.close()
        f2.close()
        f3.close()
	print(F'{fname1} and {fname2}  are  merged  to  form  {fname3}')
elif os.path.isfile(fname1):
	f1 = open(fname1, "r")
        f3 = open(fname3, "w")
	copy(f1, f3)
	f1.close()
        f3.close()
	print(F'{fname1}  is  copied  to  {fname3}')
elif os.path.isfile(fname2):
        f2 = open(fname2, "r")
        f3 = open(fname3, "w")
        copy(f2, f3)
        f2.close()
        f3.close()
	print(F'{fname2}  is  copied  to  {fname3}')
else:
	print('Both  the  files  are  not  existing')
	if os.path.isfile(fname3):
        	os.remove(fname3)



'''
Write   a  program  to  count  number  of   lines , characters , words , vowels , consonants ,  spaces , tabs  and
sentences  in  a  file

File
-----
Rama Rao
9247<tab>Sita
+-$ Hyd

str  object ---> 


List  'a'  --->   [ 3         27           6            2             1              0                 6               8 ]
                      Lines    Chars     Words   Spaces     Tabs     Sentences    Vowels     Consonants
'''
def  count_all(f):
	s=f.read()
	a = []
	c=0
	for line in f:
		c=c+1
	a.append(c)
	a.append(len(s))
	a.append(len(s.split( )))
	a.append(s.count(' '))
	a.append(s.count('\t'))
	a.append(s.count('.'))
	for ch in s:
        	if ch.isalpha():
			if ch.lower() in "aeiou":
                		vowels += 1
            		else:
                		consonants += 1
        a.append(vowels)
    	a.append(consonants)
    	return a
#  End  of   function
filename=input()
f=open(filename,'r')
count_all(f)
f.close()
b = ['Lines' , 'Chars' , 'Words' , 'Spaces' , 'Tabs' , 'Sentences' , 'Vowels' , 'Consonants']
for i in range(len(b)):
    print(f'{b[i]} = {a[i]}')



'''
Write  a  function  to  search  for  a  word  in  the  file  and   return  number  of  times  it  is  found

File
----
Hyd  is  green  city.
Hyd  is  hitec  city.
Hyd  is  beautiful  city.

str  object  --->  Hyd  is  green  city.\nHyd  is  hitec  city.\nHyd  is  beautiful  city.\n

What  is  the  result  when  'Hyd'  is  searched  in  the  file ?  --->   3
'''
def   search(f ,  word):
	s = f.read()
    	return s.count(word)
#End of  the  function
filename=input()
f=open(filename,'r')
word=input()
print(word, "is present", search(f, word), "times in file")




'''
Write  a  program  to  write  0! ,  1! , 2!, ...... n!  to  the  file

Hint:  Use  math . factorial()  function
'''
import math

def fact(f, n):
    for i in range(n + 1):
        f.write(f'{i}! = {math.factorial(i)}\n')

fname = input("Enter filename : ")
f = open(fname, "w")
n = int(input("Enter value of n : "))
fact(f, n)
f.close()
print("Factorials are written to the file")



'''
Write  a   program  to  remove  all  the   comments  in  a  python  file

1) Remove  all  single  line  comments  only  but  not   multi-line  comments

2) Do  not  remove  lines  which  starts  with  #
     Eg:  #statement  --->  Do  not  delete

3) Do  not  remove  lines  which  starts  with   <spaces>#
    Eg:  <Spaces>#   comment   --->  Do  not  delete

4) Remove  comments  which  are  at  the  end  of  statement
    Eg:   statement  #   comment  --->  Delete  the  comment

5) Input  is  filename

6) File
     ----
	 # Question
     stmt1   #  comment
     stmt2
     #stmt3
     stmt4  #  comment
     <spaces>#stmt5

7) List  --->  ['# Question\n' ,  'stmt1 # comment' , 'stmt2' , '#stmt3' , 'stmt4  #  comment' , '<spaces>#stmt5']

8) File
   ------
   # Question
   stmt1
   stmt2
   #stmt3
   stmt4
   #stmt5

9) What  action  to  be  made  when  the  line  starts  with  '#' ?  --->  Write  line  to  the  file

10) What  action  to  be  made  when  the  line  contains  '#' ?  --->  Write  statement  before  #  to  the  file

11) What  action  to  be  made  when  the  line  does  not  contain  '#' ?  --->  Write  line  to  the  file

12) What  action  to  be  made  when  line  has  spaces  before  #  ?  --->  Write  the  line  to  the  file  without  leading  spaces
'''
import os

def cmt_remove(f):
    lines = f.readlines()
    fw = open(f.name, "w")
    for line in lines:
        temp = line.lstrip()
        if temp.startswith('#'):
            fw.write(temp)
        elif '#' in line:
            a = line.split('#')
            fw.write(a[0].rstrip() + '\n')
        else:
            fw.write(line)
    fw.close()
try:
    fname = input("Enter filename : ")
    f = open(fname, "r")
    cmt_remove(f)
    f.close()
    print(f'All the single line comments are removed from {fname}')
except:
    print('File does not exist')




#  Find  outputs  (Home  work)
f = open('a.txt' , 'w+')
f . write('Hyd is green city.')
f . seek(0)
f . write('Sec')
f . seek(0)
print(f . read())  
f . seek(7)
print(f . read(5))
f . seek(0 , 2)
f . write('Hyd is Hitec city.')
f . seek(0)
print(f . read())  
f . seek(7)
f . write('red')
f . seek(0)
print(f . read())  


'''
File  --->  

output:
Sec is green city.
green
Sec is green city.Hyd is Hitec city.
Sec is reden city.Hyd is Hitec city.


Where  does  file  handle  point  to  (i.e.  offset)  --->



#  Find  outputs (Home  work)
f = open('a.txt' , 'w+')
print(f . tell()) # 0
f . write('Hyd is green city')
print(f . tell())  # 17
f . seek(7)
print(f . read(5))  # green 
print(f . tell())  # 12 

'''
File   --->   

File  handle  points  ----> 


H   y    d             i     s          g     r     e      e     n              c      i      t      y     eof
0   1     2     3     4    5    6    7     8     9     10    11    12     13    14    15    16    17
'''



'''
Write  a  program  to  evaluate  prefix  expression

Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -
'''



#  Write  a  program  to  convert  postfix  to  prefix


def postfix_to_prefix(postfix):
    s = Stack()
    for ch in postfix:
        if ch.isalnum():
            s.push(ch)
        else:
            op2 = s.pop()
            op1 = s.pop()
            temp = ch + op1 + op2
            s.push(temp)
    return s.pop()


postfix = input("Enter postfix expression : ")
prefix = postfix_to_prefix(postfix)
print("Prefix expression :", prefix)



# Write  a  program  to  implement  min  priority  queue  using  list
class  priority_queue:
	def  __init__(pq):
		pq.list=[]
	# pq = priority_queue()		
	def  isempty(pq):
		return  pq.list==[]
	# pq . isempty() 		
	def  insert(pq , x):
		 pq.list.append(x)
		 pq.list.sort()		 
	# pq . insert(25)		 
	def  delete(pq):
		try:
			return pq.list.pop(0)
		except:  
			return  None
	# x = pq . delete()			
	def  highest_priority(pq):
		try:
			return pq[0]
		except:  
			return  None
	# x = pq . highest_priority()			
	def  smallest_priority(pq):
		try:
			return pq[-1]
		except:   
			return  None
	# x = pq . smallest_priority()			
	def  disp(pq):
		print('Priority  Queue :  ' , pq.list)
	# pq . disp()		
	def   size(pq):
		return   len(pq.list)
	# pq . size()		
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  priority  queue')
        print('4. Highest  priority  element of  priority  queue')
        print('5. Smallest  priority  element of  priority  queue')
        print('6. Number  of  elements  in  the  priority  queue')
        print('7. Exit')
# End of  the  function
How  to  create  priority_queue()  class  object
while  True:
	menu()
	ch = int(input('Enter  choice : ' ))
	match  ch:
		case  1:
				x = eval(input('Enter  element  to  be  inserted : '))
				pq.list.insert(x)
				pq.disp()
		case  2:
				x=delete()
				if  x==None:
						print('Priority  queue  is  empty  , deletion  is  not  permitted')
				else:
						print('Deleted  element : '  , x)
				pq.disp()
		case  3:
				pq.disp()
		case  4:
				x = pq . smallest_priority()
				if  x==None:
						print('Priority  queue  is  empty')
				else:
						print('Highest  priority  element :  ' ,  x)
		case  5:
				x = pq.smallest_priority()
				if  x==None:
						print('priority  queue  is  empty')
				else:
						print('Smallest  priority  element :  ' ,  x)
		case  6:
				print('Number  of  elements  :  ' , pq.size())
		case  7:
				exit()
		# End  of  match


#  Write  functions  to  create  and  print  linked  list
class  node:
		def   __init__(self , x):  
				self . data = x   
				self . link = None  
		'''
		1) new = node(25)
		
		2) object  new  ---> 	 data = 25	 , link = None
		'''		
class  linked_list:
		def   __init__(a):
				a . first = None  
		'''
		1) a = linked_list()
		
		2) Object  'a'  --->  first = None
		'''
		def  isempty(a):
				return  a . first == None  
		# a . isempty()  --->  True / False
		def  disp(a):
				if  a . isempty():  
						print('Linked  List  is  empty')
				else:
						p = a . first
						while  p != None:
								print(p . data , end = '\t') 
								p = p . link
						print()
		# a . disp()					
		def  append(a , new):  
				How  to  append  a  node  to  empty  linked  list
				How  to  append  a  node  to  non-empty  linked  list
		# a . append(new)						
		def  create(a):
				How  to  create  a  linked  list
		# a . create()						
# End  of  the  class
How  to  create  linked  list
print('Linked  List  :  ' , end = '')
How  to  print  linked  list