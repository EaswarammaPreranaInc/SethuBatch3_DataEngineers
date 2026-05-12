#  Modify  following  program  with  'with'  statement
def   create(f):
	try:
		print('Type  text  terminated  by  ctrl+z')
		while  line :=  input():
				f . write(line + '\n')
	except  EOFError:
		print(F'File  {f . name}  is  created')
#  End  of  the  function
fname = input('Enter  filename :  ')
with open(fname , 'w') as f:
    create(f)




'''
Repeat  prog5c(File-Create)  with  writelines()  method

Inputs
--------
Rama  Rao
9247
+-$
Hyd is green city
ctrl+z

List  --->  ['Rama  Rao\n' , '9247\n' , '+-$\n' , 'Hyd is green city\n']

File
-----
Rama  Rao
9247
+-$
Hyd is  green city
	
	
'''
def  create(f):
		print('Enter  text  terminated  by  ctrl + z')
		How  to  read  each  line  from  keyboard  and  write  to  the  list  until  user  strikes  ctrl+z
		How  to  write  list  to  the  file
		print(F'File  {f.name}  is  created')
#  End  of  the  function
How  to  read  the  filename
How  to  open  the  file
How  to  call  create()  function
How  to  close  the  file



'''  (Home  work)
Write  a  program  to  print  data  of  the  file

File
-----
Rama  Rao
9247
+-$
Hyd is green city

1) Which  method  is  used  to  read  data  of  the  file  ?  ---> read()

2) Which  function  is  used  to  print  whole  data  of  the  file ?  --->  print()

3) In  which  mode  is  file  opened ?  --->  read  mode
'''
def  disp(f):
	data = f.read()
	print(F'Data  of  the  file  {f . name}')
	print(data)
# End  of  the  function
fname=input()
f=open(fname,'r')
disp(f)
f.close()



'''  (Home  work)
Write  a  program  to  print  file  pagewise  and  page  length = 20   lines

File
-----
Rama  Rao
9247
+-$
Hyd is green city


1) Which  method  is  used  to  read  each  line  of  the  file  ?  --->  readline()

2) Which  function  is  used  to  print  each  line ?  ---> print()

3) How  long  is  the  procedure  repeated ?  --->  Until  end  of  the  file  is  reached

4) In  which  mode  is  file  opened ?  --->  read  mode

5) How  to  pause  execution  for  every  20  lines ?  --->  os . system('pause')  where  pause  is  a  dos  command

6) How  to  clear  the  20  lines   before  printing   next  20  lines ?  ---> os . system('cls')  where  cls  is  a  dos  command
'''
import os
def  disp(f):
	count=0
	while True:
        	line = f.readline()  
        	if line == '':        
            		break
        	print(line, end='')  
        	count += 1
        	if count % 20 == 0:
            		os.system('pause')  
            		os.system('cls')
#  End  of  the  function
fname = input() 
f = open(fname, 'r')        
disp(f)                    
f.close()



'''
Repeat  prog9b(File-pagewise)  with  for  loop
i.e.  Print  file  pagewise  and  pause  execution  for  every  20  lines

File
-----
Rama  Rao
9247
+-$
Hyd is green city

1) How  to  iterate  thru  the  file ?  --->  With  for  loop

2) Which  function  is  used  to  print  each  line ?  --->  print()

3) How  long  is  the  procedure  repeated ?  ---> Until  end  of  the  file  is  reached

4) In  which  mode  is  file  opened ?  ---> read  mode
'''
import  os
def  disp(f):
	count = 0
        for line in f:
        	print(line, end='')
        	count += 1
        	if count % 20 == 0:
            		os.system('pause')
            		os.system('cls')
# End  of  the  function
fname = input()
f = open(fname, 'r')
disp(f)
f.close()



'''
Repeat  prog9b(File-pagewise)  with  readlines()  method
i.e.  Print  file  pagewise  and  pause  execution  for  every  20  lines

File
-----
Rama  Rao
9247
+-$
Hyd is green city

List  --->  ['Rama Rao\n' , '9247\n' , '+-$\n' , 'Hyd is green city']


1) Which  method  is  used  to  read  the  whole  file  ?  ---> readlines()

2) Where  are  all  the  lines  stored ?  ---> List

3) How  to  print  each  line  of  the  list ?  --->  Iterate  thru  the  list  and  print  each  line

4) How  long  is  the  procedure  repeated ?  ---> Until  list  is  fully  iterated

5) In  which  mode  is  file  opened ?  --->  read  mode
'''
def  disp(f):
	How  to  print  each  line  of  the  file  and  pause  execution  for  every  20  lines
