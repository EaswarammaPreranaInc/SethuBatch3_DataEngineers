#1
'''
Write a program to print distinct vowels of the string by using set
1) Let input be RamA Rao
   What is the output ? ---> AO (case is ignored)
2) Both input and output are strings
3) Hint: Same as prog19 with minor changes
'''
ipstr = "RamA Rao"
vowels = "aeiouAEIOU"
s = set()
for char in input_str:
    if char in vowels:
        s.add(char.upper())
result = "".join(s)
print(result)



#2
# How to access values of dictionary (Home work)
a = {'Empno' : 25 , 'Ename' : 'Rama Rao' , 'Sal' : 1000.65 }
print(a['Empno'])      # Access value 25
print(a['Ename'])      # Access 'Rama Rao'
print(a['Sal'])        # Access value 1000.65



#3
# How to modify values of dictionary (Home work)
a = {'Empno' : 25, 'Ename' : 'Rama Rao' , 'Sal' : 1000.65 }
print(a)
print(id(a))
a['Sal'] = 2000        # Modify 1000.65 to 2000
a['Ename'] = 'Sita'    # Modify 'Rama Rao' to 'Sita'
a['Empno'] = 35        # Modify 25 to 35
print(a)
print(id(a))



#4
# How to append key : value pairs to dictionary (Home work)
a = {'Empno' : 25, 'Ename' : 'Rama Rao' , 'Sal' : 1000.65 }
print(a)
a['Gender'] = 'M'      # Append 'Gender' : 'M'
a['Married'] = True    # Append 'Married' : True
print(a)



#5
# Find outputs (Home work)
a = { }
a[10] = 'Rama'         # Append 10 : 'Rama'
a[20] = 'Sita'         # Append 20 : 'Sita'
a[15] = 'Rajesh'       # Append 15 : 'Rajesh'
a[18] = 'Kiran'        # Append 18 : 'Kiran'
print(a)



#6
# How to remove key : value pairs of dictionary (Home work)
a = {'Empno' : 25, 'Ename' : 'Rama Rao' , 'Sal' : 1000.65 }
print(a)
del a['Sal']           # Remove 'Sal' : 1000.65
print(a)



#7
# in and not in operators (Home work)
a = {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30 in a.keys())      # True
print(60 in a.keys())      # False
print(60 in a.values())    # True
print(30 in a.values())    # False
print(50 in a)             # True
print(20 in a)             # False
print(70 not in a.keys())  # False
print(40 not in a.values())# False
print(25 not in a)         # True



#8
# What are the outputs if input is {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter dictionary : ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))



#9
# Find outputs (Home work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)
print(a is b)   # False
print(a == b)   # True
c = a
print(a is c)   # True
print(a == c)   # True



#10
# Find outputs (Home work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20 : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}      # Unpacks keys into a set
print(d)
print(type(d))
e = {**a , **b , **c}   # Merges into a dictionary
print(e)
print(type(e))



#11
# Find outputs (Home work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
# print(a + b)          # Error as concatenation of dictionaries can't be done via plus operator instead use pipe operator
c = {**a , **b}
print(c)
d = a | b               # Dictionary union operator
print(d)



#12
'''
(Home work)
Write a program to create a dictionary with emp names and salaries
Hint: Append each emp name and salary to dictionary 'a'
'''
a = {}
n = int(input("Enter number of entries: "))
for i in range(n):
    name = input("Enter Emp Name: ")
    sal = float(input("Enter Salary: "))
    a[name] = sal
print(a)



#13
''' (Home work)
Write a program to convert a string to dictionary
Let input be "Emp no = 25 , Emp name = Rama Rao , sal = 10000.0 , gender = m"
What is the output ? ---> {Emp no : 25 , Emp name : Rama Rao , sal : 10000.0 , gender : m}
Hint : Use split() method twice
'''
ipstr = "Emp no = 25 , Emp name = Rama Rao , sal = 10000.0 , gender = m"
a = {}
for pair in ipstr.split(','):
    key, val = pair.split('=')
    a[key.strip()] = val.strip()
print(a)