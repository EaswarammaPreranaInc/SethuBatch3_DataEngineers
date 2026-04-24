'''class c1:
    x = 10

    def m1(self):
        self.y = 20
        z = 30
        c1.m = 40


def f1():
    a = c1()
    a.p = 50
    c1.q = 60
    s = 70


k = 80

c1.l = 90

b = c1()
b.n = 100

# No outputs'''


'''class person:
    def __init__(self):
        self.name = ''

    @property
    def name(self):
        print('getter method')
        return self._name

    @name.setter
    def name(self, value):
        print('Setter Method')
        self._name = value

    @name.deleter
    def name(self):
        print('Deleter Method')
        del self._name

    def __del__(self):
        print('Destructor')


p = person()
print(p.name)
p.name = 'Vamsi'
print(p.name)
del p.name
# print(p.name)
del p'''

'''Outputs:
Setter Method
getter method

Setter Method
getter method
Vamsi
Deleter method
getter method
AttributeError
Destructor'''


'''import time
lst = [25 , 10.8 , 'Hyd' , True]

e = enumerate(lst, start=5)

while True:
    try:
        print(next(e))
        time.sleep(1)
    except StopIteration:
        break

#print(lst[5])

#Outputs:
#(5, 25)
#(6, 10.8)
#(7, 'Hyd')
#(8, True)
#Indexerror'''


'''import time
a = 'Hyd'

e = enumerate(a)

while True:
    try:
        print(next(e))
        time.sleep(1)
    except StopIteration:
        break

#outputs:
# (0, 'H')
# (1, 'y')
# (2, 'd')'''


'''import time
a = {25 , 10.8 , 'Hyd' , True , 3+4j}

print(a)

b = enumerate(a)

while True:
    try:
        print(next(b))
        time.sleep(1)
    except StopIteration:
        break
'''

# output:
# (0, True)
# (1, 'Hyd')
# (2, 25)
# (3, 10.8)
# (4, (3+4j))
# unordered as it is a set


'''import time
def disp(e):
    while True:
        try:
            print(next(e))
            time.sleep(1)
        except StopIteration:
            break
    print()


d = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}

e1 = enumerate(d.keys())
disp(e1)

e2 = enumerate(d.values())
disp(e2)

e3 = enumerate(d.items())
disp(e3)

e4 = enumerate(d, start=5)
disp(e4)'''

'''Outputs:
(0, 'Empno')
(1, 'Emp Name')
(2, 'Sal')

(0, 25)
(1, 'Rama Rao')
(2, 10000.0)

(0, ('Empno', 25))
(1, ('Emp Name', 'Rama Rao'))
(2, ('Sal', 10000.0))

(5, 'Empno')
(6, 'Emp Name')
(7, 'Sal')'''

'''import time

a = ['Telangana', 'Andhra Pradesh', 'Karnataka' , 'Tamil Nadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi', 'Bangalore', 'Chennai', 'Mumbai']

e = enumerate(a)

for index ,element in e:
    print(f'{element:20}...{b[index]}')
    time.sleep(1)'''

'''#outputs:
Telangana           ...Hyderabad
Andhra Pradesh      ...Amaravathi
Karnataka           ...Bangalore
Tamil Nadu          ...Chennai
Maharastra          ...Mumbai'''
