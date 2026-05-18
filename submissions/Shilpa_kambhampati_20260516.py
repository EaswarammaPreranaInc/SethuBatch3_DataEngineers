#  Write   a  program   to  perform  following  operations  on  employee  file  i.e.  binary  file
from os.path import isfile
import pickle
def menu():
    print('1. Print binary file')
    print('2. Print ith record of the file')
    print('3. Number of records in the file')
    print('4. Append new record to the file')
    print('5. Exit')
class emp:
    def __init__(self):
        self.empno = 0
        self.ename = ""
        self.sal = 0.0
    def get(self):
        self.empno = int(input('Enter employee number: '))
        self.ename = input('Enter employee name: ')
        self.sal = float(input('Enter salary: '))
    def disp(self):
        print(f'EmpNo: {self.empno} | Name: {self.ename} | Salary: {self.sal}')
# End of the class
def create(f):
    while True:
        e = emp()
        e.get()
        pickle.dump(e, f)
        ch = input('Add another record? (Y/N): ')
        if ch.lower() == 'n':
            break
def display(f):
    f.seek(0)  
    try:
        while True:
            e = pickle.load(f)
            e.disp()
    except EOFError:
        pass 
def num_records(f):
    f.seek(0)
    count = 0
    try:
        while True:
            pickle.load(f)
            count += 1
    except EOFError:
        return count
def disp_ith_record(f, i):  
    f.seek(0)
    try:
        for _ in range(i):
            e = pickle.load(f)
        e.disp()
    except EOFError:
        print(f'Record {i} does not exist')
def append(f, e):
    f.seek(0, 2)  
    pickle.dump(e, f)

# How to open the file in r+ mode if it is existing and w+ mode if it is not existing
filename = 'employee.dat'
if isfile(filename):
    f = open(filename, 'rb+')
else:
    f = open(filename, 'wb+')
    create(f)  # create initial records if file is new

while True:
    menu()
    ch = int(input('Enter choice: '))
    match ch:
        case 1:
            # How to print the file
            print('\n--- All Employee Records ---')
            display(f)
            print('----------------------------\n')
        case 2:
            i = int(input('Enter record number : '))
            # How to print ith object of the file
            print(f'\n--- Record {i} ---')
            disp_ith_record(f, i)
            print('-----------------\n')
        case 3:
            print('Number of records : ', num_records(f))
        case 4:
            # How to append an object to the file
            print('\n--- Enter new employee details ---')
            e = emp()
            e.get()
            append(f, e)
            print('Record appended successfully\n')
        case 5:
            # How to stop execution
            f.close()
            print('Exiting...')
            break
        case _:
            print('Invalid choice\n')


# Write  a  program  to  create  a  zip  file
from zipfile import ZipFile
import os

# How to read zip filename
zip_name = input('Enter zip filename: ')
if not zip_name.endswith('.zip'):
    zip_name += '.zip'

# How to open zip file
with ZipFile(zip_name, 'w') as zipf:
    n = int(input('How many files? : '))
    for i in range(n):
        # How to read each filename
        filename = input(f'Enter filename {i+1}: ')
        
        # Check if file exists before adding
        if os.path.isfile(filename):
            # How to write each file to zip file
            zipf.write(filename)
            print(f'Added {filename}')
        else:
            print(f'File {filename} not found, skipping...')
# How to close zip file - 'with' closes it automatically

print(f'zip file {zip_name} is created with {n} files')


'''
Write  a  program  to  print  each  file  of  zipfile

Let  zip  file  contain  1.py , 2.txt , 3.py , 4.txt , 5.py

1) Print  each  file  name  and   file  contents

2) Also  execute  the  file  if  it  is  a  py  file

3) How  to  execute  python  file  from  python  program ?  --->  os . system('py   filename.py')
'''
from zipfile import ZipFile
import os

def disp(f, zip_obj):
    # How to print content of the file and also execute the file if it is .py file
    print(f'\n{"="*10} {f} {"="*10}')
    
    # Read file content from zip
    content = zip_obj.read(f).decode('utf-8', errors='ignore')
    print('File Content:')
    print(content)
    
    # Execute if .py file
    if f.endswith('.py'):
        print('\nExecuting python file:')
        # Extract to temp location first because os.system needs actual file
        zip_obj.extract(f, 'temp_exec')
        os.system(f'py temp_exec/{f}')  # use 'python3' on Linux/Mac
        # Optional: clean up extracted file
        os.remove(f'temp_exec/{f}')
        os.rmdir('temp_exec')

def display(z):
    # How to call disp() function to print each file of zip file
    for file in z.namelist():
        disp(file, z)
# End of the function

try:
    # How to read filename
    filename = input('Enter zip filename: ')
    if not filename.endswith('.zip'):
        filename += '.zip'
    
    # How to open zip file
    with ZipFile(filename, 'r') as z:
        # How to print display() to print zip file
        display(z)
    # How to close the file - 'with' closes automatically
    
except FileNotFoundError:
    print(f'{filename} file does not exist')
except Exception as e:
    print(f'Error: {e}')

# Write  a  program  to  determine  length  of  linked  list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll:  # singly linked list
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def length(self):
        # How to count each node of linked list and return number of nodes
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
# End of the class

