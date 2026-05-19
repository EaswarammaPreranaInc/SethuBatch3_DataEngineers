import os
list = ['a' , 'b']
print(list)
for x in list: # 'x' is 
list . append(x) 
print(list) # ['a' , 'b' ]['a' , 'b' ,'a']['a' , 'b' , 'a' , 'b']['a' , 'b' ,'a' , 'b' , 'a' ]....['a' , 'b' ,'a' , 'b' , 'a' , 'b' , 'a'..................'a' , 'b' ,...]it was a infinate loop.
os . system('pause')


# Modify the following program with writerows() method
import csv
def create(f):
w = csv . writer(f)
w . writerow(['EMP NO' , 'EMP NAME' , 'SALARY'])
n = eval(input('How Many Employees ? : ')) # 3
list=[]
for i in range(n): # Iteration 3
empno = eval(input('Enter Employee No : '))
ename = input('Enter Employee Name : ')
sal = eval(input('Enter Employee Salary : '))
list.append([empno,ename,sal])
w . writerows(list)
# End of for loop
print(F'File {f . name} is created')
# End of the function
fname = input('Enter filename : ') # emp.csv
f = open(fname , 'w' , newline ="")
create(f)
f . close()


# Write a program to print csv file
import csv
def disp(f):
for x in r:
print(*x)#How to itertae thru csv file using reader object
# End of function
try:
fname=input("enter the file name:")#How to read the filename
f=open(fname,"r")#How to open the file
r=csv.reader(f)
disp(f)#How to print the file
f.close()#How to close the file 
except FileNotFoundError:
print(F'File {fname} does not exist')
