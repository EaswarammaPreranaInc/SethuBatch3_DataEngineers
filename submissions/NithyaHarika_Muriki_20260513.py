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
def avg(f):
    s = 0.0
    ctr = 0
    for line in f:
        line = line.strip()
        if not line:
            continue
        # try to convert to float; bools convert to 1/0 via int/float so handled naturally
        try:
            val = float(line)
        except ValueError:
            # skip non-numeric lines (eg 'eof')
            continue
        s += val
        ctr += 1
    return (s / ctr) if ctr else None
# usage
fname = input('Enter filename : ')
with open(fname, 'r') as f:
    res = avg(f)
if res is None:
    print('No numeric data found')
else:
    print('Average of numbers in the file :', res)


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
import os

def copy(filer, filew):
    # copy contents of opened readable file `filer` to opened writable file `filew`
    for line in filer:
        filew.write(line)

fname1 = input('Enter first filename : ')
fname2 = input('Enter second filename : ')
fname3 = input('Enter output filename : ')

exists1 = os.path.exists(fname1)
exists2 = os.path.exists(fname2)

if exists1 and exists2:
    with open(fname1, 'r') as f1, open(fname2, 'r') as f2, open(fname3, 'w') as f3:
        copy(f1, f3)
        copy(f2, f3)
    print(f'{fname1} and {fname2} are merged to form {fname3}')
elif exists1:
    with open(fname1, 'r') as f1, open(fname3, 'w') as f3:
        copy(f1, f3)
    print(f'{fname1} is copied to {fname3}')
elif exists2:
    with open(fname2, 'r') as f2, open(fname3, 'w') as f3:
        copy(f2, f3)
    print(f'{fname2} is copied to {fname3}')
else:
    print('Both the files are not existing')
    # if output file was created earlier and you want to remove it, uncomment:
    # if os.path.exists(fname3): os.remove(fname3)


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
def count_all(f):
    text = f.read()
    lines = text.count('\n')
    # If file doesn't end with newline, the number of lines is lines+1 when there's any text
    if text and not text.endswith('\n'):
        lines += 1
    chars = len(text)
    words = len(text.split())
    spaces = text.count(' ')
    tabs = text.count('\t')
    # sentences approximated by '.', '!' or '?' occurrences
    sentences = sum(text.count(p) for p in ('.', '!', '?'))
    vowels = sum(1 for ch in text.lower() if ch in 'aeiou')
    consonants = sum(1 for ch in text.lower() if ch.isalpha() and ch not in 'aeiou')
    return [lines, chars, words, spaces, tabs, sentences, vowels, consonants]

fname = input('Enter filename : ')
with open(fname, 'r') as f:
    a = count_all(f)
b = ['Lines', 'Chars', 'Words', 'Spaces', 'Tabs', 'Sentences', 'Vowels', 'Consonants']
print(b)
print(a)

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
def search(f, word):
    text = f.read()
    # simple word-boundary search: split into tokens and count exact matches
    tokens = []
    # replace common punctuation with spaces so words at sentence ends count
    import string
    trans = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    tokens = text.translate(trans).split()
    return sum(1 for t in tokens if t == word)

fname = input('Enter filename : ')
word = input('Enter word to search : ')
with open(fname, 'r') as f:
    cnt = search(f, word)
print(f"'{word}' found {cnt} times")


'''
Write  a  program  to  write  0! ,  1! , 2!, ...... n!  to  the  file

Hint:  Use  math . factorial()  function
'''
import math
def fact(f, n):
    for i in range(n + 1):
        f.write(f'{i} {math.factorial(i)}\n')

fname = input('Enter filename : ')
n = int(input('Enter n : '))
with open(fname, 'w') as f:
    fact(f, n)
print('Factorials written')


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
def cmt_remove(f):
    lines = f.readlines()
    out_lines = []
    for line in lines:
        stripped = line.lstrip()
        # if line starts with '#' after stripping leading spaces -> keep as-is
        if stripped.startswith('#'):
            out_lines.append(line.rstrip('\n') + '\n')
            continue
        # otherwise, if there is a '#' somewhere, remove from the '#' to end of line
        if '#' in line:
            idx = line.find('#')
            new_line = line[:idx].rstrip()
            out_lines.append(new_line + '\n' if new_line else '\n')
        else:
            out_lines.append(line)
    return out_lines

try:
    fname = input('Enter python filename : ')
    with open(fname, 'r') as f:
        new = cmt_remove(f)
    # overwrite the same file (or use a new filename if you prefer)
    with open(fname, 'w') as f:
        f.writelines(new)
    print(f'All the single line comments are removed from {fname}')
except FileNotFoundError:
    print('File does not exist')

# Find outputs (Home work)
f = open('a.txt', 'w+')
f.write('Hyd is green city.')
f.seek(0)
f.write('Sec')
f.seek(0)
print(f.read())   # Sec is green city.
f.seek(7)
print(f.read(5))  #  green
f.seek(0, 2)
f.write('Hyd is Hitec city.')
f.seek(0)
print(f.read())   # Sec is green city.Hyd is Hitec city.
f.seek(7)
f.write('red')
f.seek(0)
print(f.read())   # Sec is gred city.Hyd is Hitec city.
f.close()


# Find outputs (Home work)
f = open('a.txt', 'w+')
print(f.tell())        # 0
f.write('Hyd is green city')
print(f.tell())        # 18 (length of written string)
f.seek(7)
print(f.read(5))       # '' because file pointer at 7 but file was opened for writing and not rewound for reading; after write, reading requires seek; for safety, do seek(7) then f.seek(7); reopen:
f.seek(0)
f.write('Hyd is green city')
f.seek(7)
f.seek(7)
# to read, we must reopen or switch mode properly:
f.close()
f = open('a.txt', 'r+')
f.seek(7)
print(f.read(5))       # green
print(f.tell())        # 12
f.close()


