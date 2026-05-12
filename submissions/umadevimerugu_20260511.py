'''#  Modify  following  program  with  'with'  statement
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
f . close() '''
def create(f):
    try:
        print('Type text terminated by ctrl+z')
        while line := input():
            f.write(line + '\n')
    except EOFError:
        print(f'File {f.name} is created')
# End of the function
fname = input('Enter filename : ')
with open(fname, 'w') as f:
    create(f)

'''prog5c:
def   create(f):
	try:
		print('Type  text  terminated  by  ctrl+z')
		while  line :=  input():  #  Reads  each  line  of  input  from  keyboard  until  user  strikes  ctrl+z
				f . write(line + '\n')  #  Writes  each  line  to  the  file  along  with  '\n'
	except  EOFError:   #   Executed  as  soon   as  user  strikes  ctrl + z
		print(F'File  {f . name}  is  created')
#  End  of  the  function
fname = input('Enter  filename :  ')  #  Reads  filename
f = open(fname , 'w')  #  Opens  file  in  write  mode
create(f)  #  Writes  user  input  text  to  the  file
f . close() 
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
def  create(f):
		print('Enter  text  terminated  by  ctrl + z')
		How  to  read  each  line  from  keyboard  and  write  to  the  list  until  user  strikes  ctrl+z
		How  to  write  list  to  the  file
		print(F'File  {f.name}  is  created')
#  End  of  the  function
How  to  read  the  filename
How  to  open  the  file
How  to  call  create()  function
How  to  close  the  file'''
def create(f):
    try:
        print('Enter text terminated by ctrl + z')
        lst = []
        while True:
            line = input()      
            lst.append(line + '\n')   
    except EOFError:
        f.writelines(lst)     
        print(f'File {f.name} is created')
fname = input('Enter filename : ')   
f = open(fname, 'w')    
create(f)              
f.close()               

'''Write  a  program  to  print  data  of  the  file
File
-----
Rama  Rao
9247
+-$
Hyd is green city
1) Which  method  is  used  to  read  data  of  the  file  ?  ---> read()
2) Which  function  is  used  to  print  whole  data  of  the  file ?  --->  print()
3) In  which  mode  is  file  opened ?  --->  read  mode '''
def disp(f):
    data = f.read()     
    print(f'Data of the file {f.name}')
    print(data)         
fname = input('Enter filename : ')  
f = open(fname, 'r')  
disp(f)                 
f.close()               

'''prog 9b:
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
6) How  to  clear  the  20  lines   before  printing   next  20  lines ?  ---> os . system('cls')  where  cls  is  a  dos  command '''
import os
def disp(f):
    while True:
        for i in range(20):
            line = f.readline()     
            if line == '':
                return              
            print(line, end='')     
    os.system('pause')        
    os.system('cls')            
fname = input('Enter filename : ')  
f = open(fname, 'r')    
disp(f)                 
f.close()               

'''Repeat  prog9b(File-pagewise)  with  for  loop
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
4) In  which  mode  is  file  opened ?  ---> read  mode '''
import os
def disp(f):
    count = 0
    for line in f:
        print(line, end='')
        count += 1
        if count % 20 == 0:
            os.system('pause')
            os.system('cls')
fname = input('Enter filename : ')
f = open(fname, 'r')
disp(f)
f.close()         

'''Repeat  prog9b(File-pagewise)  with  readlines()  method
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
    lst = f.readlines()
    print('List --->', lst)
    count = 0
    for line in lst:
        print(line, end='')
        count += 1
        if count % 20 == 0:
            os.system('pause')
            os.system('cls')
fname = input('Enter filename : ')
f = open(fname, 'r')
disp(f)
f.close()

'''Write  a  program  to  copy  contents  of  a  file  to  a  different  file
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
Enter first filename : 1.txt
Enter second filename : 2.txt
Data of file 1.txt is copied to 2.txt

Enter first filename : 4.txt
File 4.txt does not exist


Enter first filename : 1.txt
Enter second filename : 2.txt
2.txt already exists, overwrite (y/n)? : y
Data of file 1.txt is copied to 2.txt

Enter first filename : 1.txt
Enter second filename : 2.txt
2.txt already exists, overwrite (y/n)? : n
Program terminates without copy'''
import os
fname1 = input('Enter first filename : ')
if os.path.isfile(fname1):
    fname2 = input('Enter second filename : ')
    if os.path.isfile(fname2):
        ch = input(f'{fname2} already exists, overwrite (y/n)? : ')
        if ch == 'y':
            f1 = open(fname1, 'r')
            f2 = open(fname2, 'w')
            data = f1.read()
            f2.write(data)
            print(f'Data of file {fname1} is copied to {fname2}')
            f1.close()
            f2.close()
        else:
            print('Program terminates without copy')
    else:
        f1 = open(fname1, 'r')
        f2 = open(fname2, 'w')
        data = f1.read()
        f2.write(data)
        print(f'Data of file {fname1} is copied to {fname2}')
        f1.close()
        f2.close()
else:
    print(f'File {fname1} does not exist')
    
'''Write  a  program  to  append  data  of  a  file  to  another  file
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
Enter first filename : 1.txt
Enter second filename : 2.txt
Data of file 1.txt is appended or copied to file 2.txt