# How to create a linked list
a = sll()
a.append(10)
a.append(20)
a.append(30)
a.append(40)

print('Number of nodes : ', a.length())  # Output: Number of nodes : 4


	  


'''
Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  ---> Returns  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Returns  None
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll: # base singly linked list
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

class linkedlist(sll):
    def find(self, i):
        # return data of ith node if ith node exists and None otherwise
        if i <= 0: # 1-indexed: node 1 is head
            return None
        temp = self.head
        count = 1
        while temp:
            if count == i:
                return temp.data
            temp = temp.next
            count += 1
        return None # ith node does not exist
# End of the class

# How to create a linked list
a = linkedlist()
a.append(10)
a.append(20)
a.append(30)
a.append(40)
a.append(50)

while True:
    i = int(input("Enter value of 'i': "))
    # How to obtain data of ith node
    data = a.find(i)
    if data is None:
        print(f'Node {i} does not exist')
    else:
        print(f'Data of node {i} is : {data}')
    ch = input('Do you wish to continue (y / n) : ')
    if ch == 'N' or ch == 'n':
        break
# End of while loop
print('Good Bye')


'''
Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  the  node   where  'x'  is  found

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:  # base class
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

class singly_linked_list(linked_list):
    def search(self, x):
        # Return that node where 'x' is found and None otherwise
        temp = self.head
        while temp:  # 1) Move reference to next node when 'x' is not in current node
            if temp.data == x:  # 2) Return the node where 'x' is found
                return temp
            temp = temp.next  # Move to next node
        return None  # 3) Return None outside loop when 'x' not found
# End of the class

# How to create a linked list
a = singly_linked_list()
a.append(10)
a.append(20)
a.append(30)
a.append(40)

while True:
    x = eval(input("Enter value to be searched : "))
    # How to search for 'x' in the linked list
    result = a.search(x)
    if result is None:
        print(f'{x} is not found')
    else:
        print(f'Found at that node whose address : {result}')
        print(f'Data at found node : {result.data}')
    ch = input('Do you wish to continue (y / n) : ')
    if ch == 'N' or ch == 'n':
        break
# End of while loop
print('Good Bye')

'''
Write  a  method  to  insert  a  node  in  the  linked  list
1) How  many  links  have  to  be  modified  for  insertion ?  --->  Two  links

2) How  to  insert  a  node  at  the  begining  of  linked list ?  --->  Modify  new  node  link  to  1st  node
																														and
																									   modify  reference  a . first  to  new  node

3) How  to  insert  a  node  at  the  end  of  linked list ?  --->  Modify  new  node  link  to  None
																												and
																								modify  last  node  link  to  new  node

4) How  to  insert  a  node  after  ith  node ?  --->  Modify  new  node  link  to  (i + 1)th  node  and
																		       modify  ith  node  link   to  new  node

5) In  which  order  can  links  be  modified ?  --->  Modify  new  node  link  first  and  then  existing  node  link

6) Is  logic  same  for  middle  insertion  and  insertion  at  the  end  ? --->  Yes

7) What  is  the  difference  between  insertion  at  the  begining  and  insertion  anywhere  else ?  --->															
															a . first  is  modified  when  node  is   inserted  at  the  begining  and
															a . first  reference  remains  unchanged  when  node  is   inserted  anywhere  else
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.first = None  # using 'first' as per your hints
    
    def display(self):
        temp = self.first
        if not temp:
            print('List is empty')
            return
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')
    
    def length(self):
        count = 0
        temp = self.first
        while temp:
            count += 1
            temp = temp.next
        return count

class linkedlist(sll):
    def insert(self, i, x):
        # 1) Two links have to be modified for insertion
        
        if i < 0 or i > self.length():
            # if 'i' is an invalid node number:
            print(f'Node {i} does not exist')
            return
            
        elif i == 0:  # insertion at the beginning of linked list
            # How to create a new node with value 'x'
            new_node = Node(x)
            # How to insert a node at the beginning of linked list
            # 5) Modify new node link first and then existing node link
            new_node.next = self.first  # new node link to 1st node
            self.first = new_node       # modify reference a.first to new node
            
        else:  # insert after ith node - covers middle and end
            # How to create a new node with value 'x'
            new_node = Node(x)
            # How to insert the node after ith node of LL
            temp = self.first
            for _ in range(1, i):  # move to ith node
                temp = temp.next
            # 5) Modify new node link first and then existing node link
            new_node.next = temp.next  # new node link to (i+1)th node
            temp.next = new_node       # ith node link to new node
# End of the class

# How to create a linked list
a = linkedlist()
a.insert(0, 30)  # 30
a.insert(0, 10)  # 10 -> 30  
a.insert(1, 20)  # 10 -> 20 -> 30

while True:
    a.display()
    i = int(input("Enter value of 'i' : (0 - At the begin) "))
    x = eval(input('Enter value to be inserted : '))
    # How to insert 'x' after ith node
    a.insert(i, x)
    # How to print linked list
    print('Linked list after insertion:')
    a.display()
    ch = input('Would you like to insert another node (Y or N) ? : ')
    if ch == 'n' or ch == 'N':
        break