'''
Write  a  program  to  evaluate  prefix  expression

Prefix  expression :   -  +  3  *  4  5  /  6  2
Reverse  of  prefix :   2  6  /  5  4  *  3  +  -
'''
def eval_prefix(tokens):
    # tokens is list like ['-', '+', '3', '*', '4', '5', '/', '6', '2']
    stack = []
    # process tokens from right to left (reverse)
    for tok in reversed(tokens):
        if tok.lstrip('-').replace('.', '', 1).isdigit():
            # numeric literal
            if '.' in tok:
                stack.append(float(tok))
            else:
                stack.append(int(tok))
        else:
            # operator: pop two operands
            a = stack.pop()
            b = stack.pop()
            if tok == '+':
                stack.append(a + b)
            elif tok == '-':
                stack.append(a - b)
            elif tok == '*':
                stack.append(a * b)
            elif tok == '/':
                stack.append(a / b)
            else:
                raise ValueError('Unsupported operator')
    return stack[0]

prefix = '- + 3 * 4 5 / 6 2'.split()
print('Prefix expression:', ' '.join(prefix))
# reverse shown in problem: '2 6 / 5 4 * 3 + -'
print('Reverse of prefix :', ' '.join(reversed(prefix)))
print('Value =', eval_prefix(prefix))


#  Write  a  program  to  convert  postfix  to  prefix
def postfix_to_prefix(tokens):
    stack = []
    for tok in tokens:
        if tok.lstrip('-').replace('.', '', 1).isdigit():
            stack.append(tok)
        else:
            # operator
            op2 = stack.pop()
            op1 = stack.pop()
            new = tok + ' ' + op1 + ' ' + op2
            stack.append(new)
    return stack[0]

postfix = '3 4 5 * + 6 2 / -'.split()
print('Postfix :', ' '.join(postfix))
print('Prefix  :', postfix_to_prefix(postfix))


# Write  a  program  to  implement  min  priority  queue  using  list
class priority_queue:
    def _init_(pq):
        pq.lst = []
    def isempty(pq):
        return len(pq.lst) == 0
    def insert(pq, x):
        pq.lst.append(x)
        pq.lst.sort()   # keep sorted ascending so smallest at index 0
    def delete(pq):
        try:
            return pq.lst.pop(0)  # remove smallest
        except IndexError:
            return None
    def highest_priority(pq):
        try:
            return pq.lst[0]
        except IndexError:
            return None
    def smallest_priority(pq):
        try:
            return pq.lst[-1]
        except IndexError:
            return None
    def disp(pq):
        print('Priority Queue :', pq.lst)
    def size(pq):
        return len(pq.lst)

def menu():
    print('1. Insertion')
    print('2. Deletion')
    print('3. Print priority queue')
    print('4. Highest priority element of priority queue')
    print('5. Smallest priority element of priority queue')
    print('6. Number of elements in the priority queue')
    print('7. Exit')

pq = priority_queue()
pq.lst = []
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
            if x is None:
                print('Priority queue is empty , deletion is not permitted')
            else:
                print('Deleted element :', x)
            pq.disp()
        case 3:
            pq.disp()
        case 4:
            x = pq.highest_priority()
            if x is None:
                print('Priority queue is empty')
            else:
                print('Highest priority element :', x)
        case 5:
            x = pq.smallest_priority()
            if x is None:
                print('priority queue is empty')
            else:
                print('Smallest priority element :', x)
        case 6:
            print('Number of elements :', pq.size())
        case 7:
            break


#  Write  functions  to  create  and  print  linked  list
class node:
    def __init__(self, x):
        self.data = x
        self.link = None
    """
    1) new = node(25)
    2) object new ---> data = 25, link = None
    """

class linked_list:
    def __init__(self):
        self.first = None
    """
    1) a = linked_list()
    2) object 'a' ---> first = None
    """

    def isempty(self):
        return self.first is None
    # a.isempty() ---> True / False

    def disp(self):
        if self.isempty():
            print('Linked List is empty')
        else:
            p = self.first
            while p is not None:
                print(p.data, end='\t')
                p = p.link
            print()
    # a.disp()

    def append(self, new_node):
        """Append a node object new_node to the list."""
        if self.first is None:
            # append to empty linked list
            self.first = new_node
            return
        # append to non-empty linked list: walk to last and link
        p = self.first
        while p.link is not None:
            p = p.link
        p.link = new_node
    # a.append(new_node)

    def create(self, values):
        """Create linked list from an iterable of values (appends in order)."""
        for v in values:
            self.append(node(v))
    # a.create()

# Helper functions (optional)
def create_from_input(prompt='Enter values separated by space: '):
    """Read a line of input, split by whitespace, convert tokens to int when possible,
    otherwise keep as string. Returns list of values."""
    raw = input(prompt).strip()
    if not raw:
        return []
    vals = []
    for tok in raw.split():
        # try integer, then float, else keep string
        try:
            iv = int(tok)
            vals.append(iv)
            continue
        except ValueError:
            pass
        try:
            fv = float(tok)
            vals.append(fv)
            continue
        except ValueError:
            pass
        vals.append(tok)
    return vals

a = linked_list()
a.create([10, 20, 30])
print('Linked List : ', end='')
a.disp()   
a.append(node(40))
print('Linked List : ', end='')
a.disp()