# Write a program to perform following operations on employee file i.e. binary file

from os.path import isfile
import pickle

def menu():
    print('\n1. Print binary file')
    print('2. Print ith record of the file')
    print('3. Number of records in the file')
    print('4. Append new record to the file')
    print('5. Exit')

class emp:

    def get(self):
        self.empno = int(input('Enter employee number : '))
        self.ename = input('Enter employee name : ')
        self.sal = float(input('Enter salary : '))

    def disp(self):
        print(self.empno, self.ename, self.sal)




def create(f):

    while True:
        e = emp()
        e.get()

        pickle.dump(e, f)

        ch = input('Do you want to continue (Y/N) : ')
        if ch in ['N', 'n']:
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
        pass

    return count


def disp_ith_record(f, i):

    f.seek(0)

    count = 1

    try:
        while True:

            e = pickle.load(f)

            if count == i:
                e.disp()
                return

            count += 1

        print('Record not found')

    except EOFError:
        print('Record not found')


def append(f, e):

    f.seek(0, 2)

    pickle.dump(e, f)

if isfile('emp.dat'):
    f = open('emp.dat', 'r+b')
else:
    f = open('emp.dat', 'w+b')
    create(f)
while True:

    menu()

    ch = int(input('Enter choice : '))

    match ch:

        case 1:
            display(f)

        case 2:
            i = int(input('Enter record number : '))
            disp_ith_record(f, i)

        case 3:
            print('Number of records : ', num_records(f))

        case 4:
            e = emp()
            e.get()
            append(f, e)

        case 5:
            f.close()
            break

        case _:
            print('Invalid choice')






# Write a program to create a zip file

from zipfile import ZipFile
zipname = input('Enter zip filename : ')

zf = ZipFile(zipname, 'w')

n = int(input('How many files ? : '))

for i in range(n):
    fname = input('Enter filename : ')
    zf.write(fname)
zf.close()

print(f'Zip file is created with {n} files')



'''
Write a program to print each file of zipfile

1) Print each file name and file contents

2) Also execute the file if it is a .py file

3) How to execute python file from python program ?
   ---> os.system('py filename.py')
'''

from zipfile import ZipFile
import os

def disp(f):

    print('\nFile Name : ', f.filename)
    print('-' * 40)
    data = f.read().decode()

    print(data)
    if f.filename.endswith('.py'):

        temp = open(f.filename, 'w')
        temp.write(data)
        temp.close()

        print('\nExecuting Python File...\n')

        os.system(f'py {f.filename}')


def display(z):

    for fname in z.namelist():

        f = z.open(fname)

        disp(f)

        f.close()
try:

    filename = input('Enter zip filename : ')

    z = ZipFile(filename, 'r')
    display(z)
    z.close()

except FileNotFoundError:

    print(f'{filename} file does not exist')








# Write a program to determine length of linked list

class node:

    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:

    def __init__(self):
        self.head = None

    def append(self, data):

        newnode = node(data)

        if self.head is None:
            self.head = newnode
        else:

            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = newnode


class sll(linked_list):

    def length(a):

        count = 0

        temp = a.head

        while temp is not None:

            count += 1

            temp = temp.next

        return count

l = sll()

n = int(input('How many nodes ? : '))

for i in range(n):

    x = int(input('Enter data : '))

    l.append(x)


print('Number of nodes : ', l.length())








'''
Write a program to determine data of ith node

1) Returns data of ith node if ith node exists

2) Returns None if ith node does not exist
'''

class node:

    def __init__(self, data):
        self.data = data
        self.next = None


class sll:

    def __init__(self):
        self.head = None

    def append(self, data):

        newnode = node(data)

        if self.head is None:
            self.head = newnode

        else:

            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = newnode


class linkedlist(sll):

    def find(a, i):

        temp = a.head

        count = 1

        while temp is not None:

            if count == i:
                return temp.data

            temp = temp.next

            count += 1

        return None

l = linkedlist()

n = int(input('How many nodes ? : '))

for i in range(n):

    x = int(input('Enter data : '))

    l.append(x)


while True:

    i = int(input("Enter value of 'i' : "))
    x = l.find(i)

    if x is None:

        print(f'Node {i} does not exist')

    else:

        print(f'Data of node {i} is : {x}')

    ch = input('Do you wish to continue (y / n) : ')

    if ch == 'N' or ch == 'n':
        break
print('Good Bye')









'''
Write a method to search for a value in the linked list.

1) Move reference to next node when x is not found

2) Return node where x is found

3) Return None when x is not found in linked list
'''

class node:

    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:

    def __init__(self):
        self.head = None

    def append(self, data):

        newnode = node(data)

        if self.head is None:
            self.head = newnode

        else:

            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = newnode


class singly_linked_list(linked_list):

    def search(a, x):

        temp = a.head

        while temp is not None:

            if temp.data == x:
                return temp

            temp = temp.next

        return None

l = singly_linked_list()

n = int(input('How many nodes ? : '))

for i in range(n):

    x = eval(input('Enter data : '))

    l.append(x)


while True:

    x = eval(input("Enter value to be searched : "))
    p = l.search(x)

    if p is None:

        print(f'{x} is not found')

    else:

        print(f'Found at that node whose address : {p}')

    ch = input('Do you wish to continue (y / n) : ')

    if ch == 'N' or ch == 'n':
        break

print('Good Bye')






'''
Write a method to insert a node in the linked list
'''

class node:

    def __init__(self, data):
        self.data = data
        self.next = None


class sll:

    def __init__(self):
        self.first = None

    def append(self, x):

        newnode = node(x)

        if self.first is None:
            self.first = newnode

        else:

            temp = self.first

            while temp.next is not None:
                temp = temp.next

            temp.next = newnode

    def display(self):

        temp = self.first

        while temp is not None:

            print(temp.data, end=' --> ')

            temp = temp.next

        print('None')


class linkedlist(sll):

    def insert(a, i, x):
        if i < 0:

            print(f'Node {i} does not exist')
        elif i == 0:

            # Create new node
            newnode = node(x)

            # Insert at beginning
            newnode.next = a.first
            a.first = newnode

        else:

            temp = a.first
            count = 1

            while temp is not None and count < i:

                temp = temp.next
                count += 1

            if temp is None:

                print(f'Node {i} does not exist')

            else:

                # Create new node
                newnode = node(x)

                # Insert after ith node
                newnode.next = temp.next
                temp.next = newnode

l = linkedlist()

n = int(input('How many nodes ? : '))

for i in range(n):

    x = eval(input('Enter data : '))

    l.append(x)


print('\nLinked List : ')
l.display()


while True:

    i = int(input("Enter value of 'i' : (0 - At the begin) : "))

    x = eval(input('Enter value to be inserted : '))
    l.insert(i, x)
    print('\nLinked List after insertion : ')
    l.display()

    ch = input('Would you like to insert another node (Y or N) ? : ')

    if ch == 'n' or ch == 'N':
        break