1) Modify  following  program  with  'with'  statement
def   create(f):
	try:
		print('Type  text  terminated  by  ctrl+z')
		while  line :=  input():
				f . write(line + '\n')
	except  EOFError:
		print(F'File  {f . name}  is  created')
#  End  of  the  function
fname = input('Enter  filename :  ')
f = open(fname , 'w')
create(f)
f . close()

#Modified Program
def   create(f):
	try:
		print('Type  text  terminated  by  ctrl+z')
		while  line :=  input():
				f . write(line + '\n')
	except  EOFError:
		print(F'File  {f . name}  is  created')
#  End  of  the  function
fname = input('Enter  filename :  ')
with open(fname, 'w') as f:
    create(f)

2) Repeat  prog5c(File-Create)  with  writelines()  method

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
		list = []
		try: 
		   print('Enter  text  terminated  by  ctrl + z')
		   while true:
		       line = input() 
		       list.append(line + '\n')#How  to  read  each  line  from  keyboard  and  write  to  the  list  until  user  strikes  ctrl+z
		
		 except EOFError :
		       f.writelines(list) #How  to  write  list  to  the  file
                       print(F'File  {f.name}  is  created')
#  End  of  the  function
fname = input("Enter filename : ") #How  to  read  the  filename
f = open(fname, 'w') #How  to  open  the  file
create(f) #How  to  call  create()  function
f.close() #How  to  close  the  file


3) Write  a  program  to  print  data  of  the  file

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
	data = f.read() #How  to  read  the  whole  file
	print(F'Data  of  the  file  {f . name}')
	print(data) #How  to  print  the  file
# End  of  the  function
fname = input('Enter filename:') #How  to  read  the  filename
f = open(fname, 'r') #How  to  open  the  file
disp(f) #How  to  call  disp()  function
f.close() #How  to  close  the  file

4) Write  a  program  to  print  file  pagewise  and  page  length = 20   lines

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
	count = 0
	while true:
	   line = f.readline()
	   if line == '':
		break
	   print(line, end='')
	   count += 1
	   if count % 20 == 0:
		os.system('pause')
		os.system('cls')
#  End  of  the  function
fname = input('Enter filename : ') #How  to  read  filename
f = open(fname, 'r') #How  to  open  the  file
disp(f) #How  to  call  disp()  function
f.close() #How  to  close  the  file

5) Repeat  prog9b(File-pagewise)  with  for  loop
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
import os
def disp(f):
    count = 0
    for line in f:
        print(line, end='')
        count += 1
        if count % 20 == 0:
            os.system('pause')
            os.system('cls')
# End  of  the  function
fname = input('Enter filename : ') #How  to  read  filename
f = open(fname, 'r') #How  to  open  the  file
disp(f) #How  to  call  disp()  function
f.close() #How  to  close  the  file

6) Repeat  prog9b(File-pagewise)  with  readlines()  method
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
import os
def disp(f):
    lines = f.readlines()
    count = 0
    for line in lines:
        print(line, end='')
        count += 1
        if count % 20 == 0:
            os.system('pause')
            os.system('cls') #How  to  print  each  line  of  the  file  and  pause  execution  for  every  20  lines
# End  of  the  function
fname = input('Enter filename : ') #How  to  read  filename
f = open(fname, 'r') #How  to  open  the  file
disp(f) #How  to  call  disp()  function
f.close() #How  to  close  the  file

7) Write  a  program  to  copy  contents  of  a  file  to  a  different  file

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