# End  of  the  function
How  to  read  filename
How  to  open  the  file
How  to  call  disp()  function
How  to  close  the  file



'''
Write  a  program  to  copy  contents  of  a  file  to  a  different  file

1st  File
---------
Rama  Rao
9247
+-$
Hyd  is  green  city
Eof 

2nd  file
----------
Rama  Rao
9247
+-$
Hyd  is  green  city



1) In  which  mode  is  1st  file  opened ?  ---> 'r'  mode
    In  which  mode  is  2nd  file  opened ?  ---> 'w'   mode

2) What  action  to  be  made  when  1st  file  does  not  exist ?  --->  Print  a  message

3) What  action  to  be  made  when  2nd  file  does  not  exist ?  --->  Copy  1st  file  to  2nd  file

4) What  action  to  be  made  when  both  the  files  are  existing ? --->																
																	Copy  file  when  user  input  is  yes  and  print  a  message  when  user  input  is  no
'''



'''
Write  a  program  to  append  data  of  a  file  to  another  file
i.e.  Copy  data  of  1st  file  to  the  end  of  2nd  file

1st  file
---------
Rama  Rao
9247
+-$
Hyd  is  green  city

2nd  file
----------
Hyd
Sec
Cyb
Rama  Rao
9247
+-$
Hyd  is  green  city



1) In  which  mode  is  1st  file  opened ?  ---> read  mode
    In  which  mode  is  2nd  file  opened ?  ---> append  mode

2) Where  does  file  handle  points  to  when  file  is  opened  in  append  mode ?  --->  End  of  the  file
    Where  does  file  handle  points  to  when  file  is  opened  in  read  or  write  mode ? --->  Begining  of  the  file
'''



# Write  a  program  to  implement  queue  using  list
class  queue:
	def  __init__(q):
		q.list=[]
	# q = queue()		
	def  isempty(q):
		return q.list==[]
	# q . isempty()	
	def  enqueue(q , x):  
		q.list.append(x)
		
	# q . enqueue(25)		
	def  dequeue(q):
		try:
			return q.list.pop(0)
		except: 
			return  None
	# q . dequeue()			
	def  first(q):
		try:
			return q.list[0]
		except:   
			return  None
	# q . first()			
	def  last(q):
		try:
			return q.list[-1]
		except:  
			return  None
	# q . last()			
	def  disp(q):
		print('Queue  :  ' ,  q.list)
	# q . disp()		
	def  size(q):
		return  len(q.list)
	# q . size()		
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  queue')
        print('4. First  element of queue')
        print('5. Last  element of queue')
        print('6. Number  of  elements  in  the  queue')
        print('7. Exit')
# End of  the  function
How  to  create  queue  class  object
while  True:
	menu()
	ch = int(input('Enter  choice : ' ))
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					q.enqueue(x)
					q.disp()
		case  2:
					x=q.dequeue()
					if  x==None:
						print('Queue  is  empty , deletion  is  not  permitted')
					else:
							print('Deleted  element  : ' , x)
					q.disp()
		case  3:
					q.disp()
		case  4:
					x=q.first()
					if  x==None:
							print('Queue  is  empty')
					else:
							print('First  element :  ' , x)
		case  5:
					x=q.last()
					if  x==None:
							print('Queue  is  empty')
					else:
							print('Last  element :  ' , x)
		case  6:
					print('Number  of  elements  :  ' ,  q.size())
		case  7:
					exit()
	# End  of  match
#  End  of  while  loop



# Write  a  program  to  implement  deque  using  list
class  deque:
	def   __init__(dq):
		dq.list=[]
	#  dq = deque()		
	def  isempty(dq):
            return  dq.list==[]
	# dq . isempty()
	def  ins_rear(dq , x):
			return dq.list.append(x)
	# dq . insrear(x)			
	def  ins_front(dq , x):
			return dq.list.insert(0,x)
	# dq . insfront(x)						
	def  del_front(dq):
			try:
				return dq.list.pop(0)
			except: 
				return  None
	# dq . delfront()										
	def  del_rear(dq):
			try:
				return dq.list.pop()
			except:  
				return  None
	def  disp(dq):
			print('Deque :  ' ,  dq.list)
	# dq . disp()			
	def  size(dq):
			return  len(dq.list)
	# dq . size()			
	def  leftmost(dq):
			try:
				return  dq.list[0]
			except: 
				return   None
	# dq . leftmost()
	def  rightmost(dq):
			try:
				return  dq.list[-1]
			except: 
				return   None
	# dq . rightmost()				
