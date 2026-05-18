1) Write  a  function  to  return  average  of  numbers  in  the  file

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

#def avg(f):
    sum = 0
    ctr = 0
    while True:
        data = f.readline().strip()
        if data == 'eof':
            break
        sum = sum + eval(data)
        ctr = ctr + 1
    return sum / ctr
fname = input('Enter filename : ')
f = open(fname, 'r')
print('Average of numbers in the file : %.2f' % avg(f))
f.close()


2) Write  a  program  to  merge  two  files  to  form  a  new  file

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
import os
def copy(file1, file2):
    while True:
        data = file1.readline()
        if data == '':
            break
        file2.write(data)
fname1 = input("Enter first file name : ")
fname2 = input("Enter second file name : ")
fname3 = input("Enter third file name : ")
if os.path.exists(fname1) and os.path.exists(fname2):
    f1 = open(fname1, 'r')
    f2 = open(fname2, 'r')
    f3 = open(fname3, 'w')
    copy(f1, f3)
    copy(f2, f3)
    f1.close()
    f2.close()
    f3.close()
    print(f'{fname1} and {fname2} are copied to {fname3}')
elif os.path.exists(fname1):
    f1 = open(fname1, 'r')
    f3 = open(fname3, 'w')
    copy(f1, f3)
    f1.close()
    f3.close()
    print(f'{fname1} is copied to {fname3}')
elif os.path.exists(fname2):
    f2 = open(fname2, 'r')
    f3 = open(fname3, 'w')
    copy(f2, f3)
    f2.close()
    f3.close()
    print(f'{fname2} is copied to {fname3}')
else:
    print('Both the files are not existing')
    if os.path.exists(fname3):
        os.remove(fname3)

3) Write   a  program  to  count  number  of   lines , characters , words , vowels , consonants ,  spaces , tabs  and
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
def count_all(f):
    s = f.read()
    a = []
    a.append(s.count('\n') + 1)
    a.append(len(s))
    a.append(len(s.split()))
    a.append(s.count(' '))
    a.append(s.count('\t'))
    a.append(s.count('.') + s.count('?') + s.count('!'))
    vowels = 0
    consonants = 0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels = vowels + 1
            else:
                consonants = consonants + 1
    a.append(vowels)
    a.append(consonants)
    return a
fname = input("Enter filename : ")
f = open(fname, "r")
a = count_all(f)
f.close()
b = ['Lines', 'Chars', 'Words', 'Spaces','Tabs', 'Sentences', 'Vowels', 'Consonants']
for i in range(len(a)):
    print(f"{b[i]}...{a[i]}")

4) Write  a  function  to  search  for  a  word  in  the  file  and   return  number  of  times  it  is  found

File
----
Hyd  is  green  city.
Hyd  is  hitec  city.
Hyd  is  beautiful  city.

str  object  --->  Hyd  is  green  city.\nHyd  is  hitec  city.\nHyd  is  beautiful  city.\n

What  is  the  result  when  'Hyd'  is  searched  in  the  file ?  --->   3
'''
def search(f, word):
    s = f.read()
    return s.count(word)
fname = input("Enter filename : ")
f = open(fname, "r")
word = input("Enter the word to be searched : ")
print(f"{word} is present {search(f, word)} times in the file")
f.close()


5) Write  a  program  to  write  0! ,  1! , 2!, ...... n!  to  the  file

Hint:  Use  math . factorial()  function
'''
import  math
def  fact(f , n):
	How  to  write  i  and  i!  to  the  file  where  'i'  varies  from  0  to  n
# End  of  the  function
How  to  read  filename
How  to  open  the  file
How  to  read  value  of  'n'
How  to  write  all  the  results  to  the  file
How  to  close  the  file



6) Write  a   program  to  remove  all  the   comments  in  a  python  file

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
    fw = open(f.name, 'w')
    for line in lines:
        temp = line.lstrip()
        if temp.startswith('#'):
            fw.write(temp)
        elif '#' in line:
            fw.write(line[:line.index('#')].rstrip() + '\n')
        else:
            fw.write(line)
    fw.close()
try:
    fname = input('Enter filename : ')
    f = open(fname, 'r')
    cmt_remove(f)
    f.close()
    print(f'All the single line comments are removed from {f.name}')
except:
    print('File does not exist')

7) outputs  
f = open('a.txt' , 'w+')
f . write('Hyd is green city.') # Hyd is green city.
f . seek(0) # 18
f . write('Sec') # Sec is green city.
f . seek(0) # 3
print(f . read())  # Sec is green city. 
f . seek(7) # 18
print(f . read(5)) # green
f . seek(0 , 2) # 12
f . write('Hyd is Hitec city.') # Sec is green city.Hyd is Hitec city.
f . seek(0) # 36
print(f . read())  # Sec is green city.Hyd is Hitec city.
f . seek(7) # 36
f . write('red') # Sec is reden city.Hyd is Hitec city.
f . seek(0) # 10
print(f . read())  # Sec is reden city.Hyd is Hitec city.