Enter first filename : 1.txt
Enter second filename : 2.txt
Data of file 1.txt is appended or copied to file 2.txt

Enter first filename : 1.txt
File 1.txt does not exist'''
import os
fname1 = input('Enter first filename : ')
if os.path.isfile(fname1):
    fname2 = input('Enter second filename : ')
    f1 = open(fname1, 'r')
    f2 = open(fname2, 'a')
    data = f1.read()
    f2.write(data)
    print(f'Data of file {fname1} is appended or copied to file {fname2}')
    f1.close()
    f2.close()
else:
    print(f'File {fname1} does not exist')

# Write a program to implement queue using list
class queue:
    def __init__(q):
        q.lst = []
    def isempty(q):
        return q.lst == []
    def enqueue(q, x):
        q.lst.append(x)
    def dequeue(q):
        try:
            return q.lst.pop(0)
        except:
            return None
    def first(q):
        try:
            return q.lst[0]
        except:
            return None
    def last(q):
        try:
            return q.lst[-1]
        except:
            return None
    def disp(q):
        print('Queue : ', q.lst)
    def size(q):
        return len(q.lst)

def menu():
    print('1. Insertion')
    print('2. Deletion')
    print('3. Print queue')
    print('4. First element of queue')
    print('5. Last element of queue')
    print('6. Number of elements in the queue')
    print('7. Exit')
q = queue()
while True:
    menu()
    ch = int(input('Enter choice : '))
    match ch:
        case 1:
            x = eval(input('Enter element to be inserted : '))
            q.enqueue(x)
            q.disp()
        case 2:
            x = q.dequeue()
            if x == None:
                print('Queue is empty, deletion is not permitted')
            else:
                print('Deleted element : ', x)
            q.disp()
        case 3:
            q.disp()
        case 4:
            x = q.first()
            if x == None:
                print('Queue is empty')
            else:
                print('First element : ', x)
        case 5:
            x = q.last()

            if x == None:
                print('Queue is empty')
            else:
                print('Last element : ', x)
        case 6:
            print('Number of elements : ', q.size())
        case 7:
            break

# Write  a  program  to  implement  deque  using  list

class deque:
    def __init__(dq):
        dq.lst = []
    def isempty(dq):
        return dq.lst == []
    def ins_rear(dq, x):
        dq.lst.append(x)
    def ins_front(dq, x):
        dq.lst.insert(0, x)
    def del_front(dq):
        try:
            return dq.lst.pop(0)
        except:
            return None
    def del_rear(dq):
        try:
            return dq.lst.pop()
        except:
            return None
    def disp(dq):
        print('Deque : ', dq.lst)
    def size(dq):
        return len(dq.lst)
    def leftmost(dq):
        try:
            return dq.lst[0]
        except:
            return None
    def rightmost(dq):
        try:
            return dq.lst[-1]
        except:
            return None
        
def menu():
    print('1. Insert element at the end of deque')
    print('2. Insert element at the begining of deque')
    print('3. Delete left most element')
    print('4. Delete right most element')
    print('5. Print Deque')
    print('6. Print left most element')
    print('7. Print right most element')
    print('8. Number of elements in deque')
    print('9. Exit')

dq = deque()
while True:
    menu()
    ch = int(input('Enter Choice : '))
    match ch:
        case 1:
            x = eval(input('Enter element to be inserted : '))
            dq.ins_rear(x)
            dq.disp()
        case 2:
            x = eval(input('Enter element to be inserted : '))
            dq.ins_front(x)
            dq.disp()
        case 3:
            x = dq.del_front()
            if x == None:
                print('Deque is empty, deletion is not permitted')
            else:
                print('Deleted element : ', x)
            dq.disp()
        case 4:
            x = dq.del_rear()
            if x == None:
                print('Deque is empty, deletion is not permitted')
            else:
                print('Deleted element : ', x)
            dq.disp()
        case 5:
            dq.disp()
        case 6:
            x = dq.leftmost()
            if x == None:
                print('Deque is empty')
            else:
                print('Leftmost element : ', x)
        case 7:
            x = dq.rightmost()
            if x == None:
                print('Deque is empty')
            else:
                print('Rightmost element : ', x)
        case 8:
            print('Number of elements : ', dq.size())
        case 9:
            break

'''
Conversion
------------
1) Let  infix  expression  be  3 + 4 * 5 - 6 / 2 ^ 7
    What  is  the  postfix  expression ?  --->  3 + 4 * 5 - 6 / (27^)
                                                              --->  3 + (45*) - 6 / (27^)
                                                              --->  3 + (45*) - (627^/)
                                                              --->  (345*+) - (627^/)
                                                              --->  345*+627^/-
    What  is  the  prefix  expression ?   --->  3 + 4 * 5 - 6 / 2 ^ 7
                                          --->  3 + (*45) - 6 / (^27)
                                          --->  3 + (*45) - (/6^27)
										  --->  (+3*45) - (/6^27)
										  ---> -+3*45/6^27