4) What  action  to  be  made  when  both  the  files  are  existing ? --->Copy  file  when  user  input  is  yes  and  print  a  message  when  user  input  is  no
'''
#file1 = input("Enter first filename : ")
try:
    fp1 = open(file1, "r")
except FileNotFoundError:
    print(f"File {file1} does not exist")
else:
    file2 = input("Enter second filename : ")
    try:
        fp2 = open(file2, "r")
        fp2.close()
        choice = input(f"{file2} already exists, overwrite (y/n) ?: ")
        if choice.lower() != 'y':
            print("File is not copied")
            fp1.close()
            exit()
    except FileNotFoundError:
        pass
    fp2 = open(file2, "w")
    data = fp1.read()
    fp2.write(data)
    print(f"Data of file {file1} is copied to {file2}")
    fp1.close()
    fp2.close()

8) Write  a  program  to  append  data  of  a  file  to  another  file
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
#file1 = input("Enter first filename : ")

try:
    f1 = open(file1, "r")
except FileNotFoundError:
    print(f"File {file1} does not exist")
    exit()
file2 = input("Enter second filename : ")
f2 = open(file2, "a")
data = f1.read()
f2.write(data)
print(f"Data of file {file1} is appended or copied to file {file2}")
f1.close()
f2.close()


9) Write  a  program  to  implement  queue  using  list
class  queue:
	def  __init__(q):
		q.lst = [] #How  to  initialize  queue  with  an  empty  list
	# q = queue()		
	def  isempty(q):
		return q.lst == [] #return  True  when  list  held  by  queue  is  empty  and  False  otherwise
	# q . isempty()	
	def  enqueue(q , x):  
		q.lst.append(x) #How  to  append  'x'  to  the  list  held  by  object  'q'
	# q . enqueue(25)		
	def  dequeue(q):
		try:
		     return q.lst.pop(0) #How  to  remove  first  element  of  the  list  held  by  object  'q'  and  returns  the  deleted  element
		except: 
			return  None
	# q . dequeue()			
	def  first(q):
		try:
			 return q.lst.pop[0] #How  to  return  first  element  of  the  list  held  by  object  'q'
		except:   
			return  None
	# q . first()			
	def  last(q):
		try:
			return q.lst[-1] #How  to  return  last  element  of  the  list  held  by  object   'q'
		except:  
			return  None
	# q . last()			
	def  disp(q):
		print('Queue  :  ' , q.lst) # How  to  print  the  list  held  by  object  'q'
	# q . disp()		
	def  size(q):
		return len(q.lst) #return  number   of  elements  in   the  list  held  by  object  'q'
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
					q.enqueue(x) #How  to  insert  'x'  into  the  queue
					q.disp() #How  to  print  the  queue
		case  2:
				 x = q.dequeue() #How  to  remove  element  of  the  queue
					if x is None:
						print('Queue  is  empty , deletion  is  not  permitted')
					else:
							print('Deleted  element  : ' , ???)
				q.disp() #How  to  print  the  queue
		case  3:
					q.disp() #How  to  print  the  queue
		case  4:
				 x = q.first()	#How  to  obtain  first  element  of  the  queue
					i if x is None:
                print("Queue is empty")
            else:
                print("First element :", x)
		case  5:
			 x = q.last() #How  to  obtain  first  element  of  the  queue
		if x is None:
                print("Queue is empty")
            else:
                print("Last element :", x)
		 case 6:
            print("Number of elements :", q.size())

        case 7:
            break
	# End  of  match
#  End  of  while  loop



10) Write  a  program  to  implement  deque  using  list
# Write a program to implement deque using list

class Deque:

    def __init__(dq):

        # How to initialize deque with an empty list
        dq.lst = []

    # dq = Deque()

    def isempty(dq):

        # return True when deque is empty and False otherwise
        return dq.lst == []

    # dq.isempty()

    def ins_rear(dq, x):

        # How to append 'x' to the list held by object dq
        dq.lst.append(x)

    # dq.ins_rear(x)

    def ins_front(dq, x):

        # How to insert 'x' at the beginning of the list held by object dq
        dq.lst.insert(0, x)

    # dq.ins_front(x)

    def del_front(dq):

        try:

            # How to remove left most element of the list held by object dq
            # and returns the deleted element
            return dq.lst.pop(0)

        except:

            return None

    # dq.del_front()

    def del_rear(dq):

        try:

            # How to remove right most element of the list held by object dq
            # and returns the deleted element
            return dq.lst.pop()

        except:

            return None

    # dq.del_rear()

    def disp(dq):

        print('Deque : ', dq.lst)

        # How to print the list held by object dq

    # dq.disp()

    def size(dq):

        # return number of elements in the list held by object dq
        return len(dq.lst)

    # dq.size()

    def leftmost(dq):

        try:

            # return left most element of the list held by object dq
            return dq.lst[0]

        except:

            return None

    # dq.leftmost()

    def rightmost(dq):

        try:

            # return right most element of the list held by object dq
            return dq.lst[-1]

        except:

            return None

    # dq.rightmost()

# End of the class


def menu():

    print('1. Insert element at the end of deque')
    print('2. Insert element at the beginning of deque')
    print('3. Delete left most element')
    print('4. Delete right most element')
    print('5. Print Deque')
    print('6. Print left most element')
    print('7. Print right most element')
    print('8. Number of elements in deque')
    print('9. Exit')

# End of the function


# How to create deque class object
dq = Deque()

while True:

    menu()

    ch = int(input('Enter Choice : '))

    match ch:

        case 1:

            x = eval(input('Enter element to be inserted : '))

            # How to insert 'x' at the end of deque
            dq.ins_rear(x)

            # How to print deque
            dq.disp()

        case 2:

            x = eval(input('Enter element to be inserted : '))

            # How to insert 'x' at the beginning of deque
            dq.ins_front(x)

            # How to print deque
            dq.disp()

        case 3:

            # How to remove left most element of deque
            x = dq.del_front()

            if x is None:

                print('Deque is empty , deletion is not permitted')

            else:

                print('Deleted element : ', x)

            # How to print deque
            dq.disp()

        case 4:

            # How to remove right most element of deque
            x = dq.del_rear()

            if x is None:

                print('Deque is empty , deletion is not permitted')

            else:

                print('Deleted element : ', x)

            # How to print deque
            dq.disp()

        case 5:

            # How to print deque
            dq.disp()

        case 6:

            # How to obtain left most element of deque
            x = dq.leftmost()

            if x is None:

                print('Deque is empty')

            else:

                print('Leftmost element : ', x)

        case 7:

            # How to obtain right most element of deque
            x = dq.rightmost()

            if x is None:

                print('Deque is empty')

            else:

                print('Rightmost element : ', x)

        case 8:

            print('Number of elements : ', dq.size())

        case 9:

            # How to stop execution
            break

# End of match

# End of while loop

11) Conversion
------------
1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  --->  3 + 4 * 5 - 6 / (27^)
                                                              --->  3 + (45*) - 6 / (27^)
                                                              --->  3 + (45*) - (627^/)
                                                              --->  (345*+) - (627^/)
                                                              --->  345*+627^/-
    What  is  the  prefix  expression ?   --->   -+3*45/6^27

2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  --->  abc^^
    What  is  the  prefix  expression ?   --->  a ^ (^bc)
							     --->  ^a^bc

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  --->  ab+c+
    What  is  the  prefix  expression ?  --->   ++abc

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  --->  (-b + ((b2^) - 4 * a * c) ^ 0.5) / (2 * a)
                                                              --->  (-b + ((b2^) - (4a*) * c) ^ 0.5) / (2 * a)
                                                              --->  (-b + ((b2^) - (4a*c*)) ^ 0.5) / (2 * a)
                                                              --->  (-b + (b2^ 4a*c*-) ^ 0.5) / (2 * a)
                                                              --->  (-b + (b2^ 4a*c*-0.5^)) / (2 * a)
                                                              --->  (-bb2^ 4a*c*-0.5^+) / (2 * a)
                                                              --->  (-bb2^ 4a*c*-0.5^+) / (2a*)
                                                              --->  -bb2^ 4a*c*-0.5^+2a*/
    What  is  the  prefix  expression ?   ---> /(+(-b)(^( -(^b2)(**4ac) )0.5))(*2a)
                       --->  /+-b^-^b2**4ac0.5*2a
				                            
5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  --->   ab<bc>cd<andor
    What  is  the  prefix  expression ?   --->	  or<aband>bc<cd			                             

6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  --->   xy^5z*/2+
    What  is  the  prefix  expression ?  --->  +(/^xy*5z)2
                       --->  +/^xy*5z2
7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  --->   abcd^e-fgh*+^*+i-
    What  is  the  prefix  expression ?   --->-(+a(*b(^(-(^cd)e)(+f(*gh)))))i
                       --->  -+a*b^-^cde+f*ghi

12) Write  a  program  to  convert  infix  to  postfix

Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
def  icp(operator):
	return  icp  of  the  operator
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(operator):
	return  isp  of  the  operator
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  --->  -1
'''
def  convert(infix):
	How  to  push  '#'  into  the  stack
	postfix = '' 
	How  to  iterate  thru  infix  expression
		if  ch  is  an  operand
			How  to  concatenate  the  operand  to  postfix  expression
		elif  Is  ch  ')'
			Remove  each  operator  of  the  stack  and  concatenate  to  postfix  expression  and
			repeat  this  process  until  '('  is  the  last  element  of  stack.
			Remove  '('  also  but  do  not  concatenate  to  postfix  expression
		else:
			Remove  each  operator  of  the  stack  and  concatenate  to  postfix  expression  and
			repeat  this  process  until  icp > isp.
			Push  the  operator  into  the  stack  as  soon  as   icp  >  isp
	#  End  of  for  loop
	Remove  each  operator  of  the  stack  and  concatenate  to  postfix  expression  and  
	repeat  '#'  is  the  last  element  of  stack
	Finally  return  postfix  expression
#  End  of  the  function
How  to  read  infix  expression
How  to  convert  infix  expression  to  postfix  expression
print('Postfix  expression :  ' , ???)