8) outputs 
f = open('a.txt' , 'w+')
print(f . tell()) # 0
f . write('Hyd is green city')
print(f . tell())  # 17 
f . seek(7) # green 12
print(f . read(5))  # 12 
print(f . tell())   # 12

9) Write  a  program  to  evaluate  prefix  expression

Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -
from prog7b import *
def eval(prefix):
    s = stack()
    prefix = prefix[::-1]
    for ch in prefix:
        if ch.isdigit():
            s.push(int(ch))
        else:
            x = s.pop()
            y = s.pop()
            match ch:
                case '+':
                    s.push(x + y)
                case '-':
                    s.push(x - y)
                case '*':
                    s.push(x * y)
                case '/':
                    s.push(x // y)
                case '^':
                    s.push(x ** y)
    return s.pop()
prefix = input('Enter prefix expression : ')
print('Result : ', eval(prefix))

10) Write  a  program  to  convert  postfix  to  prefix
from prog1b import stack
def convert(postfix):
    s = stack()
    for ch in postfix:
        if ch.isalnum():
            s.push(ch)
        else:
            y = s.pop()
            x = s.pop()
            temp = ch + x + y
            s.push(temp)
    return s.pop()
postfix = input('Enter postfix expression : ')
prefix = convert(postfix)
print('Prefix expression : ', prefix)

11) Write  a  program  to  implement  min  priority  queue  using  list
class priority_queue:
    def __init__(pq):
        pq.lst = []
    # pq = priority_queue()

    def isempty(pq):
        return pq.lst == []
    # pq.isempty()

    def insert(pq, x):
        pq.lst.append(x)
    # pq.insert(25)

    def delete(pq):
        try:
            x = min(pq.lst)
            pq.lst.remove(x)
            return x
        except:
            return None
    # x = pq.delete()

    def highest_priority(pq):
        try:
            return min(pq.lst)
        except:
            return None
    # x = pq.highest_priority()

    def smallest_priority(pq):
        try:
            return max(pq.lst)
        except:
            return None
    # x = pq.smallest_priority()

    def disp(pq):
        print('Priority Queue : ', pq.lst)
    # pq.disp()
    
    def size(pq):
        return len(pq.lst)
    # pq.size()
# End of the class

def menu():
    print('1. Insertion')
    print('2. Deletion')
    print('3. Print priority queue')
    print('4. Highest priority element of priority queue')
    print('5. Smallest priority element of priority queue')
    print('6. Number of elements in the priority queue')
    print('7. Exit')
pq = priority_queue()
while True:
    menu()
    ch = int(input('Enter choice : '))
    match ch:
        case 1:
            x = eval(input('Enter element to be inserted : '))
            pq.insert(x)
            pq.disp()
        case 2:
            x = pq.delete()
            if x == None:
                print('Priority queue is empty , deletion is not permitted')
            else:
                print('Deleted element : ', x)
            pq.disp()
        case 3:
            pq.disp()
        case 4:
            x = pq.highest_priority()
            if x == None:
                print('Priority queue is empty')
            else:
                print('Highest priority element : ', x)
        case 5:
            x = pq.smallest_priority()
            if x == None:
                print('Priority queue is empty')
            else:
                print('Smallest priority element : ', x)
        case 6:
            print('Number of elements : ', pq.size())
        case 7:
            break


12) Write  functions  to  create  and  print  linked  list
class node:
    def __init__(self, x):
        self.data = x
        self.link = None
    '''
    1) new = node(25)
    2) object new ---> data = 25 , link = None 
    '''

class linked_list:
    def __init__(a):
        a.first = None
    '''
    1) a = linked_list()
    2) Object 'a' ---> first = None 
    '''
    def isempty(a):
        return a.first == None

    def disp(a):
        if a.isempty():
            print('Linked List is empty')
        else:
            p = a.first
            while p != None:
                print(p.data, end='\t')
                p = p.link
            print()
    # a.disp()

    def append(a, new):
        if a.isempty():
            a.first = new
        else:
            p = a.first
            while p.link != None:
                p = p.link
            p.link = new
    # a.append(new)

    def create(a):
        while True:
            x = eval(input('Enter element : '))
            new = node(x)
            a.append(new)
            ch = input('Do you want another node (yes/no) : ')
            if ch.lower() == 'no':
                break
    # a.create()
    
a = linked_list()
a.create()
print('Linked List : ', end='')
a.disp()