2) Let  infix  expression  be  a ^ b ^ c
    What  is  the  postfix  expression ?  ---> a ^ b ^ c
                                          ---> a ^ (bc^)
                                        ---> abc^^
    What  is  the  prefix  expression ?   --->  a ^ (^bc)
							              --->  ^a^bc

3) Let  infix  expression  be  a + b + c
    What  is  the  postfix  expression ?  --->  a + b + c
                                          ---> (ab+) + c
                                          ---> ab+c+
    What  is  the  prefix  expression ?  --->  a + b + c
    									 ---> (+ab) + c
										 ---> ++abc

4) Let  infix  expression  be  (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
    What  is  the  postfix  expression ?  --->  (-b + ((b2^) - 4 * a * c) ^ 0.5) / (2 * a)
                                                              --->  (-b + ((b2^) - (4a*) * c) ^ 0.5) / (2 * a)
                                                              --->  (-b + ((b2^) - (4a*c*)) ^ 0.5) / (2 * a)
                                                              --->  (-b + (b2^ 4a*c*-) ^ 0.5) / (2 * a)
                                                              --->  (-b + (b2^ 4a*c*-0.5^)) / (2 * a)
                                                              --->  (-bb2^ 4a*c*-0.5^+) / (2 * a)
                                                              --->  (-bb2^ 4a*c*-0.5^+) / (2a*)
                                                              --->  -bb2^ 4a*c*-0.5^+2a*/
    What  is  the  prefix  expression ?   ---> (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
				                          ---> (+(-b)(^(b^2-4*a*c)0.5)) / (*2a)
										  ---> (+(-b)(^(-(b^2)(*(*4a)c))0.5)) / (*2a)
										  ---> (/ (+(-b)(^(-( ^b2)(*(*4a)c))0.5)) (*2a))
										  ---> /+-b^-^b2**4ac0.5*2a

5) Let  infix  expression  be  a < b  or  b > c   and  c < d
    What  is  the  postfix  expression ?  ---> a < b or b > c and c < d 
    									---> (ab<) or b > c and c < d
										---> (ab<) or (bc>) and c < d
										---> (ab<) or (bc>) and (cd<)
										---> (ab<) or (bc>cd<and)
										---> ab<bc>cd<andor
    What  is  the  prefix  expression ?   --->	a < b or b > c and c < d
    									---> (<ab) or (>bc) and (<cd)
										---> (<ab) or (and>bc<cd)
										---> or<aband>bc<cd			                             

6) Let  infix  expression  be  x ^ y / ( 5 * z) + 2
    What  is  the  postfix  expression ?  --->  x ^ y / (5 * z) + 2
    									---> (xy^) / (5z*) + 2
										---> (xy^5z*/) + 2
										---> xy^5z*/2+
    What  is  the  prefix  expression ?   --->x ^ y / (5 * z) + 2
				                         ---> (^xy) / (*5z) + 2
										---> (/^xy*5z) + 2
										---> +/^xy*5z2
7) Let  infix  expression  be  a + b * (c ^ d - e) ^ (f + g * h) - i
    What  is  the  postfix  expression ?  --->  a + b * (c ^ d - e) ^ (f + g * h) - i
    									---> a + b * ((cd^) - e) ^ (f + g * h) - i
										---> a + b * (cd^e-) ^ (f + g * h) - i
										---> a + b * (cd^e-) ^ (f + (gh*)) - i
										---> a + b * (cd^e-) ^ (fgh*+) - i
										---> a + (b(cd^e-fgh*+^*)) - i
										---> abcd^e-fgh*+^*+i-
    What  is  the  prefix  expression ?   ---> a + b * (c ^ d - e) ^ (f + g * h) - i
										---> a + b * (-(^cd)e) ^ (+(f)(*gh)) - i
										---> a + (*b(^(-(^cd)e)(+f(*gh)))) - i
										---> (+a(*b(^(-(^cd)e)(+f(*gh))))) - i
										---> -+a*b-^cde+f*ghi
'''

'''Write  a  program  to  convert  infix  to  postfix
Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite '''
from prog1b import stack
def icp(operator):
    if operator in ['+', '-']:
        return 1
    if operator in ['*', '/']:
        return 2
    if operator == '^':
        return 4
    if operator == '(':
        return 5

def isp(operator):
    if operator in ['+', '-']:
        return 1
    if operator in ['*', '/']:
        return 2
    if operator == '^':
        return 3
    if operator == '(':
        return 0
    if operator == '#':
        return -1

def convert(infix):
    s = stack()
    s.push('#')
    postfix = ''
    for ch in infix:
        if ch.isalnum():
            postfix += ch
        elif ch == ')':
            while s.peek() != '(':
                postfix += s.pop()
            s.pop()
        else:
            while icp(ch) <= isp(s.peek()):
                postfix += s.pop()
            s.push(ch)
    while s.peek() != '#':
        postfix += s.pop()
    return postfix
infix = input('Enter infix expression : ')
postfix = convert(infix)
print('Postfix expression : ', postfix)