#End of the class
def  menu():
	print('1. Insert  element  at  the  end  of  deque')
	print('2. Insert  element  at  the  begining  of  deque')
	print('3. Delete  left  most  element')
	print('4. Delete  right  most  element')
	print('5. Print  Deque')
	print('6. Print  left  most  element')
	print('7. Print  right  most  element')
	print('8. Number  of  elements  in  deque')
	print('9. Exit')
#end of  the  function
How  to  create  deque  class  object
while  True:
	menu()
	ch = int(input('Enter Choice :   '))
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					dq.ins_rear(x)
					dq.disp()
		case  2:
					x = eval(input('Enter  element  to  be  inserted : '))
					dq.ins_front(x)
					dq.disp()
		case  3:
					x=dq.del_front()
					if  x==None:
						print('Deque  is  empty  ,  deletion  is  not  permitted')
					else:
						print('Deleted  element :  ' , x)
					dq.disp()
		case  4:
					x=dq.del_rear()
					if  x==None:
						print('Deque  is  empty  ,  deletion  is  not  permitted')
					else:
						print('Deleted  element :  ' , x)
					dq.disp()
		case  5:
					dq.disp()
		case  6:
					x=dq.leftmost()
					if  ???:
						print('Deque  is  empty')
					else:
						print('Leftmost  element :  ' , x)
		case  7:
					x=dq.rightmost()
					if  ???:
						print('Deque  is  empty')
					else:
						print('Rightmost  element :  ' , x)
		case  8:
					print('Number  of  elements   :  ' , dq.size())
		case  9:
					exit()
	# End  of  match
# End  of  while  loop




Conversion
------------
1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  --->  3 + 4 * 5 - 6 / (27^)
                                                              --->  3 + (45*) - 6 / (27^)
                                                              --->  3 + (45*) - (627^/)
                                                              --->  (345*+) - (627^/)
                                                              --->  345*+627^/-
    What  is  the  prefix  expression ?   ---  -+3*45/6^27 

2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  ---> abc^^
    What  is  the  prefix  expression ?   --->  a ^ (^bc)
							     --->  ^a^bc

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  --->  ab+c+
    What  is  the  prefix  expression ?  --->  ++abc

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  --->  (-b + ((b2^) - 4 * a * c) ^ 0.5) / (2 * a)
                                                              --->  (-b + ((b2^) - (4a*) * c) ^ 0.5) / (2 * a)
                                                              --->  (-b + ((b2^) - (4a*c*)) ^ 0.5) / (2 * a)
                                                              --->  (-b + (b2^ 4a*c*-) ^ 0.5) / (2 * a)
                                                              --->  (-b + (b2^ 4a*c*-0.5^)) / (2 * a)
                                                              --->  (-bb2^ 4a*c*-0.5^+) / (2 * a)
                                                              --->  (-bb2^ 4a*c*-0.5^+) / (2a*)
                                                              --->  -bb2^ 4a*c*-0.5^+2a*/
    What  is  the  prefix  expression ?   --->
				                             ---> (-b + ((^b2) - 4 * a * c) ^ 0.5) / (2 * a)
                                                                  (-b + ((^b2) - (*4a) * c) ^ 0.5) / (2 * a)
								  /+-b^-^b2**4ac0.5*2a

5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  ---> ab< bc> cd< and or
    What  is  the  prefix  expression ?   --->	or <ab and >bc <cd			                             

6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  --->  xy^5z*/2+
    What  is  the  prefix  expression ?   ---> +/^xy*5z2
				                             --->
7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  --->  abcd^e-fgh*+^*+i-
    What  is  the  prefix  expression ?   ---> -+a*b^-^cde+f*ghi



'''
Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from prog1b import stack
def  icp(operator):
	d={'+':1,'/':2,'^':4}
	return  d[operator]
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(operator):
	d={'-':1, '*': 2, '^': 3, '(': 0, '#': -1}
	return  d[operator]
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  --->  -1
'''
def  convert(infix):
	s.push(#)
	postfix = '' 
	for x in infix:
		if  ch.isalnum():
			postfix+=ch
		elif  ch==')'
			while s.peek()!='(':
				postfix+=s.pop()
			s.pop()
		else:
			while icp(ch)>isp(s.peek()):
				postfix+=s.pop()
			s.push(ch)
	#  End  of  for  loop
	while s.peek()!='#':
		postfix+=s.pop()  
	return postfix
#  End  of  the  function
infix=input()
postfix=convert(infix)
print('Postfix  expression :  ' , postfix)
